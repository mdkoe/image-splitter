import sys
import os
import subprocess
import zipfile
from helpers import *

def process(input_path,out_path,ext,quality,log):
    zip_file = zipfile.ZipFile(input_path,'r')
    for image_name in zip_file.namelist():
        path = os.path.join(out_path,image_name.encode('cp437').decode('cp932'))
        if image_name[-1] == '/':
            os.makedirs(os.path.dirname(path),exist_ok=True)
        else:
            with open(path,'wb') as file:
                file.write(zip_file.read(image_name))
            if log: print(path)
            slice(path,out_path,ext,quality)
            os.remove(path)
    zip_file.close()
    if log : print("Complete")
    sys.exit()

def slice(path,out_path,ext,quality):
    image_name,image_ext = os.path.splitext(path)
    quality_commad = ' '
    if ext == '.jpg':
        quality_commad = ' -quality %d '%(quality)
    # get size
    size = subprocess.check_output(["identify", "-format", "%w %h", path])
    size = list(map(int, size.decode('utf-8').split(" ")))

    # calculator size
    image_w, image_h = size
    splice_w = int(image_w/2)
    splice_h = int(image_h)

    #slice-left
    leftArea = (convert_path(str(path)), splice_w, splice_h, 0, 0, quality_commad, convert_path(image_name)+"b",ext)
    leftCmd = "convert %s -crop '%dx%d+%d+%d'%s%s%s"%leftArea
    os.system(leftCmd)

    #slice-right
    rightArea = (convert_path(str(path)), image_w - splice_w, image_h, splice_w, 0,quality_commad, convert_path(image_name)+"a",ext)
    rightCmd = "convert %s -crop '%dx%d+%d+%d'%s%s%s"%rightArea
    os.system(rightCmd)
    sys.exit()
