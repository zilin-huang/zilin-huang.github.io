"""Lightly compress only the largest photos so they drop under a size cap.

Conservative by design: it does NOT resize, and it picks the *highest* JPEG
quality that still gets the file under TARGET_MB, so visible quality loss is
minimal. EXIF/ICC metadata is preserved. Originals are tracked by git, so the
operation is reversible.

Usage:
    python scripts/compress_large_photos.py            # compress + report
    python scripts/compress_large_photos.py --dry-run  # only report
"""

from __future__ import annotations

import argparse
import io
import os
from PIL import Image

ASSETS_DIR = "assets"
# Only touch photos larger than this.
THRESHOLD_MB = 10.0
# Aim a little below 10 MB so results sit comfortably under the cap.
TARGET_MB = 9.0
# Highest -> lowest quality to try; the first one under TARGET_MB wins.
QUALITY_LADDER = [98, 95, 92, 90, 88, 85]


def mb(num_bytes: int) -> float:
    return num_bytes / (1024 * 1024)


def encode_jpeg(im: Image.Image, quality: int, exif: bytes, icc: bytes) -> bytes:
    buf = io.BytesIO()
    save_kwargs = {
        "format": "JPEG",
        "quality": quality,
        "optimize": True,
        "progressive": True,
    }
    if exif:
        save_kwargs["exif"] = exif
    if icc:
        save_kwargs["icc_profile"] = icc
    im.save(buf, **save_kwargs)
    return buf.getvalue()


def compress(path: str, dry_run: bool = False) -> int:
    src_bytes = os.path.getsize(path)
    im = Image.open(path)
    im.load()
    exif = im.info.get("exif", b"")
    icc = im.info.get("icc_profile", b"")

    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")

    target = int(TARGET_MB * 1024 * 1024)
    chosen_q = None
    chosen_data = None
    for q in QUALITY_LADDER:
        data = encode_jpeg(im, q, exif, icc)
        if len(data) <= target:
            chosen_q, chosen_data = q, data
            break

    # Fall back to the lowest quality on the ladder if none hit the target.
    if chosen_data is None:
        chosen_q = QUALITY_LADDER[-1]
        chosen_data = encode_jpeg(im, chosen_q, exif, icc)

    dst_bytes = len(chosen_data)
    print(
        f"{path}\n"
        f"  {mb(src_bytes):.2f} MB -> {mb(dst_bytes):.2f} MB "
        f"(q={chosen_q}, {100 * (1 - dst_bytes / src_bytes):.0f}% smaller)",
        flush=True,
    )

    if dry_run:
        print("  [dry-run] not written\n", flush=True)
        return src_bytes

    if dst_bytes >= src_bytes:
        print("  re-encode not smaller, leaving original\n", flush=True)
        return src_bytes

    with open(path, "wb") as f:
        f.write(chosen_data)
    print("  written in place\n", flush=True)
    return dst_bytes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    threshold = THRESHOLD_MB * 1024 * 1024
    targets = []
    for root, _dirs, files in os.walk(ASSETS_DIR):
        for name in files:
            if name.lower().endswith((".jpg", ".jpeg")):
                p = os.path.join(root, name)
                if os.path.getsize(p) > threshold:
                    targets.append(p)

    targets.sort(key=os.path.getsize, reverse=True)
    if not targets:
        print(f"No JPEGs over {THRESHOLD_MB} MB found.")
        return

    total_src = 0
    total_dst = 0
    for p in targets:
        total_src += os.path.getsize(p)
        total_dst += compress(p, dry_run=args.dry_run)

    print(
        f"TOTAL: {mb(total_src):.2f} MB -> {mb(total_dst):.2f} MB "
        f"({100 * (1 - total_dst / total_src):.0f}% smaller)"
    )


if __name__ == "__main__":
    main()
