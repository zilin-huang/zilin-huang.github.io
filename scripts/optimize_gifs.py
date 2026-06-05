"""Convert large animated GIFs to animated WebP to shrink page weight.

Animated WebP keeps the same <img> usage (and medium-zoom) while typically
cutting 85-95% of the file size compared to GIF.

Usage:
    python scripts/optimize_gifs.py            # convert + report
    python scripts/optimize_gifs.py --dry-run  # only report what would happen

The original .gif files are left in place (and are tracked by git), so the
conversion is fully reversible.
"""

from __future__ import annotations

import argparse
import os
from PIL import Image, ImageSequence

# Longest side (px) the output is downscaled to. Teasers/thumbnails display
# small, so this keeps them crisp while removing wasted resolution.
MAX_SIDE = 800
# Lossy WebP quality for animation frames (0-100). 72 is visually clean.
QUALITY = 72
# Pillow WebP encoder effort (0-6). Higher = smaller but MUCH slower on many
# frames; 4 is a good speed/size balance for animations.
METHOD = 4

# GIFs to convert, relative to the repo root. Each entry may override the
# defaults above via: max_side, quality, stride (keep 1 of every `stride`
# frames, doubling durations to preserve playback speed for huge animations).
TARGETS = [
    {"path": "assets/teaser/2025_qian_agentthink.gif"},
    {"path": "assets/teaser/2025_sheng_safeplug.gif"},
    {"path": "assets/teaser/2025_sheng_Talk2Traffic.gif"},
    {"path": "assets/teaser/2025_sheng_curricuvlm.gif"},
    {"path": "assets/teaser/2024_huang_vlmrl.gif"},
    {"path": "assets/teaser/2025_huang_perlhf.gif"},
    {"path": "assets/teaser/2024_huang_haim_1.gif"},
    {"path": "assets/teaser/2024_sheng_traffic.gif"},
    {"path": "assets/teaser/2024_huang_cv2x.gif"},
    # Big, long news thumbnail shown small -> compress harder + drop frames.
    {
        "path": "assets/news_photo/news_thumbnails/2024/huang_haim.gif",
        "max_side": 640,
        "quality": 58,
        "stride": 2,
    },
    {"path": "assets/news_photo/news_thumbnails/2024/huang_perlhf.gif"},
    {"path": "assets/news_photo/news_thumbnails/2024/sheng_traffic.gif"},
]


def mb(num_bytes: int) -> float:
    return num_bytes / (1024 * 1024)


def convert(target: dict, dry_run: bool = False) -> None:
    gif_path = target["path"]
    max_side = target.get("max_side", MAX_SIDE)
    quality = target.get("quality", QUALITY)
    stride = target.get("stride", 1)

    webp_path = os.path.splitext(gif_path)[0] + ".webp"
    src_bytes = os.path.getsize(gif_path)

    im = Image.open(gif_path)
    loop = im.info.get("loop", 0)

    frames = []
    durations = []
    for frame in ImageSequence.Iterator(im):
        # Seeking composites partial frames, so .convert yields a full frame.
        rgba = frame.convert("RGBA")
        durations.append(frame.info.get("duration", 100))
        frames.append(rgba)

    if stride > 1:
        frames = frames[::stride]
        # Preserve playback speed: each kept frame absorbs the dropped ones.
        durations = [
            sum(durations[i : i + stride]) for i in range(0, len(durations), stride)
        ]

    w, h = frames[0].size
    scale = min(1.0, max_side / max(w, h))
    new_size = (max(1, round(w * scale)), max(1, round(h * scale)))
    if scale < 1.0:
        frames = [f.resize(new_size, Image.LANCZOS) for f in frames]

    print(
        f"{gif_path}\n"
        f"  frames={len(frames)} size={w}x{h} -> {new_size[0]}x{new_size[1]} "
        f"loop={loop} q={quality}",
        flush=True,
    )

    if dry_run:
        print(f"  [dry-run] would write {webp_path}\n", flush=True)
        return

    frames[0].save(
        webp_path,
        format="WEBP",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=loop,
        method=METHOD,
        quality=quality,
        minimize_size=True,
    )
    dst_bytes = os.path.getsize(webp_path)

    # If WebP isn't actually smaller (happens for low-color GIFs), keep the GIF.
    if dst_bytes >= src_bytes * 0.9:
        os.remove(webp_path)
        print(
            f"  {mb(src_bytes):.2f} MB -> {mb(dst_bytes):.2f} MB "
            f"(not worthwhile, keeping GIF)\n",
            flush=True,
        )
        return

    print(
        f"  {mb(src_bytes):.2f} MB -> {mb(dst_bytes):.2f} MB "
        f"({100 * (1 - dst_bytes / src_bytes):.0f}% smaller)  -> {webp_path}\n",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    total_src = 0
    total_dst = 0
    for target in TARGETS:
        rel = target["path"]
        if not os.path.exists(rel):
            print(f"!! missing: {rel}")
            continue
        src = os.path.getsize(rel)
        convert(target, dry_run=args.dry_run)
        webp = os.path.splitext(rel)[0] + ".webp"
        # Count the file that will actually be served (webp if kept, else gif).
        total_src += src
        total_dst += os.path.getsize(webp) if os.path.exists(webp) else src

    if not args.dry_run:
        print(
            f"TOTAL (served): {mb(total_src):.2f} MB -> {mb(total_dst):.2f} MB "
            f"({100 * (1 - total_dst / total_src):.0f}% smaller)"
        )


if __name__ == "__main__":
    main()
