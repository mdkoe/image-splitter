import sys
import getopt
import zipfile
from pathlib import Path
import os
import image_slicer

if __name__ == "__main__":
    filename = sys.argv[1]

    zipFile = zipfile.ZipFile(filename,'r')
    for imageName in zipFile.namelist():
        path = Path(imageName.encode('cp437').decode('cp932'))
        if imageName[-1] == '/': #folder
            if not path.exists():
                path.mkdir()
        else:
            print(path)
            with path.open('wb') as folder:
                folder.write(zipFile.read(imageName))
            image_slicer.slice(path,2)
            os.remove(path)
    zipFile.close()
    print("Complete")
