special_chars = "\|&:;()<>~*@?!$#[]{}/'\" "

def convert_path(path):
    for char in special_chars:
        path=path.replace("%c"%(char),"\%c"%(char))
    return path
