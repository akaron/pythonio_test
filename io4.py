#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import asciitable

# 參數
filename = "data.dat"

# 讀入資料
data = asciitable.read(filename)
wavelength = data['col1']
flux = data['col2']

print "wavelength", wavelength
print "flux", flux

# 畫圖
ax = plt.subplot(111)
ax.plot(wavelength, flux)
ax.set_xlabel("Wavelength [Angs]")
ax.set_ylabel(r"Flux [erg/s/cm$^2$/Angs]")
#ax.annotate('pi', xy=(np.pi,0), 
#        xytext=(np.pi,0.2),
#        arrowprops=dict(facecolor='black', shrink=0.05, width=0.01, headwidth=0))
#ax.annotate('0.5*pi', xy=(0.5*np.pi,0), 
#        xytext=(0.5*np.pi,-0.2),
#        arrowprops=dict(facecolor='black', shrink=0.05, width=0.01, headwidth=0))
## 寫一個小程式取代以上六行(因為輸入參數有重複的部份，也有需要算的部份)
def my_annotate(text, xy, text_rel, arrowprop):
    # text      : 要標記的字串
    # xy        : 要標記的點的座標
    # text_rel  : 要標記的文字的座標"相對"於該點的距離
    # arrowprop : 點到文字間的線段/箭頭的屬性[dict]
    ax.annotate(text, xy=xy, xytext=(xy[0]+text_rel[0], xy[1]+text_rel[1]),
            arrowprops=arrowprop,  horizontalalignment='center')
arrowprop1 = dict(shrink=0.05, width=0.01, headwidth=0) # if headwidth != 0 then there's arrow
arrowprop2 = dict(facecolor='yellow', shrink=0.05, width=0.01, headwidth=12)
my_annotate(text=r"$\pi$", xy=[np.pi,0], text_rel=[0,0.2], arrowprop=arrowprop1)
my_annotate(text=r"$0.5 \times \pi$", xy=[0.5*np.pi, 0], text_rel=[0,-0.2], arrowprop=arrowprop1)
my_annotate(text=r"$1.5 \times \pi$", xy=[1.5*np.pi, 0], text_rel=[0,-0.5], arrowprop=arrowprop2)
my_annotate("0", (0,0), (0.3,-0.3), arrowprop2)

plt.show()


# Note:
#   1. 用asciitable套件主要的差別只有在讀入資料的部份, 其他大致上不變
#       * asciitable包含在astropy裡面, 有裝astropy就不用再裝asciitable,
#         不過module的全名可能不太一樣（要再查）
#       * 用python的好處是有很多現成的模組(module), 還有要自己發展也很 
#         容易；有些程式片段常用到的話就寫成模組或用"物件/方法"來寫
#   2. 用"ax.annotate()"來標記字串（包含連結的箭頭或線段）
#       * 因為我們想要標記的字串跟線段的格式都一樣（某個資料點再高一點或低一點）
#         所以寫了個小小的副程式來產生要丟給ax.annotate()的參數，
#         這樣點多的時候比較方便
#       * 範例：http://matplotlib.org/examples/pylab_examples/annotation_demo.html
#
# Python style:
#   1. 有需要縮排的話, 應空4個空白
#   2. 通常等號兩端要空一個
#   3. 通常逗號右邊要空一格, 左邊不用
#   4. 多用變數; 避免magic number
#   5. ...
#
# Next:
#   * subplots
#   * label
#   * 調整字型大小
