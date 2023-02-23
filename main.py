import cv2
import os
import datetime
import numpy as np
import time

from progress_bar import progress_bar

def FileSetup():
    # file setup
    if not os.path.exists("data"):
        os.makedirs('data')

def IterateVid():
    vid = cv2.VideoCapture("video/newjean.mp4")
    # vid = cv2.VideoCapture("D:\Videos\John Wick Chapter 1, 2, 3 - Trilogy 2014-2019 Eng Subs 720p [H264-mp4]\John Wick Chapter - 1-2-3\John_Wick_Chapter_1.mp4")

    # VIDEO DATA
    fps = vid.get(cv2.CAP_PROP_FPS)
    frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    seconds = round(frame_count / fps)
    video_time = datetime.timedelta(seconds=seconds)

    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    print("FPS: ", fps)
    print("FRAME COUNT: ", frame_count)
    print("SECONDS: ", seconds)
    print("DURATION: ", video_time)
    print("DIMENSIONS: ", height, width)

    # iterator
    current_frame = 0
    colors = []
    start_time = time.time()
    while vid.isOpened() and current_frame < frame_count:
        success, frame = vid.read()

        # cv2.imshow("Output", frame)
        # cv2.imwrite('./data/frame{:d}.jpg'.format(current_frame), frame)
        current_frame += fps # i.e. at 30 fps, this advances one second
        vid.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        progress_bar(current_frame, frame_count)
        colors.append(GetDominateColor(frame, int(height), int(width), current_frame))
    print(f"\nProcess Finished in: {(time.time() - start_time):.2f}s")
    return colors

def create_bar(height, width, color):
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)

def GetDominateColor(frame, height, width, current_frame):
    # print(frame)
    data = np.reshape(frame, (height * width, 3))
    data = np.float32(data)

    number_clusters = 1
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)
    # print(centers)
    font = cv2.FONT_HERSHEY_SIMPLEX
    rgb_values = []
    bars = []
    for index, row in enumerate(centers):
        bar, _notUsed = create_bar(200, 200, row)
        rgb_values.append((int(row[2]), int(row[1]), int(row[0])))
        bars.append(bar)
    
    # img_bar = np.hstack(bars)

    # for index, row in enumerate(rgb_values):
    #     image = cv2.putText(img_bar, f'{index + 1}. RGB: {row}', (5 + 200 * index, 200 - 10),
    #                     font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    #     print(f'{index + 1}. RGB{row}')

    # cv2.imwrite('output/bar.jpg', img_bar)
    # cv2.imwrite('./data/frame{:d}.jpg'.format(current_frame), img_bar)

    return rgb_values[0]


def CreateImage(colors):
    # print(colors)
    h, w = 720, 5
    bars = []
    for rgb in colors:
        bar = np.zeros((h, w, 3), np.uint8)
        bar[:] = rgb
        bars.append(bar)
    img_bar = np.hstack(bars)
    print(bar[:5])
    print(img_bar)
    # cv2.imwrite('output/bar.jpg', img_bar)

if __name__ == '__main__':
    FileSetup()
    colors = IterateVid()
    CreateImage(colors)