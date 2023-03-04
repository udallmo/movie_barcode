import datetime
import time
import cv2

from helper.dominateColors import GetDominateColor
from helper.progressBar import progressBar

def IterateVid():
    # TODO: CMD arguments
    vid = cv2.VideoCapture("video/newjean.mp4")

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

        # i.e. at 30 fps, this advances one second
        current_frame += fps 
        vid.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        progressBar(current_frame, frame_count)
        colors.append(GetDominateColor(frame, int(height), int(width)))
    print(f"\nProcess Finished in: {(time.time() - start_time):.2f}s")
    return colors