#!/usr/bin/python
import numpy as np
x1 = np.linspace(1,10)
x2 = np.linspace(1,10,num = 10,retstep = True)
x3 = np.linspace(1,10,retstep = True)
x4 = np.linspace(1,10,num = 10)

print("x1", x1)
print("x2", x2)
print("x3", x3)
print("x4", x4)

print("length of x1 is %d" % len(x1))
print("length of x2 is %d" % len(x2))
print("length of x3 is %d" % len(x3))
print("length of x4 is %d" % len(x4))
