
def mkdir_p( path ):
    '''
    mkdir -p functional equivalent
    '''
    import errno
    import os
    try:
        os.makedirs( path )
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir( path ):
            pass
        else:
            raise
