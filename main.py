import sys
import getopt
import zipfile
import os
import subprocess
from pathlib import Path
from helpers import convert_path

def slice(path):
    imageName = os.path.splitext(path)[0]

    #get size
    size = subprocess.check_output(["identify", "-format", "%w %h", path])
    size = list(map(int, size.decode('utf-8').split(" ")))

    # calculator size
    image_w, image_h = size
    splice_w = int(image_w/2)
    splice_h = int(image_h)

    #slice-left
    leftArea = (convert_path(str(path)), splice_w, splice_h, 0, 0, convert_path(imageName)+"b.jpg")
    leftCmd = "convert %s -crop '%dx%d+%d+%d' %s"%leftArea
    os.system(leftCmd)

    #slice-right
    rightArea = (convert_path(str(path)), image_w - splice_w, image_h, splice_w, 0, convert_path(imageName)+"a.jpg")
    rightCmd = "convert %s -crop '%dx%d+%d+%d' %s"%rightArea
    os.system(rightCmd)

if __name__ == "__main__":
    filename = sys.argv[1]

    zipFile = zipfile.ZipFile(filename,'r')
    for imageName in zipFile.namelist():
        path = Path(imageName.encode('cp437').decode('cp932'))
        if imageName[-1] == '/': #folder
            if not path.exists():
                path.mkdir()
        else:
            with path.open('wb') as folder:
                folder.write(zipFile.read(imageName))
            print(path)
            slice(path)
            os.remove(path)
    zipFile.close()
    print("Complete")
