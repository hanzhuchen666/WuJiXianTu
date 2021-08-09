# -*- coding: utf-8 -*-
import numpy as np
import uiautomator2 as u2
import adbutils
import time

SLEEP = 3
def login(d):
    #启动应用
    d.xpath('//*[@text="无极仙途"]').click()
    time.sleep(SLEEP)
    d.click(441, 1440)
    time.sleep(SLEEP)
    d.click(766, 398)


def logout(d):
    d.stop_app('//*[@text="无极仙途"]')

def click():
