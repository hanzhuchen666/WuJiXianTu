# -*- coding: utf-8 -*-
import time
import os
import cv2
import matplotlib as plt
import numpy as np
import uiautomator2 as ui2
import subprocess


def classify_gray_hist(image1, image2, size=(900, 1600)):
    # 先计算直方图
    # 几个参数必须用方括号括起来
    # 这里直接用灰度图计算直方图，所以是使用第一个通道，
    # 也可以进行通道分离后，得到多个通道的直方图
    # bins 取为16
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 可以比较下直方图
    # plt.plot(range(256), hist1, 'r')
    # plt.plot(range(256), hist2, 'b')
    # plt.show()
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


# 通过得到RGB每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2, size=(900, 1600)):
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data


# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


class Page:
    def __init__(self, id):
        self.screenshot = d.screenshot(format='opencv')
        self.id = id

    def detect(self):
        # 首先截图，保存截图图片，
        # 读取层级结构
        # 对于每个按钮元素，声明新的按钮类，分配id
        pass

    def newPage(self):
        list = np.array([(-1, 0, 0)], dtype=ICON)
        return list

    def read(self):
        pass
        # 以数组的形式返回，并且调用icon的同名函数

    def judgeImage(self, image, structure):
        length = len(structure)
        threshold = 0.85
        for i in range(length):
            testimg = cv2.imread(PATH + "\\GameData\\page{}.jpg".format(i))
            degree = classify_gray_hist(testimg, image)
            print("the similarity of current id {} between page id {}: {}".format(self.id, i, degree))
            if degree < threshold:
                pass
            else:
                print("the page id should be changed from {} to {}".format(self.id, i))
                return i
        return length

    def saveScreen(self):
        cv2.imwrite(PATH + "\\GameData\\page{}.jpg".format(self.id), self.screenshot)

    def screenshot_test(self):
        # take screenshot and save to a file on the computer, require Android>=4.2.
        d.screenshot(PATH + "\\GameData\\home1.jpg")

        # get PIL.Image formatted images. Naturally, you need pillow installed first
        image = d.screenshot()  # default format="pillow"
        image.save(PATH + "\\GameData\\home2.jpg")  # or home.png. Currently, only png and jpg are supported
        print(image)
        input("the data of PIL.Image")

        # get opencv formatted images. Naturally, you need numpy and cv2 installed first
        image = d.screenshot(format='opencv')
        cv2.imwrite(PATH + "\\GameData\\home3.jpg", image)
        print(image)
        input("the data of opencv formatted images")

        # get raw jpeg data
        imagebin = d.screenshot(format='raw')
        open(PATH + "\\GameData\\home4.jpg", "wb").write(imagebin)
        print(imagebin)


class Icon:
    def __init__(self, location, father=-1):
        self.location = location
        self.name = ""
        self.to = 0
        self.father = father

    def __int__(self, to, location):
        self.location = location
        self.name = ""
        self.to = to

    def checkIcon(self):
        for icons in game.structure[self.father]:
            if (icons[0] == self.to) and (icons[1] + 5 > self.location[0]) and (icons[1] - 5 < self.location[0]) and (
                    icons[2] + 5 > self.location[1]) and (icons[2] - 5 < self.location[1]):
                return False
        return True

    def assignId(self):
        # 截图保存按钮的图片
        #
        pass

    def save(self):
        # 保存图片
        pass

    def read(self):
        # 以数组的形式返回
        pass

    def newIcon(self):
        container = np.array([(self.to, self.location[0], self.location[1])], dtype=ICON)
        return container


class MessageBox:

    def __init__(self, father):
        self.label = ""
        self.number = 0
        self.fatherpage = father
        self.locationbox = [0, 0, 0, 0]

    def enterlabel(self):
        pass

    def readlabel(self):
        pass

    def readnumber(self):
        pass

    def enternumber(self):
        pass

    def newMessageBox(self):
        pass


class Property:
    def __init__(self):
        self.propertypool = {}
        self.timepool = {}

    def execute(self):
        pass

    def bfs(self):
        pass


class Game:
    SLEEP = 7

    def __init__(self):
        self.structure = []
        ## structure = list;

    def listen_click(self):
        self.listen = subprocess.Popen("adb shell getevent -l", stdin = subprocess.PIPE,stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

        while True:
            print("...")

            text = self.listen.stdout.readline()
            print(text)

    def login(self):
        # 启动应用
        d.xpath('//*[@text="无极仙途"]').click()
        time.sleep(self.SLEEP)
        d.click(441, 1440)
        time.sleep(self.SLEEP)
        d.click(766, 398)

    def learn(self):
        self.structure = self.getStructure()
        pageid = len(self.structure)
        page = Page(pageid)
        checkpage = page.judgeImage(page.screenshot, self.structure)
        if checkpage == page.id:
            self.structure.append(page.newPage())
            print(self.structure)
            page.saveScreen()
        else:
            page.id = checkpage

        while True:
            check = input("continue to learn?")
            if check == 'q':
                break
            x = eval(input("please input the x location of the point"))
            y = eval(input("please input the y position of the point"))
            prev_page_id = page.id
            icon = Icon([x, y], father=prev_page_id)

            d.click(x, y)
            time.sleep(self.SLEEP)
            pageid = len(self.structure)
            page = Page(pageid)
            checkpage = page.judgeImage(page.screenshot, self.structure)
            if checkpage == page.id:
                self.structure.append(page.newPage())
                print(self.structure)
                page.saveScreen()
            else:
                page.id = checkpage

            icon.to = page.id
            if self.structure[prev_page_id][0][0] == -1:
                self.structure[prev_page_id][0] = icon.newIcon()
            elif icon.checkIcon():
                if icon.father == icon.to:
                    pass
                else:
                    self.structure[prev_page_id] = np.append(self.structure[prev_page_id], icon.newIcon())
            else:
                pass

        self.saveStructure()

    def play(self):
        pass

    def getStructure(self):
        self.structure = []
        i = 0
        while True:

            try:
                file = np.load(PATH + "\\GameData\\page{}.npy".format(i))
                print("\n the data of page {}:".format(i))
                print(file)
                self.structure.append(file)
                i = i + 1

            except:
                print("the structure npy load stopped at page {}!!!".format(i))
                break

        return self.structure

    def saveStructure(self):
        i = 0
        for page in self.structure:
            np.save(PATH + "\\GameData\\page{}.npy".format(i), page)
            i = i + 1


class checkbox(Page):
    def confirm(self):
        pass

    def cancel(self):
        pass


if __name__ == '__main__':
    ip = "127.0.0.1:62001"

    # PAGETEMP = [0,[[1,[459,1433]],[2,[818,75]],[3,[450,1235]]]]
    PATH = os.getcwd()
    print("the program runs in the directory: " + PATH)
    POINT = np.array([('x', 'i2'), ('y', 'i2')])
    ICON = np.dtype([('to', 'i1'), ('x', 'i2'), ('y', 'i2')])

    #d = ui2.connect(ip)
    d = ui2.connect_usb()


    game = Game()
    game.listen_click()
    game.learn()
    # game.login()

# 公告825 80  关闭公告825 240 进入游戏450 1440
