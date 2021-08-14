# -*- coding: utf-8 -*-
import numpy as np
import uiautomator2 as u2
import adbutils
import time
import os

###
print(os.getcwd())
###
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

POINT = np.dtype([('x', 'i2'), ('y', 'i2')])
ICON = np.dtype([('to', 'i1'), ('x', 'i2'), ('y', 'i2')])

test = np.array([1,2,3],dtype=ICON)
test2 = np.array([2,2],dtype=POINT)
test3 = np.array([1,2],dtype=POINT)
gather = np.array([(2,2), (1,3),(1,4)],dtype=POINT)

print(test)
print(gather)



