#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 得到數值
a = np.linspace(0,2*np.pi, 100)
b = np.sin(a)
c = np.cos(a)

# 畫第一張圖（第一個座標軸)
ax1 = plt.subplot(211) #注釋1
ax1.plot(a, b, label = "sine") #如果不用放標籤(legend)的話, 不用label也行
ax1.set_title("sin(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

# 畫第二張圖（第二個座標軸)
ax2 = plt.subplot(212)
ax2.axis([np.amin(a),np.amax(a),np.amin(b),np.amax(b)]) #調整ax2的座標軸顯示的範圍
#ax2.axis([0,2*np.pi,-1,1]) #也行, 但得要自己算, 交給電腦看數值的範圍就好囉
#ax2.axis([np.amin(a),np.amax(a),np.amin(b)*1.2,np.amax(b)]) # y軸的範圍為y最大值加20%的空間
ax2.plot(a, c, label = "cosine")
ax2.set_title("cos(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# 示範一個同時改多個axes的參數的方法
for ax in ax1, ax2:
    ax.legend()
# 以上相當於打了 ax1.legend() 跟 ax2.legend() 兩行; 同理, 可以加上 ax.set_xlabel() 跟 ax.set_ylabel();
# 將各個圖都相同的屬性或都要執行的函式放在一起控管！

plt.show()

# 注釋:
# 1. plt.subplot(211)的"211"是縮寫, 代表總共有兩列/一欄/目前為第一張圖, 若超過十張圖則不能用縮寫, 要用:
#    plt.subplot(numRows=2, numCols=1, plotNum=1) 或 plt.subplot(2, 1, 1) 的格式。
#    plt.subplot 會自動算每一列/欄的高度及寬度(但是在視窗顯示時，預設值常常會擠在一起)
# 2. (個人習慣) 就算只畫一張圖還是寫出 ax1 = plt.subplot(111)，這樣的話，比如說，我只要記 ax1.set_xlabel()
#    而不用記 plt.xlabel() 跟其他在 plt.xxxx 跟在 ax1.xxxx 同功能但長得不一樣的函式
