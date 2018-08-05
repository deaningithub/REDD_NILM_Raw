# -*- coding: utf-8 -*-

from bitstring import BitArray, BitStream, Bits
#Use bitstring to readin file.
with open("G:\SmartMeter\\high_freq_raw\\house_3\\current_1\\1303091049", "rb") as f:
    p = Bits(f)
a=p[0:8]
_Timestamplist = list(p.findall('0x74696d65', bytealigned=True))

for i in range(len(_Timestamplist)):
    #print(p[_Timestamplis[i]:p[_Timestamplis[i]+32.tobytes(),p[_Timestamplis[i]+32:_Timestamplis[i]+64].intle, p[_Timestamplis[i]+64:_Timestamplis[i]+96].intle)
    print(p[_Timestamplist[i]:_Timestamplist[i]+32].tobytes(),p[_Timestamplist[i]+32:_Timestamplist[i]+64].intle,p[_Timestamplist[i]+64:_Timestamplist[i]+96].intle,p[_Timestamplist[i]+96:_Timestamplist[i]+128].floatle)
    
#print(p[0:32].tobytes(),p[32:64].intle, p[64:96].intle,p[96:128].floatle,p[128:160].floatle,p[160:192].floatle)
#print(p[0:32])
