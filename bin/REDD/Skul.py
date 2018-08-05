# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:24:03 2018

@author: user
"""
#All member counter are 1 base
#All Day counter are 1 base
import numpy as np
DayLong = 28
_MemberNumber = 7
_Weekend = 2
_Rate = 5/2
_DTotal = 4  # while 12 days ago, become 3
_ETotal = 3
_NTotal = 3


n = _MemberNumber + 1;  m = DayLong+1
a = [[0] * m for i in range(n)]
_EStyle = [number for number in range(0,15)]
_EStyle[1] = "D";_EStyle[2] = "D";_EStyle[3] = "D";_EStyle[4] = "D"
_EStyle[5] = "D";_EStyle[6] = "D+E";_EStyle[7] = "D+E";_EStyle[8] = "E"
_EStyle[9] = "E";_EStyle[10] = "E";_EStyle[11] = "N";_EStyle[12] = "N"
_EStyle[13] = "N";_EStyle[14] = "N"
 
# All member are 1-base, the first column record the pre-mounth state.

a[1][13] = "R1" ; a[1][14] = "R1" ;a[1][27] = "R2";
a[2][16] = "R1" ; a[2][21] = "R1" ;a[2][22] = "R2";
a[3][7] = "R1" ; a[3][8] = "R1" ;a[3][18] = "R2";
a[4][7] = "檢" ; a[4][23] = "R1" ;a[4][28] = "檢";
a[5][1] = "R1" ; a[5][15] = "R1" ;a[5][20] = "R2";
a[6][10] = "R1";a[6][11] = "R1";a[6][24] = "R2";
a[7][13] = "R2";a[7][21] = "R1";a[7][22] = "R1";


_DTotalWorkDay = _DayLong * _DTotal
_ETotalWorkDay = _DayLong * _ETotal
_NTotalWorkDay = _DayLong * _NTotal

_SkulGrade = 1000
#while _SkulGrade :
    

