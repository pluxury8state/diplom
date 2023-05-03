import cv2 as cv
import numpy as np
from sys import argv
import time


CONFIDENCE = 0.5
NMS_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5
weights_path = r"C:\Users\Admin\PycharmProjects\Make_model_with_YOLO\backups\weights\416_416\bolt\1723_10_percent\bolt_2000.weights"
labels_path = r"C:\Users\Admin\PycharmProjects\Make_model_with_YOLO\backups\names\classes.names"
config_path = r"C:\Users\Admin\PycharmProjects\Make_model_with_YOLO\backups\cfgs\bolt_test.cfg"
font_scale = 1
thickness = 1

args_from_c = argv
print(type(args_from_c), args_from_c)
if args_from_c[1:]:
    weights_path, labels_path, config_path = args_from_c[1:]

print(weights_path, labels_path, config_path)

COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class_name = []
with open(labels_path,'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]
print(class_name)

net = cv.dnn.readNet(config_path, weights_path)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)


cap = cv.VideoCapture(1)
starting_time = time.time()
frame_counter = 0
while True:
    ret, frame = cap.read()
    frame_counter += 1
    if ret == False:
        break
    classes, scores, boxes = model.detect(frame, CONFIDENCE, NMS_THRESHOLD)
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_name[classid], score)
        cv.rectangle(frame, box, color,     2)
        cv.putText(frame, label, (box[0], box[1]-10),
                   cv.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
    endingTime = time.time() - starting_time
    fps = frame_counter/endingTime
    # print(fps)
    cv.putText(frame, f'FPS: {fps}', (20, 50),
               cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv.destroyAllWindows()