train：
python train.py --data data/rbc.data --cfg cfg/yolov3-tiny.cfg --epochs 20 --weights weights/yolov3-tiny.weights

detect:
python detect.py --cfg cfg/yolov3-tiny.cfg --weights weights/best.pt