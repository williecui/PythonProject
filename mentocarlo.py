#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 10:43:57 2017
@author: ryan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def easy_function(x):
    return((3)*(x**2))

def hard_function(x):
    return((1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2))

X=np.linspace(-20,20,1000)
plt.plot(X,easy_function(X))
# plt.show()

plt.plot(X,hard_function(X))
# plt.show()

def integrate(x1,x2,func=easy_function,n=100000):
    X=np.linspace(x1,x2,1000)
    y1=0
    y2=max((func(X)))+1
    print(x1,x2,y1,y2)
    area=(x2-x1)*(y2-y1)
    check=[]
    xs=[]
    ys=[]
    for i in range(n):
        x=np.random.uniform(x1,x2,1)
        xs.append(x)
        y=np.random.uniform(y1,y2,1)
        ys.append(y)
        if abs(y)>abs(func(x)) or y<0:
            check.append(0)
        else:
            check.append(1)
    return(np.mean(check)*area,xs,ys,check)

print(integrate(0.3,2.5)[0])
print(integrate(0.3,2.5,hard_function)[0])

_,x,y,c=integrate(0.3,2.5,n=100)
print("x", x)
print("y", y)
print("c", c)

df=pd.DataFrame()
df['x']=x
df['y']=y
df['c']=c

print (type(df['c']))
print (df['c']==1)
print (df[df['c']==1]['x'] )

X=np.linspace(0.3,2.5,1000)
plt.plot(X,easy_function(X))
plt.scatter(df[df['c']==0]['x'],df[df['c']==0]['y'],color='red')
plt.scatter(df[df['c']==1]['x'],df[df['c']==1]['y'],color='blue')
# plt.show()