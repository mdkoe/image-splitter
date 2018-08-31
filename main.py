import sys
import getopt
from helpers import *
from splicer import process

def main(argv):
    # default value
    ext = '.jpg'
    quality = 85
    log = False
    out_path = ''

    # commad split
    try:
        opts, args = getopt.getopt(argv,'',['help','jpg','png','log','quality='])
    except getopt.GetoptError:
        show_error(argv)
        sys.exit()

    # commad process
    for opt,value in opts:
        if opt == '--help':
            show_help()
            sys.exit(1)
        if opt == '--log':
            log = True
        if opt == '--jpg':
            ext = '.jpg'
        if opt == '--png':
            ext = '.png'
        if opt == '--quality':
            quality = int(value)
            if quality<0 or quality>100:
                show_error_quality()
                sys.exit(2)
    if len(args) == 0 or len(args) > 2:
        show_error(argv)
        sys.exit()
    if len(args) == 2:
        out_path = args[1]
    input_path= args[0]
    
    process(input_path,out_path,ext,quality,log)
    show_help()

if __name__ == "__main__":
    main(sys.argv[1:])
