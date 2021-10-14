import sys
import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
class Net3():
    def __init__(self):
        self.cur_dir = os.getcwd().replace('\\','/')
        self.data_dir = os.path.join(self.cur_dir, 'images/numberandalphbets')
        self.net3V = os.path.join(self.cur_dir, 'Txtnetdata/net3V.txt')
        self.net3W = os.path.join(self.cur_dir, 'Txtnetdata/net3W.txt')
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.alphbets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']
        self.dataset = self.numbers + self.alphbets
        self.label = self.numbers + self.alphbets
        self.dataset_len = len(self.dataset)
        self.V = np.loadtxt(self.net3V)
        self.W = np.loadtxt(self.net3W)
    # 激活函数
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    def predict(self,x):
        # 计算隐藏层的输出
        L1 = self.sigmoid(np.dot(x,self.V))
        # 计算输出的输出
        L2 = self.sigmoid(np.dot(L1,self.W))
        return L2
    def dataidentify(self,img):
        #定义图片宽度
        width = 20
        #定义图片长度
        high = 20
        index = (img == 255)
        img[index] = 1
        image = cv.resize(img,(width,high))
        # gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
        #image = cv.threshold(img,0,1,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        X = np.empty((1,400))
        X = np.array(image).reshape((1,400))
        output = self.predict(X)
        pre = np.argmax(output)
        return self.label[pre]