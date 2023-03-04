import os
import sys

from helper.imageCreator import createCircle, createBars
from helper.IterateVideo import IterateVid

def FileSetup():
    if len(sys.argv) != 3: 
        raise Exception("Missing Arguments")

    return sys.argv[1], sys.argv[2]

if __name__ == '__main__':
    filePath, name = FileSetup()
    colors, frame_count = IterateVid(filePath)
    createBars(colors, name)
    createCircle(colors, name)