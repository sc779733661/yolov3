
import xml.etree.ElementTree as ET  # 用于打开xml
import pickle
import os
from os import listdir, getcwd
from os.path import join


sets = ['train', 'test', 'val']  # 分为3个文件
classes = ["RBC"]  # magic
fxml = 'data/Annotations/'  # xml 的labels路径
flabels = 'data/labels/'  # 写入labels路径
wd = getcwd()  # 当前路径
print(wd)

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open(fxml + '%s.xml' % (image_id))
    # 输出路经
    out_file = open(flabels + '%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        # 在out_file中写入位置信息
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


for image_set in sets:
    if not os.path.exists(flabels):
        os.makedirs(flabels)
    # 读取所有这个txt文件中的内容，去除字符‘空格’，以空格为分隔符，包括\n
    image_ids = open('data/ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('data/%s.txt' % (image_set), 'w')
    for image_id in image_ids:  # 遍历这个文件下所有图片名
        # list_file.write('data/images/%s.jpg\n' % (image_id))  # 写入
        convert_annotation(image_id)
    list_file.close()
