#!/usr/bin/env python
# -*- coding: utf-8 -*-

filename="data.dat"

with open(filename,'r') as f:
    while True:
        line = f.readline().strip()
        if line:
            #print line.split()
            wavelength, flux = line.split()
            print wavelength, flux
        else:
            break

# Note:
#   1. 用 "with open(file, mode) as f:" 開檔的目的：
#       * 例外(exception)處理
#       * 在這個 block 結束後自動關檔 (f.close())
#   2. 字串的strip()跟split()方法
#       * strip()方法去除字串前端跟尾端的空白（包含斷行）字元
#       * wavelength, flux = line.split()
#           * line.split() 把line字串分成多個字串, 預設是以空白做
#             分隔符號, 會回傳多個字串, 所以左邊也要有相對映的變數
#             儲存.split()的回傳值
# Next:
#   * 把回傳值存到陣列/畫圖
