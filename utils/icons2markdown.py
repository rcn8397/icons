#!/usr/bin/env python3
from filewalker import FileWalker
import os

md_template  = '![Alt text]({0}?sanitize=true)'
tag_template = '<img src="{0}?sanitize=true">'

def main( args ):
    fw = FileWalker( args.path )
    svgs = fw.find( ['.svg'] )
    for svg in svgs:
        if args.html:
            template = tag_template
        else:
            template = md_template
        if svg[0] == '.':
            svg = svg[1:]
        path = args.repo + svg
        print( template.format( path ) )

# Temporary to test view
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser( description='Generate markdown or html tags for all svgs found' )

    parser.add_argument( 'path', help = 'Path to search' )
    parser.add_argument( '-v', '--verbose', action="store_true",
                         help="Increase the verbosity." )
    parser.add_argument( '-x', '--html', action="store_true",
                         help="Create HTML tags instead" )
    parser.add_argument( '-r', '--repo', help='Repo to prepend',
                         default='https://github.com/rcn8397/icons' )
    args = parser.parse_args()
    main(args)
