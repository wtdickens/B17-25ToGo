# -*- coding: utf-8 -*-
def BanditAttack(year, position, damageStatus, dataDict)
"""
Created on Sun Jul 26 13:44:49 2020

This routine computes the outcome of a bandit attack
on the formation the bomber is in

Parameters
----------
year : python integer (1942-44)
    The year the action is taking place
position : python string ("middle","lead","front","rear")
    The B-17s position in the formation
damageStatus : python binary
    True = damaged
    False = OK
dataDict : Python dictionary
    dictionary containing data used in simulation

Returns
-------
outcome : python string
    Text message describing the outcome

@author: wtdic
"""
from B17dice import d10

# Determine if attack on bomber takes place
modifier = 0 
if year == 1942:
    modifier = -2
elif year == 1944:
    modifier = -1

if damageStatus:
    modifier += 5
    
if position == "lead":
    modifier += 3
elif position == "front":
    modifier += 2
elif position == "rear"
    modifier += 1

roll = d10() + modifier()

if roll < 8:
    # No bandit attack. Return safe text.
    return("Bomber Group wards off attack. You are safe for now.")
else:
    # Bomber is attacked.  Compute Results.
    
    # Find Bandit Type
    banditType = dataDict["BanditType"][d10()]
    returnText = banditType
    
    # Determine direction of attack
    if position == "front":
        modifier = 2
    elif position == "lead":
        modifier = 3
    elif position == "rear":
        modifier = -2
    else:
        modifier = 0
    
    # Determine direction of attack
    roll = modifier + d10()
    if roll < 4:
        attackDirection = "rear"
        returnText += " attacking from the rear!\n"
    elif roll <6:
        attackDirection = "port"
        returnText += " attacking port side!\n"
    elif roll < 8:
        attackDirection = "starboard"
        returnText += " attacking starboard!\n"
    else:
        attackDirection = "front"
        returnText += " dead ahead!\n"
    
    # Determine if crew is fast
    modifier = dataDict["BomberData"]["skill"]
    if d10() + modifier >= 8:
        fastQ = True
        returnText += "RATATATATATATAATATATATATAT\n"
    else:
        fastQ = False
        returnText += "{Tracer fire whips past the cockpit\n}"
    
    # Determine outcome
    if fastQ:
        AtA = dataDict["BomberData"]["ATA"][position]
        if d10() >= AtA:
            celebrate = dataDict["Celebrate"][d10()]
            returnText += 
            return(returnText)
    
    




