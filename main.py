import sys
import getopt
import zipfile
from pathlib import Path
import os
from math import sqrt, ceil, floor

from PIL import Image

def slice(filename):
    image = Image.open(filename)

    image_w, image_h = image.size
    splice_h = int(image_w/2)
    splice_h = image_h

    leftArea = (0, 0, splice_w, splice_h)
    rightArea = (image_w - splice_h, 0, image_w, image_h)

    leftImage = image.crop    )
    # columns, rows = calc_columns_rows(number_tiles)
    # extras = (columns * rows) - number_tiles
    # tile_w, tile_h = int(floor(im_w / columns)), int(floor(im_h / rows))
    #
    # tiles = []
    # number = 1
    # for pos_y in range(0, im_h - rows, tile_h): # -rows for rounding error.
    #     for pos_x in range(0, im_w - columns, tile_w): # as above.
    #         area = (pos_x, pos_y, pos_x + tile_w, pos_y + tile_h)
    #         image = im.crop(area)
    #         position = (int(floor(pos_x / tile_w)) + 1,
    #                     int(floor(pos_y / tile_h)) + 1)
    #         coords = (pos_x, pos_y)
    #         tile = Tile(image, number, position, coords)
    #         tiles.append(tile)
    #         number += 1
    # if save:
    #     save_tiles(tiles,
    #                prefix=get_basename(filename),
    #                directory=os.path.dirname(filename))
    # return tuple(tiles)


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
