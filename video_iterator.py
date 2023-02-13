import cv2
import os

# file setup
# file setup
if not os.path.exists("data"):
    os.makedirs('data')
# params
bars = 1000

video = cv2.VideoCapture("video/newjean.mp4")
# fps = video.get(cv2.CAP_PROP_FPS)
fps = 30
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps

print(fps)
print(frame_count)
print(duration)
print(float(duration/60))
print(duration/bars)
currentframe = 0
count = 0

while video.isOpened() and currentframe < 10:
    success, frame = video.read()

    cv2.imshow("Output", frame)
    cv2.imwrite('./data/frame{:d}.jpg'.format(count), frame)
    count += 30 # i.e. at 30 fps, this advances one second
    video.set(cv2.CAP_PROP_POS_FRAMES, count)
    currentframe +=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

