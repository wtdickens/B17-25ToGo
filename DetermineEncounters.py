# -*- coding: utf-8 -*-
def DetermineEncouter(year):
    """
    Created on Sat August 15, 2020

    This routine determines the mission event

    Parameters
    ----------
    year: integer
        year of the mission

    Returns
    -------
    Encounters : string
        String containing encounters for mission

    @author: wtdic
    """
    
    from B17Dice import d10
    
    if year == 1942:
        BanditProb = 7
        2ndBanditProb = 0
        FlackProb = 5
        BanditProb2 = 4
        FlackProb2 = 0
        2ndBandit2 = 0
    elif year = 1943:
        BanditProb = 8
        2ndBanditProb = 2
        FlackProb = 5
        BanditProb2 = 7
        FlackProb2 = 0
        2ndBandit2 = 3
    else:
        BanditProb = 6
        2ndBanditProb = 2
        FlackProb = 9
        BanditProb2 = 6
        FlackProb2 = 3
        2ndBandit2 = 3

    EncounterString = []
    
    BanditPull = d10()
    if BanditPull <= 2ndBanditProb:
        EncounterString.append("2Bandits")
    elif BanditPull <= BanditProb:
        EncounterString.append("Bandit")
        
    if d10() <= FlackProb:
        EncounterString.append("Flack")
        
    EncounterString.append("BombRun")
    
    if d10() <= FlackProb2:
        EncounterString.append("Flack")
    
    BanditPull = d10()
    if BanditPull <= 2ndBandit2:
        EncounterString.append("2Bandits")
    elif BanditPull <= BanditProb2:
        EncounterString.append("Bandit")
        
return(EncounterString)