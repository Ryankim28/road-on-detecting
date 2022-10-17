import pandas
import torch
import sys
import cv2 as cv
import numpy as np
import time
import base64
import requests

# Constants.
INPUT_WIDTH = 640
INPUT_HEIGHT = 640
SCORE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.45
CONFIDENCE_THRESHOLD = 0.45

# Text parameters.
FONT_FACE = cv.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1
THICKNESS = 1

# Colors.
BLACK  = (0,0,0)
BLUE   = (255,178,50)
YELLOW = (0,255,255)
#model = torch.hub.load('.', 'custom', path='/path/to/yolov5/runs/train/exp5/weights/best.pt', source='local')
model = torch.hub.load('ultralytics/yolov5','yolov5s',pretrained=True)
#model costom

model.conf = 0.8  # NMS confidence threshold
"""model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.classes = None  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
model.max_det = 1000  # maximum number of detections per image
model.amp = False  # Automatic Mixed Precision (AMP) inference
"""
def draw_label(im, label, x, y):
    """Draw text onto image at location."""
    # Get text size.
    text_size = cv.getTextSize(label, FONT_FACE, FONT_SCALE, THICKNESS)
    dim, baseline = text_size[0], text_size[1]
    # Use text size to create a BLACK rectangle.
    cv.rectangle(im, (x,y), (x + dim[0], y + dim[1] + baseline), (0,0,0), cv.FILLED);
    # Display text inside the rectangle.
    cv.putText(im, label, (x, y + dim[1]), FONT_FACE, FONT_SCALE, YELLOW, THICKNESS, cv.LINE_AA)
#웹캠 신호 받기
wc = cv.VideoCapture(0)
while True:
    x1, x2, y1, y2 = 0,0,0,0
    start = time.time()
    ret, frame = wc.read()
    h,w,c = frame.shape
    results = model(frame)
    result = results.pandas().xyxy[0]
    cl = result['class'].to_list()
    if 0 in cl:
        print("사람 검출")
        con = result['confidence']
        cs = result['class']
        x1 = int(result['xmin'])
        y1 = int(result['ymin'])
        x2 = int(result['xmax'])
        y2 = int(result['ymax'])
    else:
        print("검출 안됨")
    if ret:
        cv.rectangle(frame, (x1, y2), (x2, y1), BLUE, 2)
        cv.imshow('image',frame)
        if cv.waitKey(1) == ord('q'):
            break
        end = time.time()
        print(1/(end-start), "fps")


# Image
# img = 'C:/Users/rlawl/PycharmProjects/YOLO/yolov5/data/images/bus.jpg'
# Inference


# Results, change the flowing to: results.show()
# results.save()  # or .show(), .save(), .crop(), .pandas(), etc
# results.print()
print(results.pandas().xyxy[0])
# results.show()
# if 0 in cl:
#     print("사람 검출")
# else:
#     print("검출 안됨")