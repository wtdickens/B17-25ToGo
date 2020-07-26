# -*- coding: utf-8 -*-
def Data(year)
"""
Created on Sun Jul 26 13:35:41 2020

This Routine initializes the data for the B17 simulation

Parameters
----------
year : python integer (values 1942-44)
    The start year for the simulation

Returns
-------
DataDict : Python dictionary
    This dictionary contains the data for the simulation for 
    the given year

@author: wtdic
"""

banditType = {1 : "BF-109",
              2 : "BF-109",
              3 : "BF-109",
              4 : "FW-190",
              5 : "FW-190",
              6 : "FW-190",
              7 : "BF-110",
              8 : "BF-110",
              9 : "ME-410",
              10 : "ME-410"}

celebrate = {1: "YeeeeHaw! Smoked em!",
             2: "I got him! I got him!",
             3: "Gerry is popping silk!",
             4: f"{banditType}Trailing smoke! I got him.",
             5: f"Scratch one {banditType}!",
             6: }


DataDict = {"BanditType" : banditType,
            }


