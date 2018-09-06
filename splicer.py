import sys
import os
import subprocess
import zipfile
from helpers import *
from time import sleep

def process(input_path,out_path,ext,quality,log):
    zip_file = zipfile.ZipFile(input_path,'r')
    for image_name in zip_file.namelist():
        path = os.path.join(out_path,image_name.encode('cp437').decode('cp932',"ignore"))
        if image_name[-1] == '/':
            os.makedirs(os.path.dirname(path),exist_ok=True)
        else:
            with open(path,'wb') as file:
                file.write(zip_file.read(image_name))
            if log: print("%s"%path)
            slice(path,out_path,ext,quality)
            os.remove(path)
    zip_file.close()

    sys.exit()

def slice(path,out_path,ext,quality):
    print(path)
    image_name,image_ext = os.path.splitext(path)
    quality_commad = ' '
    if ext == '.jpg':
        quality_commad = ' -quality %d '%(quality)
    # get size
    size = subprocess.check_output(["identify", "-format", "%w %h", path])
    size = list(map(int, size.decode('utf-8').split(" ")))
    image_w, image_h = size

    # refactor image
    temp_image_path = convert_path(image_name +"temp"+ ext)
    image_aspect = image_h/image_w

    if image_aspect < get_viewer_aspect():
        # increase height
        new_h = round(image_w*get_viewer_aspect()+0.5)
        create_cmd = "convert -size %dx%d xc:white %s"%(image_w,new_h,temp_image_path)
        os.system(create_cmd)

        increase_h = new_h - image_h
        refactor=(temp_image_path,convert_path(str(path)),0,int(increase_h/2),convert_path(str(path)))
        refactor_cmd = "convert %s %s -geometry +%d+%d -composite %s"%refactor
        os.system(refactor_cmd)

        os.remove(image_name +"temp"+ ext)
        image_h = new_h

    if image_aspect > get_viewer_aspect():
        # increase width
        new_w = round( image_h/get_viewer_aspect() + 0.5)
        create_cmd = "convert -size %dx%d xc:white %s"%(new_w,image_h,temp_image_path)
        os.system(create_cmd)

        increase_w = new_w - image_w
        refactor=(temp_image_path,convert_path(str(path)),int(increase_w/2),0,convert_path(str(path)))
        refactor_cmd = "convert %s %s -geometry +%d+%d -composite %s"%refactor
        os.system(refactor_cmd)
        os.remove(image_name +"temp"+ ext)
        image_w = new_w

    # calculator size
    splice_w = int(image_w/2)
    splice_h = int(image_h)
    #slice-left
    image_left_name = image_name + "b" + ext
    leftArea = (convert_path(str(path)), splice_w, splice_h, 0, 0, quality_commad, convert_path(image_left_name))
    leftCmd = "convert %s -crop %dx%d+%d+%d%s%s"%leftArea
    os.system(leftCmd)
    #slice-right
    image_right_name = image_name + "a" + ext
    rightArea = (convert_path(str(path)), image_w - splice_w, image_h, splice_w, 0,quality_commad, convert_path(image_right_name))
    rightCmd = "convert %s -crop %dx%d+%d+%d%s%s"%rightArea
    os.system(rightCmd)
