#!/usr/bin/env python3
from filewalker import FileWalker
from cairosvg   import svg2png
from shell      import mkdir_p
import os

def main( args ):
    verbose = not args.silent
    if verbose:
        print( args )
        print( 'Exporting icons...' )
        print( '\t{0} {1}x{1} -> {2}'.format( args.path, args.size, args.out ) )
    convert2svg( args.path, args.size, args.out, verbose = verbose )

def convert2svg( path, size, out_path = './export', verbose = True ):
    '''
    '''
    out = os.path.join( out_path, '{0}x{0}'.format( size ) )
    mkdir_p( out )
    fw = FileWalker( path )
    svgs = fw.find( ['.svg'] )
    for svg in svgs:
        if verbose: print( 'Exporting {0}'.format( svg ) )
        bname = os.path.basename( svg )
        svg_out = os.path.join( out, bname.replace('.svg', '.png' ) )
        svg2png( url = svg,
                 write_to      = svg_out,
                 output_width  = float( size ),
                 output_height = float( size ) )

# Temporary to test view
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser( description='Generate markdown or html tags for all svgs found' )

    parser.add_argument( 'path',   help = 'SVG file path' )
    parser.add_argument( 'size',   help = 'Width and Height', type=int )
    parser.add_argument( '-o',
                         '--out',
                         default = './export',
                         help = 'Width and Height' )
    parser.add_argument( '-s', '--silent', action="store_true",
                         help="Decrease the verbosity." )
    args = parser.parse_args()
    main(args)
