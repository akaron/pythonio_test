#!/usr/bin/env python
# -*- coding: utf-8 -*-
# modify from: http://matplotlib.org/examples/pylab_examples/axes_demo.html

import numpy as np
import matplotlib.pyplot as plt

# 參數
filename = 'ngc5194_0411.dat'

# 讀資料
wavelength = [] # 空陣列，等等附加(append)東西進去
flux = []
with open(filename, 'r') as f:
    while True:
        line = f.readline()
        if line:
            col1, col2 = line.split()
            wavelength.append(float(col1))
            flux.append(float(col2))
        else:
            break
#將python的list轉成numpy array, 因為有些numpy函式只接受numpy array
wavelength = np.array(wavelength) 
flux = np.array(flux)

# 示範accumulate函式
flux_acc = np.add.accumulate(flux)/100 # this means nothing

# 第一個axes
ax1 = plt.subplot(111)
ax1.plot(wavelength, flux, label='original', color='#22df22')
ax1.plot(wavelength, flux_acc, label='accumulated', color='#df2222')
#ax1.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s) ]) # 圖中數值的範圍
ax1.set_xlabel("Wavelength [Angs]")
ax1.set_ylabel("Flux [erg/s/cm$^2$/Angs]") 
# 錢號($)裡面進入LaTeX的數學模式; 括號前的"r"表示後面括號裡的"\"跳脫符號會視為一般符號；
# 然後，matplotlib預設是"usetex=True"，就是可以用tex表示，所以有時會出現"\"，所以習慣要用
# 到LaTeX符號就在字串前面加上"r"
ax1.set_title('ngc 5194')

# 第二個axes
ax2 = plt.axes([0.2, 0.6, .2, .2], axisbg='red')
condition1 = [ (wavelength>4000) & (wavelength<=5000) ] # 注釋1
ax2.plot(wavelength[condition1], flux[condition1])
ax2.set_title(r'4000-5000 $\AA$')

# 幾種設定刻度的方法
ax2.set_xticks([4000, 4500, 5000]) # 手動設定x軸所要標出的刻度
#ax2.set_xticks([]) # x軸不標任何刻度（給了空陣列）
ax2.yaxis.set_major_locator(plt.MaxNLocator(4)) # 設定y軸最多要有幾個刻度
#plt.setp(ax2, xticks=[4000, 4500, 5000], yticks=[]) #另一種設定ticks(刻度)的方法

# 第三個axes
ax3 = plt.axes([.65, .6, .2, .2], axisbg='yellow')
condition2 = [ (wavelength>6400) & (wavelength<=6700) ]
ax3.plot(wavelength[condition2], flux[condition2])
ax3.set_title(r'6400-6700 $\AA$')
ax3.xaxis.set_major_locator(plt.MaxNLocator(3)) # 設定x軸最多3個刻度
ax3.yaxis.set_major_locator(plt.MaxNLocator(3)) # 設定y軸最多3個刻度

# 加文字, transform把座標軸改成圖形本身，也就是圖的左下角為(0,0)，右上角為(1,1)這樣
ax1.text(5000, 0.5e-13, 'Hello')
ax1.text(0.5, 0.5, 'Hey',
        horizontalalignment='center',
        verticalalignment='center',
        transform = ax1.transAxes) #

# 加annotation (annotation包含了要標記點的座標跟要標記的文字以及文字的座標, 
# 點跟文字中間可以用箭頭相連)
ax1.annotate('3k', xy=(3000, 0), xytext=(3000, -0.5e-13), xycoords='data') 
ax1.annotate('4k', xy=(4000, 0), xytext=(4000, -0.5e-13), xycoords='data',
             horizontalalignment='center',
             arrowprops=dict(arrowstyle='-', facecolor='black')) # 用arrowstyle改成沒有箭頭的形式

#加很多annotation。這裡的方法：因為每一個annotation的格式都差不多，需要的參數就是要標記的點
#要輸入的文字，以及文字的座標，把這些資訊通通放到一個陣列(list或tuple)裡面，比如說，以下的
#"my_labels"是一個tuple陣列，內含四個陣列，內含的四個陣列各個都是一組annotation的資料
#ps1. 一個一個打可能沒有複雜太多，但是，比如說，想改箭頭樣式的話要一行一行改，這邊只要改一個地方
#ps2. 另一個方法是用物件導向來作，感覺程式碼更容易看懂，暫時先不提（？）
y_text = -0.5e-13 # annotation的文字的y軸座標
my_labels = ( ('A'          , [5200,0], [5200, y_text] ),
              ('B'          , [5500,0], [5500, y_text] ),
              ('C'          , [5560,0], [5560, y_text*1.5] ),
              (r'$H_\alpha$', [6563,0], [6563, y_text] ) )

for lbl in my_labels:
    ax1.annotate(lbl[0], xy=lbl[1], xytext=lbl[2], xycoords='data',
             horizontalalignment='center',
             arrowprops=dict(arrowstyle='-', facecolor='black'))


plt.show()

#注釋
#   1. 若只有一個條件，則寫成
#        condition1 = [ wavelength>4000 ]
#      condition1 會是一個跟 wavelength 陣列一樣大的陣列, 上面這行指令會將 wavelength 陣列的每個值
#      來作判斷，如果大於4000就回傳True，小於4000則回傳False；True跟False會存到condition1相對映的
#      元素裡。比如說 wavelength第一個元素小於4000，故回傳False，故condition1陣列第一個元素是False
#
#      利用這種陣列，可以從原來的陣列只選擇符合條件的列出來（實際操作)
#      以下是範例：
#
# In [1]: import numpy as np
# 
# In [2]: a = np.random.rand(5)
# 
# In [3]: a
# Out[3]: array([ 0.81482269,  0.06896246,  0.95026395,  0.40936113,  0.74385615])
# 
# In [4]: a>0.5
# Out[4]: array([ True, False,  True, False,  True], dtype=bool)
# 
# In [5]: a[a>0.5]
# Out[5]: array([ 0.81482269,  0.95026395,  0.74385615])

# Todo: label
# 
