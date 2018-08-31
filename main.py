import sys
import getopt
import zipfile
import os
from pathlib import Path
from math import sqrt, ceil, floor
from PIL import Image


def slice(path):
    imageName = os.path.splitext(path)[0]
    image = Image.open(path)
    print(image.size)

    image_w, image_h = image.size
    splice_w = int(image_w/2)
    splice_h = image_h

    leftArea = (0, 0, splice_w, splice_h)
    leftImage = image.crop(leftArea)
    leftImage.save(imageName+"b.jpg")

    rightArea = (image_w - splice_w - 1 , 0, image_w, image_h)
    rightImage = image.crop(rightArea)
    rightImage.save(imageName+"a.jpg")

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
            slice(path)
            os.remove(path)
    zipFile.close()
    print("Complete")
