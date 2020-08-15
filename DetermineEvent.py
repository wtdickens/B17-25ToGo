# -*- coding: utf-8 -*-
def DetermineEvent():
    """
    Created on Sat August 15, 2020

    This routine determines the mission event

    Parameters
    ----------
    none

    Returns
    -------
    EventDict : Python dictionary
        Values to set Bandit Ata, Bomber AtA, and embeded dictionary with switches
        for rear attack only bumped to lead, crew wounded only, hit damage +1,
        Bomber is Fast, Flack -1, Replacement Ball gunner, Bandit attacks two 
        turns.

    @author: wtdic
    """
    
    from B17Dice import d10
    
    # initialize event values and switches
    BanditAtA = 0
    BomberAtA = 0
    BomberAtG = 0
    RearOnly = False
    Bump2Lead = False
    CrewWound = False
    HitDamage =  1
    BomberFast = False
    FlackDamage = -1
    ReplaceBall = False
    BanditAttack2 = False
    
    # draw event
    event = d10() - 1
    
    # Set event results
    if event == 0:
        BanditAtA = -1
    elif event == 1:
        BomberAtA = 1
        BomberAtG = 1
    elif event == 2:
        RearOnly = True
    elif event == 3:
        Bump2Lead = True
    elif event == 4:
        CrewWound = True
    elif event == 5:
        HitDamage = 1
    elif event == 6:
        BomberFast = True
    elif event == 7:
        FlackDamage = -1
    elif event == 8:
        ReplaceBall = True
    else:
        BanditAttack2 = True
        
    EventSwitches = {"RearOnly": RearOnly,
                    "Bump2Lead": Bump2Lead,
                    "CrewWound": CrewWound,
                    "BomberFast": BomberFast,
                    "ReplaceBall": ReplaceBall,
                    "BanditAttack2": BanditAttack2
                    }
    EventDict = {"BanditAtA": BanditAtA,
                 "BomberAtA": BomberAtA,
                 "BomberAtG": BomberAtG,
                 "HitDamage": HitDamage,
                 "FLackDamage": FlackDamage,
                 "EventSwithces": EventSwitches
                 }
    return(EventDict)
        
    

