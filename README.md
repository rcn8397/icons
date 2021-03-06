# Icons
SVG icons
# Creation
Inkscape
https://inkscape.org/

# Utils
## Convert SVGs to PNGs

Give the util a path to the SVGs and a size in pixels. The size is width by height

```bash
    python3 ./utils/svg2png.py collections/basics 64
```

### Conversion
The conversion script uses CairoSVG to convert the input sources.

*  [Site](https://cairosvg.org/)
*  [Code](https://github.com/Kozea/CairoSVG/blob/master/cairosvg/__init__.py#L53)
    
# Previews
Icon sources

*  [icons.md](icons.md)

## Generating thumbnails
To generate icons.md run the icons2markdown.py in the utils folder.

    python ./utils/icons2markdown.py . > icons.md
    