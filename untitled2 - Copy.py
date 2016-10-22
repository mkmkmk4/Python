# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:55:02 2016

@author: My Laptop
"""
import numpy as np
import matplotlib.pyplot as plt
v=np.arange(1,11,1)
t=np.arange(1,20,2)
v_uncert=[.6,.9,1,.32,1,.323,.5,.1,.9,.32]
print(len(v)==len(t))
plt.errorbar(t,v,v_uncert,fmt='o')
plt.xlabel('t')
plt.ylabel('v')
plt.title("V vs T")
plt.show()

