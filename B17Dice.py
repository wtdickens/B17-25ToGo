# -*- coding: utf-8 -*-
def d10()
"""
Created on Tue Jul 28 21:57:38 2020

This routine rolls a d10 and returns a value 1-10

Parameters
----------
None

Returns
-------
value pyhon integer (1-10)

@author: wtdic
"""
from numpy import random as nprandom
return(int(nprandom.uniform(0,10)) + 1)
