#!/usr/bin/env python3
import os
from cairosvg import svg2png

def main( args ):
    print( 'Hello', args )
    svg2png( url = args.path, write_to=args.path.replace('.svg', '.png' ), output_width = 24, output_height = 24 )

# Temporary to test view
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser( description='Generate markdown or html tags for all svgs found' )

    parser.add_argument( 'path',   help = 'SVG file path' )
    parser.add_argument( 'size',   help = 'Width and Height' )
    parser.add_argument( '-v', '--verbose', action="store_true",
                         help="Increase the verbosity." )
    args = parser.parse_args()
    main(args)
