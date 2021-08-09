# -*- coding: utf-8 -*-
import time
import numpy as np
import uiautomator2 as ui2
import cv2

import subprocess


class Page:

    def __init__(self):
        self.image= [[0, 0]]


    def detect(self):
        # 首先截图，保存截图图片，
        # 读取层级结构
        # 对于每个按钮元素，声明新的按钮类，分配id
        pass

    def save(self):
        # 保存截图，保存树形结构
        pass

    def read(self):
        pass
        # 以数组的形式返回，并且调用icon的同名函数
    def judgeImage(self, image, imagePool):
        for i in imagePool:
            pass

    def getScreen(self):
        d.screenshot(format= 'opencv')


class Icon:
    def __init__(self, father):
        self.father = father
        self.location = [[0, 0], [1, 1]]
        self.name = ""
        self.image = [[0, 0]]
        self.to = 0

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

    def copy(self):
        pass


class Game:
    structGraph = []
    SLEEP = 5
    pagenumber = 0

    def __init__(self):
        pass


    def login(self):
        # 启动应用
        d.xpath('//*[@text="无极仙途"]').click()
        time.sleep(self.SLEEP)
        d.click(441, 1440)
        time.sleep(self.SLEEP)
        d.click(766, 398)

    def learn(self):
        x = eval(input("please input the x location of the point"))
        y = eval(input("please input the y position of the point"))
        d.click(x,y)
        page = Page()

        ifnew = page.judgeImage()
        if ifnew:
            pass


    def play(self):
        pass

    structure = []


if __name__ == '__main__':
    ip = "127.0.0.1:62001"
    subprocess.run("adb kill-server")
    subprocess.run("adb start-server")
    subprocess.run("python -m uiautomator2 init")
    subprocess.run("adb connect "+ip)
    subprocess.run("adb devices")
    global d
    d = ui2.connect(ip)
    game = Game()
    game.login()


