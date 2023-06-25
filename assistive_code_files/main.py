import cv2 as cv
import numpy as np
from sys import argv
import time

if __name__ == "__main__":
    CONFIDENCE = 0.45
    NMS_THRESHOLD = 0.5
    # IOU_THRESHOLD = 0.5
    weights_path = r"D:\Pycharm_Projects\GIT_diplom\diplom\backups\weights\bolt_1070_x_nut_899_best\nut_x_bolt_3000.weights"    labels_path = r"D:\Pycharm_Projects\GIT_diplom\diplom\imgs\bolt_1070_x_nut_899_best\classes.names"
    config_path = r"D:\Pycharm_Projects\GIT_diplom\diplom\backups\cfgs\nut_x_bolt.cfg"
    font_scale = 1
    thickness = 1

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