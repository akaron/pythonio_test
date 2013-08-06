#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('data.dat', 'r')

while True:
    line = f.readline() 
    # line = f.readline().strip() # .strip(): 去掉行尾的斷行
    if line:
        print line 
    else:
        break

f.close()

# Note:
#   1. python裡所有東西都是物件, 像是"f"是檔案物件, "line"是字串物件
#   2. 物件有物件的"方法"(methods), 像是"f"有read(), readline()等等方法
#       2.1 方法(methods) 可以想成是該物件專屬的副程式或函式
#       2.2 methods 結尾都要用一組小括弧"()"來表明他是方法
#       2.3 f.readline()回傳一個"字串"(string)物件, 該物件有他自己的方法,
#           像是"strip()", 所以方法可以這樣串起來
#   3. 檔案物件"f"
#       3.1 open(檔案名, 模式) 回傳一檔案物件, 命名為"f"
#           * 模式主要有"r","w","a", 分別為"read", "write", "append"
#       3.2 每叫一次 f.readline() 就讀入一行檔案（他會記得上次讀到哪一行）
#           * "一行檔案"包含換行字元"\n", 可以用字串的strip()方法去除
#       3.3 通常不會知道總共有幾行, 所以通常 f.readline() 放到 while 迴圈裡
#           * (重要) while 迴圈永遠要記得設一個 break
#           * 讀到檔案尾端後, f.readline() 會回傳空字串"", 而對python而言,
#             空字串為false (可以在終端機底下開python直譯器來試)
#       3.4 （重要）記得要用 close 方法關掉檔案
#       3.5 可以用 f.read() 讀入整個檔案, 或指定大小, 不過這邊不適合用這個方法
# Next:
#   * 下一個範例會介紹比較好的開檔案方式
#   * 介紹讀檔時常用的字串方法
#
