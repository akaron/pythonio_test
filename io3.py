#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# 參數
filename = "data.dat"

wavelength = [] # 空陣列，等等會附加(append)東西進去
flux = []

# 讀入資料
with open(filename,'r') as f:
    while True:
        line = f.readline()
        if line:
            col1, col2 = line.split() # 注意：split()回傳字串而不是數值
            wavelength.append(float(col1))
            flux.append(float(col2))
        else:
            break

print "wavelength", wavelength
print "flux", flux

# 畫圖
ax = plt.subplot(111)
ax.plot(wavelength, flux)
ax.set_xlabel("Wavelength [Angs]")
ax.set_ylabel(r"Flux [erg/s/cm$^2$/Angs]")
plt.show()


# Note:
#   1. 先定義兩個空陣列 wavelength 跟 flux, 等等附加(append)數值進去
#       * 這兩個空陣列"不是"numpy的陣列, 需要用到numpy陣列的方法處理資料
#         的話要另外轉。numpy有append方法但似乎不適合在這用
#   2. 資料有兩欄, 所以line.split()回傳兩個字串, 把兩個字串用float()轉成
#      浮點數(float)再附加到空陣列中
#   3. 畫圖時我用了 axes 物件 ax, 他有許多方法(method)可用, 畫多張圖時也
#      有用, 之後再詳細介紹
#      
# Next:
#   * 用 asciitable 讀資料, asciitable 要另外裝
#   * 更多畫圖的微調
#
