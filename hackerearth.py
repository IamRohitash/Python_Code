#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import math as m
T=int(input())
while T>0:
    x1,y1,x2,y2,v1,v2=[int(x) for  x in input().split()]
    x=x1
    y=0
    d1=m.sqrt((x-x1)**2+(y-y1)**2)
    d2=m.sqrt((x-x2)**2+(y-y2)**2)
    t1=d1/v1
    t2=d2/v2
    t=t1+t1
    print('%.5f'% t)
    T-=1


# In[ ]:




