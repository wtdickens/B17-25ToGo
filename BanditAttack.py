# -*- coding: utf-8 -*-
def BanditAttack(year, position, eventDict, dataDict):
    """
    Created on Sun Jul 26 13:44:49 2020

    This routine computes the outcome of a bandit attack
    on the formation the bomber is in

    Parameters
    ----------
    year : python integer (1942-44)
        The year the action is taking place
    position : string
        Position of the bomber in the formation (middle, front, rear, lead)
    eventDict: python dictionary
        Dictionary containing the adjustments due to the event
    dataDict : Python dictionary
        dictionary containing data used in simulation

    Returns
    -------
    outcome :  string
        Text message describing the outcome
    
    dataDict :  dictionary
        updated data dictionary
    
    shotDown :  Boolean
        was bomber shot down?

    @author: wtdic
    """
    from B17Dice import d10
    from crewFires import bomberFires
    from BanditFires import banditFires

    # Extract Bomber Data dictionary
    bomberData = DataDict["BomberData"]
    bomberFast = eventDict["EventSwitches"]["BomberFast"]

    # Extract Damage status
    engineStatus = bomberData["DamageStatus"]["Engine"]
    frameStatus = bomberData["DamageStatus"]["Frame"]
    if engineStatus == "OK" and frameStatus == "OK":
        damageStatus = "undamaged"
    else:
        damageStatus = "damaged"
    
    # Set shot Down status to false    
    shotDown = False

    #############################################
    # Determine if attack on bomber takes place #
    #############################################
    
    # Find modifier for bandit attack on plane
    modifier = 0  
    if year == 1942:  # Modify for year
        modifier = -2
    elif year == 1944:
        modifier = -1
    
    if damageStatus == "damaged":  # Modify for damaged status
        modifier += 4
     
    # Modify for position in formation
    if position == "lead":
        modifier += 3
    elif position == "front":
        modifier += 2
    elif position == "rear"
        modifier += 1

    roll = d10() + modifier() # Modified die roll

    if roll < 8:  # No attack
        # No bandit attack. Return safe text.
        return("OK\nBomber Group wards off attack.\nYou are safe for now.")
    else:
        #########################################
        # Bomber is attacked.  Compute Results. #
        #########################################
    
        # Find Bandit Type
        banditType = dataDict["BanditType"][d10()]
        banditDefense = dataDict["BanditDefense"][banditType]
        returnText = banditType
    
        # Determine direction of attack
        if position == "front": # Modifier depending on position in formation
            modifier = 2
        elif position == "lead":
            modifier = 3
        elif position == "rear":
            modifier = -2
        else:
            modifier = 0
                
        roll = modifier + d10() # Roll for direction
        
        if roll < 4 or eventDict["EventSwitches"]["ReadOnly"]:
            attackDirection = "rear"
            returnText += " Bandit! 6 O'clock!\n"
        elif roll <6:
            attackDirection = "port"
            returnText += " Bandit! 9 O'clock!\n"
        elif roll < 8:
            attackDirection = "starboard"
            returnText += " Bandit! 3 O'clock!\n"
        else:
            attackDirection = "front"
            returnText += " Bandit! 12 O'clock!\n"
    
        # Determine if crew is fast
        modifier = bomberData["Skill"]
        # Check if bomber fires first due to skill or bomber fast event
        if d10() + modifier >= 8 or bomeberFast:
            fastCrew = True
            returnText += "RATATATATATATAATATATATATAT\n"
        else:
            fastCrew = False
            returnText += "[Tracers whip past the cockpit]\n}"
        
        #####################
        # Determine outcome #
        #####################
        
        # If bomber crew is fast
        # Bomber crew fires first
        if fastCrew:
            banditStatus, returnText = bomberFires(position,
                                                   event,
                                                   banditDefense,
                                                   bomberData, 
                                                   returnText,
                                                   dataDict
                                                   )
            if banditStatus = "OK":
                shotDown, returnText, dataDict = banditFires(position,
                                                             eventData,
                                                             returnText,
                                                             dataDict
                                                             )
        
        # Bandit fires if crew is slow
        else:
            shotDown, returnText, dataDict = banditFires(position,
                                                         eventData,
                                                         returnText,
                                                         dataDict
                                                         )
            if not shotDown:
                banditStatus, returnText = bomberFires(position,
                                                       event,
                                                       banditDefense,
                                                       bomberData, 
                                                       returnText,
                                                       dataDict
                                                       )
        
            

                            
                                           
                            
                            
    




