# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:29:40 2016

@author: My Laptop
"""

def Collatz(n):
    if(n%2==0):
        v=n/2
        return v
        
    else:
        v=(3*n)+1
        return v        
Collatz_Current=363                 #Input to Collatz function
temp=0
Num_Steps=0
while(Collatz_Current!=1):
    temp=Collatz(Collatz_Current)
    Collatz_Current=temp
    Num_Steps=Num_Steps+1
    
    
print (Collatz_Current)
print (Num_Steps)