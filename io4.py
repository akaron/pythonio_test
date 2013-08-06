#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
plt.show()


# Note:
#   1. 用asciitable套件主要的差別只有在讀入資料的部份, 其他大致上不變
#       * asciitable包含在astropy裡面, 有裝astropy就不用再裝asciitable,
#         不過module的全名可能不太一樣（要再查）
#       * 用python的好處是有很多現成的模組(module), 還有要自己發展也很 
#         容易；有些程式片段常用到的話就寫成模組或用"物件/方法"來寫
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
