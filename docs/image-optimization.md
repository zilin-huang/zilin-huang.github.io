# Image optimization policy

This website keeps original media locally and publishes optimized derivatives.

## Originals

- Preserve every source image before replacing a web-facing file.
- Store general source backups under `assets/image-originals/`, mirroring their paths below `assets/`.
- Event-specific source folders may use a descriptive `*-originals` suffix.
- Original folders must remain excluded from both Git and Jekyll output.

## Web images

- Do not upscale a small source merely to reach a file-size target.
- For large gallery and news photos, favor high visual quality and normally keep the main web derivative around 2–4 MB.
- For new galleries, prefer a high-quality WebP main image plus a 1600-pixel responsive derivative. Keep `srcset` width descriptors equal to the files' actual widths and retain lazy loading.
- Existing large JPEG photos may keep their URLs and formats when a high-quality recompression avoids broad reference churn.
- News thumbnails should normally be no larger than 1200 pixels on the longest edge and do not need to reach the gallery-image size range.
- Leave already-small, clear images unchanged.
- Do not apply the photo target blindly to logos, icons, diagrams, screenshots, or transparent UI assets.

## Motion media

- Do not process MP4, GIF, or animated WebP files as static images.
