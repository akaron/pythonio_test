#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# 讀入資料的副程式
def read_a_file(filename):
    col1 = []
    col2 = []
    with open(filename,'r') as f:
        while True:
            line = f.readline()
            if line:
                tmp1, tmp2 = line.split() # 注意：split()回傳字串而不是數值
                col1.append(float(tmp1))
                col2.append(float(tmp2))
            else:
                break
    return col1, col2

wavelength1, flux1 = read_a_file('data.dat')
wavelength2, flux2 = read_a_file('data2.dat')
print "wavelength1", wavelength1
print "flux1", flux1

print "wavelength2", wavelength2
print "flux2", flux2

plt.plot(wavelength1, flux1)
plt.plot(wavelength2, flux2)
plt.show()

