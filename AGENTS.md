# Project working instructions

## Image thumbnails

- Before creating, replacing, or optimizing website images, read and follow `docs/image-optimization.md`.
- Generate every thumbnail directly from the preserved original with gentle ImageMagick `Mitchell` resampling.
- Do not apply `-sharpen`, `-unsharp`, or any equivalent extra sharpening to thumbnails.
- Avoid making the browser downscale a multi-megapixel source into a small card. Generate a correctly sized derivative (normally 2× the rendered CSS dimensions) and declare accurate `srcset` and `sizes` values when responsive candidates are used.
- Never upscale a source, and verify the output's actual pixel dimensions after generation.
