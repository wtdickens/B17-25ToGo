# -*- coding: utf-8 -*-
def DeterminePosition(EventDict, DataDict):
    """
    Created on Sat August 15 15:26:41 2020

    This routine determines the position of the B-17 in the formation

    Parameters
    ----------
    EventDict : python dictionary
        Contains event flag that can modify position
    DataDict : python dictionar
        Contains value of crew skill level
        
    Returns
    -------
    DataDict : python dictionary
        Modified DataDict to record formation position

    @author: wtdic
    """
    
    from B17Dice import d10
    
    positionDraw = d10() + DataDict["BomberData"]["Skill"]
    
    if positionDraw <= 6:
        position = "middle"
    elif positionDraw <= 8:
        position = "rear"
    elif positionDraw <= 10:
        position = "front"
    else:
        position = "lead"
        
    if EventDict["EventSwitches"]["Bump2Lead"]:
        position = "lead"
        
    DataDict["BomberData"]["Position"] = position
        
    return(DataDict)
    
    

