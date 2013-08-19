#!/usr/bin/env python
# -*- coding: utf-8 -*-
# modify from: http://matplotlib.org/examples/pylab_examples/axes_demo.html

import numpy as np
import matplotlib.pyplot as plt

# create some data to use for the plot
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000]/0.05)               # impulse response
x = np.random.randn(len(t))
s = np.convolve(x,r)[:len(x)]*dt  # colored noise

# the main axes is subplot(111) by default 預設的座標軸是 plt.subplot(111)
ax1 = plt.subplot(111)
ax1.plot(t, s)
ax1.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s) ]) # 圖中數值的範圍
ax1.set_xlabel('time (s)')
ax1.set_ylabel('current (nA)')
ax1.set_title('Gaussian colored noise')

# this is an inset axes over the main axes
ax2 = plt.axes([.65, .6, .2, .2], axisbg='yellow')
n, bins, patches = ax2.hist(s, 400, normed=1)
ax2.set_title('Probability')
plt.setp(ax2, xticks=[], yticks=[]) # ???

# plt.axes()  加上另一張圖（或稱座標軸), 參數1的陣列裡面4個參數為:圖左下角的位置跟寬/高, 
# 單位是normalized到(0,1)的範圍, 參數2 axisbg 是背景(y=黃色)

# this is another inset axes over the main axes
ax3 = plt.axes([0.2, 0.6, .2, .2], axisbg='red')
ax3.plot(t[:len(r)], r) # 這時候已經選了這個axes了, 就畫在這個axes上 (???)
ax3.set_title('Impulse response')
plt.setp(ax3, xlim=(0,.2), xticks=[], yticks=[]) # 設定數值的範圍

plt.show()
