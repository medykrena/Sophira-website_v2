# Fonts Self-Hosted - Instructions

## Inter Font Files Needed

You need to download these 2 files and place them in this directory:

### 1. Inter Regular (400)
- **Filename:** `inter-400.woff2`
- **Download from:** https://fonts.google.com/specimen/Inter
- Click "Download family" → Extract → Find `Inter-Regular.ttf`
- Convert to WOFF2 using: https://cloudconvert.com/ttf-to-woff2
- Rename to `inter-400.woff2`

### 2. Inter SemiBold (600)
- **Filename:** `inter-600.woff2`
- **Download from:** https://fonts.google.com/specimen/Inter
- Click "Download family" → Extract → Find `Inter-SemiBold.ttf`
- Convert to WOFF2 using: https://cloudconvert.com/ttf-to-woff2
- Rename to `inter-600.woff2`

## Alternative: Use Google Fonts Helper

1. Go to: https://gwfh.mranftl.com/fonts/inter
2. Select charsets: latin, latin-ext
3. Select styles: regular (400), 600
4. Download the WOFF2 files
5. Place them in this folder

## Why WOFF2?

- Smallest file size (~30% smaller than TTF)
- Best browser support (all modern browsers)
- Optimal performance

## File Sizes (approximate)

- inter-400.woff2: ~50-70 KB
- inter-600.woff2: ~50-70 KB
- **Total: ~100-140 KB** (vs loading from Google CDN)

## CSS is already configured

The fonts are already referenced in `assets/css/main.css` with the correct paths.
Just add the files here and they'll work immediately!
