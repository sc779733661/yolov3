# 读取标签列表，分比例写入train,val的 .txt文件
import os
import random


trainval_percent = 0.1  # 验证集占比大小
train_percent = 0.9  # 训练集占比
xmlfilepath = 'data/Annotations'
txtsavepath = 'data/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)

tv = int(num * trainval_percent)  # 验证集大小
tr = int(tv * train_percent)  # 训练集大小
# 从list中随机获取这么多个元素，作为一个片断返回
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data/ImageSets/trainval.txt', 'w')
ftest = open('data/ImageSets/test.txt', 'w')
ftrain = open('data/ImageSets/train.txt', 'w')
fval = open('data/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'  # 取到倒数第4个字符
    if i in trainval:  # 0.1
        ftrainval.write(name)
        if i in train:  # 0.1*0.9
            ftest.write(name)
        else:  # 0.1*0.1
            fval.write(name)
    else:  # 0.9
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
