# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 09:44:07 2018

@author: user
"""

import bz2

input_file = bz2.BZ2File('G:\SmartMeter\\high_freq.tar.bz2', 'rb')
try:
    print(input_file.read())
finally:
    input_file.close()