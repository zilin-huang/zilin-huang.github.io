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

## Fixed-size thumbnails

- Never rely on the browser to shrink a multi-megapixel original directly into a small fixed-height card or gallery thumbnail.
- For an image displayed at roughly 200–450 CSS pixels, provide dedicated 900- and 1600-pixel WebP candidates through `srcset` and an accurate `sizes` attribute; keep the original only as the fallback `src` when useful.
- Generate thumbnail derivatives with a gentle downsampling filter (currently ImageMagick `Mitchell`) and do not apply an additional unsharp mask. Browser downscaling of a very large source and repeated sharpening can produce brittle edges, visible noise, or an over-sharpened appearance.
- Use a `-thumb-900.webp` / `-thumb-1600.webp` suffix for thumbnail-only derivatives. Width descriptors must match the files' actual pixel widths.
- Before adding a new fixed-size gallery image, check its source dimensions and file size. Images wider than about 2400 pixels or larger than about 1 MB should normally receive thumbnail derivatives.

### Remembered thumbnail recipe

- Always generate each derivative directly from the preserved original. Do not resize an already-resized thumbnail a second time.
- Use ImageMagick's `-filter Mitchell` immediately before `-resize`. Do not add `-sharpen`, `-unsharp`, or an equivalent sharpening operation anywhere in the thumbnail pipeline.
- Crop only when the component requires a fixed aspect ratio. For a news-list cover displayed at `280 × 180` CSS pixels, generate a `560 × 360` WebP (2× density) from the original with Mitchell resampling instead of sending a large gallery image to the browser.
- For responsive gallery thumbnails, generate the 900- and 1600-pixel candidates independently from the original, then declare their true widths in `srcset` and describe the rendered width accurately in `sizes`.
- Never upscale a source. If the original is smaller than a planned candidate, omit that candidate and use the best available native-size derivative.
- After generation, verify pixel dimensions and inspect the page at its real rendered size. Apparent harshness should first be investigated as excessive browser downscaling, repeated resizing, or source noise—not corrected by adding sharpening.

Reference command pattern (the crop geometry is component-specific):

```sh
magick ORIGINAL -auto-orient -filter Mitchell -resize '560x360^' \
  -gravity center -extent 560x360 -quality 88 THUMBNAIL.webp
```

## Motion media

- Do not process MP4, GIF, or animated WebP files as static images.
