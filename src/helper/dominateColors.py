import cv2
import numpy as np

number_clusters = 1
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

def GetDominateColor(frame, height, width):
    data = np.reshape(frame, (height * width, 3))
    data = np.float32(data)

    _compactness, _labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)
    rgb_values = []
    bars = []
    for _index, row in enumerate(centers):
        bar, _notUsed = create_bar(200, 200, row)
        rgb_values.append((int(row[2]), int(row[1]), int(row[0])))
        bars.append(bar)
    
    return rgb_values[0]

def create_bar(height, width, color):
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)