# -*- coding: utf-8 -*-
def bomberFires(position, event, banditDefense,
                bomberData, returnText, dataDict):
    """
    Created on Mon Jul 27 11:44:59 2020
    This routine determines the outcome when the bomber fires at a bandit

    Parameters
    ----------
    position: python string 
        direction from which bandit is attacking
    event: python integer (1-10)
        Event for current mission
    banditDefense: python integer
        Adjustment to bomber ata for bandit defense
    bomberData: python dictionary
        dictionary containing bomber data
    returnText: python string
        text string containing color dialog and events
    dataDict: python dictionary 
        contains all game data
    
    Returns
    -------
    result: python string
        was bandit shot down ("shot down","escaped")
    returnText: python string
        text string containing color dialog and events

    @author: wtdic
    """
    
    ata = bomberData["AtA"][position]
    if event == 2:
        ata -= 1
    ata += banditDefense
        
    # Bandit shot down
    if d10() >= ata:
        celebrate = dataDict["Celebrate"][d10()]
        pos = celebrate.find("{")
        if pos >=0:
            returnText += (celebrate[:pos] + banditType +
                           celebrate[pos+2:] + "\n")
            bomberData["XP"] += 1
        else:
            returnText += celebrate + "\n"
            return("OK\n + returnText)
        result = "shot down"
    # Bandit missed
    else:
        result = "escaped"
        
    return(result, returnText)
        
