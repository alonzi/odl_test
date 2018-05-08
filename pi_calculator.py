#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:32:29 2018

@author: lpa2a
"""

from numpy.random import rand

N = 10e6
RADIUS = 1
count = 0

for i in range(int(N)):
  x = (rand()-0.5)*2.
  y = (rand()-0.5)*2.
  if (x**2+y**2)**(1./2.)<=1: count+=1

print("Estimate of pi:",4*count/N)
print("Estimate of er:",4*count/N*(1/(count**(1./2.))))