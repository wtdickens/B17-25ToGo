# -*- coding: utf-8 -*-
DetermineDamage(dataDict, returnText, EventDict):
    """
    Created on Sat Aug 22 15:37:43 2020
    When bomber is hit this determines the nature of the damage.
    
    Parameters
    ----------
    dataDict: dictionary
        Contains game data
        
    returnText: String
        Text account of events on current mission
    
    EventDict: dictionary
        Impacts from mission event
        
    Returns
    -------
    shotDown: boolean
        Was bomber shot down?
        
    returnText: String
        Text account of events on current mission
        
    dataDict: dictionary
        Contains game data

    @author: wtdic
    """

    shotDown = False
    # Determine where bomber was hit 
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
            if bomberData["DamageStatus"]["Frame"] != "OK":
                returnText += "We're going down! Hit the silk!\n"\
                        "...\n...\n...\n...\n...\n"                      \
                        "You land safely but are picked up by a German\n"\
                        "patrol and spend the rest of the war in a\n"    \
                        "prison camp"
                shotDown = True
                return(shotDown, returnText, dataDict)
            # If not damaged Frame damaged
            else:
                bomberData["DamageStatus"]["Frame"] = "damaged"
                returnText += "Wingsapr was hit bad, but it\n"  \
                                  "should hold for now."
                            
        # Engine Hit
        elif hitLocation == 9:
            engineDamage = bomberData["DamageStatus"]["Engine"]
            # If already damaged shot down
            if engineDamage != "OK":
                returnText += "Engines 3 and 4 gone\n "       \
                            "We're going down. Hit the silk!\n"       \ 
                            "...\n...\n...\n...\n...\n"               \
                            "You land safely and are picked up by\n"  \
                            "the underground who smuggle you into\n"  \
                            "Switerland where you spend the rest of\n"\
                            "the war."
                shotDown = True
                return(shotDown, returnText, dataDict)
            else:
                bomberData["DamageStatus"]["Engine"] = "damaged"
                returnText += "Engine 2's on fire! Blow the"   \
                            " extinguisher.\nFires out. Feather 2\n"   \
                            " we're good. Continue on course."
                            
        # Shot Down
        else:
            returnText += "Flames erupt all arount you. A wing" \
                        " has separated from the plane. The bomber "    \
                        " begins to spin maddly. You pass out.\n"       \
                        " Your war is over..."
            shotDown = True
            return(shotDown, returnText, dataDict)
                    
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
                            