#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:41:32 2022

@author: hc
"""

from pylab import *

m=40e-3/6.02e23
kb=1.38e-23

def ddp(v,T):
    return 4*pi*(m/(2*pi*kb*T))**1.5*v*v*exp(-m*v*v/2/kb/T)

