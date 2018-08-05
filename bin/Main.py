# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 10:57:34 2018

@author: user
"""
import bitstring
import matplotlib.pyplot as plt
fname = "G:\SmartMeter\\high_freq_raw\\house_3\\current_1\\1303091049"
b = bitstring.BitArray(bytes = open(fname,"rb").read())
fig = plt.figure()
_length = len(b.bin)

width = 10000
column = _length // width + 1
print(width,column)
ax = fig.add_axes((0, width/1000, 0, column/1000))
plt.show()
#print(b.hex[0:1000])
