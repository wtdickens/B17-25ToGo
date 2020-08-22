# -*- coding: utf-8 -*-
banditFires(eventData, returnText, dataDict):
    """
    Created on Fri Aug 21 12:57:09 2020

    This subroutine computes the results of a bandit firing at the bomber

    Parameters
    ----------
    eventData: Dictionary
        Contains the information on modifications due to events
        
    returnText: String
        Contains the text description of events to be reported to the player
        
    dataDict: Dictionary
        Contains game data
        
    Returns
    -------
    shotDown: Boolean
        Was the bomber shot down?

    returnText: String
        Contains the text description of events to be reported to the player
        
    dataDict: Dictionary
        Contains game data

    @author: wtdic
    """
    from B17Dice import d10
    from BomberHit import DetermineDamage
    
    # Determine bandit to hit number
    banditAtA = dataDict["BanditAtA"] + EventDict["BanditAtA"]
    if year == 1942: # Add year modifier
        banditAtA -= 1
    elif year == 1944:
        banditAtA += 1
        
    # Results of bandid fire
    if d10() < banditAtA:  # Miss
        returnText += "OK\nWhew that was close!\n"
    else:   # Hit
        shotDown, returnText, dataDict = DetermineDamage(dataDict,
                                                         returnText,
                                                         EventDict
                                                         )
        
    return(shotDown, returnText, dataDict)
           
                        
                            