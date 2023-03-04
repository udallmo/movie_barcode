import os

from helper.imageCreator import createCircle, createBars
from helper.IterateVideo import IterateVid

def FileSetup():
    # file setup
    if not os.path.exists("data"):
        os.makedirs('data')

if __name__ == '__main__':
    FileSetup()
    colors = IterateVid()
    createBars(colors)
    createCircle(colors)