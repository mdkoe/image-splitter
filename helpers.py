special_chars = "\|&:;()<>~*@?!$#[]{}/'\" "

def convert_path(path):
    for char in special_chars:
        path=path.replace("%c"%(char),"\%c"%(char))
    return path
    
def show_help():
    print('usage: python3 main.py [--help] [--log] [--jpg]')
    print('[--quality=] filename.zip output_path')

def show_error(argv):
    print('ERROR: %s is not command. See python3 main.py --help'%(' '.join(argv)))

def show_error_quality():
    print('ERROR: value of --quality in [1,100]')
