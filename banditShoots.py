# -*- coding: utf-8 -*-
def banditFires(position, event, bomberData, returnText, dataDict)
    """
    Created on Tue Jul 28 22:52:04 2020
    This routine computes the results of bandit fire on the bomber

    Parameters
    ----------
    position: python string 
        direction from which bandit is attacking
    event: python integer (1-10)
        Event for current mission
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
    returnText:
        text string containing colot dialog and events
        
    @author: wtdic
    """

