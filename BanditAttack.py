# -*- coding: utf-8 -*-
def BanditAttack(year, position, event,dataDict)
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
event: python integer (1-10)
    The number of the event for mission
dataDict : Python dictionary
    dictionary containing data used in simulation

Returns
-------
outcome : python string
    Text message describing the outcome
    
dataDict : python dictionary
    updated data dictionary
    
shotDown : python Boolean
    was bomber shot down?

@author: wtdic
"""
from B17Dice import d10
from crewFires import bomberFires
from banditFires import banditFires

# Extract Bomber Data dictionary
bomberData = DataDict["BomberData"]

# Extract Damage status
engineStatus = bomberData["DamageStatus"]["Engine"]
frameStatus = bomberData["DamageStatus"]["Frame"]
if engineStatus == "OK" and frameStatus == "OK":
    damageStatus = "undamaged"
else:
    damageStatus = "damaged"
shotDown = False

# Determine if attack on bomber takes place
# Find modifier for bandit attack on plane
modifier = 0  
if year == 1942:  # Modify for year
    modifier = -2
elif year == 1944:
    modifier = -1
damageStatus != "undamaged":  # Modify for damaged status
    modifier += 5
 
position = bomberData["Position"] # Modify for position in formation
if position == "lead":
    modifier += 3
elif position == "front":
    modifier += 2
elif position == "rear"
    modifier += 1

roll = d10() + modifier() # Modified die roll

if roll < 8:  # No attack
    # No bandit attack. Return safe text.
    return("OK\nBomber Group wards off attack. You are safe for now.")
else:
    # Bomber is attacked.  Compute Results.
    
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
    if roll < 4 or event == 3:
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
    if d10() + modifier >= 8 or event == 7:
        fastQ = True
        returnText += "RATATATATATATAATATATATATAT\n"
    else:
        fastQ = False
        returnText += "[Tracer fire whips past the cockpit]\n}"
    
    # Determine outcome
        
    # If bomber crew is fast
    # Bomber crew fires first
    if fastQ:
        banditStatus, returnText = bomberFires(position,
                                               event,
                                               banditDefense,
                                               bomberData, 
                                               returnText,
                                               dataDict)
        
    # Bandit fires if crew is slow
    else:
        returnText = banditFires(position,
                                 event,
                                 bomberData
                                 returnText,
                                 dataDict)
        returnText += "[Tracer fire whips past the cockpit]\n}"
        # Determine bandit to hit number
        banditAtA = dataDict["BanditData"][banditType]
        if year == 1942: # Add year modifier
            banditAtA -= 1
        elif year == 1944:
            banditAtA += 1
                
        if event == 1: # Apply event modifier
            banditAtA += 1
        elif event == 2:
            banditAtA -= 1
        
        # Results of bandid fire
        # Miss
        if d10() < banditAtA:  # Miss
            returnText += "OK\nWhew that was close!\n"
            
        # Hit   
        else:  
            whoHit = d10()
            returnText += "We're hit! We're hit!\n"
            hitLocation = d10()
            
            # Hit other than crew member
            if hitLocaation <= 3 or hitLocation > 7:
                returnText += "Damage report!\n"
                
                # Superficial damage
                if hitLocaation <=3:
                    returnText +=("Nothing serious. Just some holes in "
                                  + bomberData["HitLocations][hitLocation])
                
                # Frame Damage
                elif hitLocation == 8:
                    # If already damaged shot down
                    if bomberData["DamageStatus"]["Frame"] == "damaged":
                        returnText += "We're going down! Hit the silk!\n"\
                        "...\n...\n...\n...\n...\n"                      \
                        "You land safely but are picked up by a German\n"\
                        "patrol and spend the rest of the war in a\n"    \
                        "prison camp"
                        return("Shot Down\n" + returnText)
                    # If not damaged Frame damaged
                    else:
                        bomberData["DamageStatus"]["Frame"] = "damaged"
                        returnText += "Wingsapr was hit bad, but it"  \
                            " should hold for now."
                            
                # Engine Hit
                elif hitLocation == 9:
                    if bomberData["DamageStatus"] == "enginedamage":
                        returnText += "Engines 3 and 4 gone\n "       \
                            "We're going down. Hit the silk!\n"       \ 
                            "...\n...\n...\n...\n...\n"               \
                            "You land safely and are picked up by\n"  \
                            "the underground who smuggle you into\n"  \
                            "Switerland where you spend the rest of\n"\
                            "the war."
                            return("Shot Down/n" + returnText)
                    else:
                        bomberData["DamageStatus"]
                        returnText += "Engine 2's on fire! Blow the"   \
                            " extinguisher.\nFires out. Feather 2\n"   \
                            " we're good. Continue on course."
                            
                # Shot Down
                else:
                    returnText += "Flames erupt all arount you. A wing" \
                        " has separated from the plane. The bomber "    \
                        " begins to spin maddly. You pass out.\n"       \
                        " Your war is over..."
                        return("Shot Down/n" + returnText)
                    
            # Already wounded/killed crew member is hit
            elif bomberData["CrewStatus"][whoHit] != "healthy":
                returnText += "Whoa that was close. Bullet just missed"
                
            # Crew member wounded
            else:
                returnText += "I'm hit!\n"
                
                # Pilot is hit
                if whoHit == 1:
                    returnText += "Co-Piolot: It's the captain." \
                    " I'm taking over."
                    bomberData["Tactics"] = []
                    if event == 5:
                        bomberData["CrewStatus"][1] = "wounded"
                    else:
                        bomberData["CrewStatus"][1] = KIA
                        returnText += ("Co-pilot: Pilot's hit.
                                       I'm taking over\n")
                            returnText += "[No more tactics]\n"
                        if event == 5:
                            bomberData["CrewStatus"][1] = "wounded"
                        else:
                            bomberData["CrewStatus"][1] = "KIA"
                            bomberData["Tactics"] = []
                            
                # Other crew is hit
                else: 
                    returnText += ("It's "+
                                   BomberData["CrewNickName"][whoHit])
                    returnText += ("\n[Position: " 
                                   + bomberData["CrewPositions"][whoHit]
                                   + "]"/n)
                    if event == 5:
                        returnText += "It's not bad. He'll be OK\n"
                        bomberData["CrewStatus"][whoHit] = "wounded"
                    else:
                        returnText += ("He's a mess. I don't think he'll
                                       make it.\n")
                        bomberData["CrewStatus"][whoHit] = "KIA"
                            
                    # Crew hit consequences
                    if whoHit == 3:
                            bomberData["AtA"]["Front"] += 1
                    elif whoHit == 4:
                            bomberData["AtG"] = -2
                    elif whoHit == 5:
                            bomberData["AtA"]["Front"] +=1
                    elif whoHit == 7:
                            bomberData["AtA"]["Port"] += 1
                            bomberData["AtA"]["Starboard"] += 1
                    elif whoHit == 8:
                            bomberData["AtA"]["Port"] = 8
                    elif whoHit == 9:
                            bomberData["AtA"]["Starboard"] = 8
                    elif whoHit == 10:
                            bomberData["AtA"]["Rear"] = 7
                            
                        
                            
                            
                                           
                            
                            
    




