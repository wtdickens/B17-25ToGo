# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:33:13 2020

Main Program for B17 simulation

This program runs the B17 25 mission simulator

@author: wtdic
"""

from B17Data import Data
import B17io as io
from DetermineEvent import DetermineEvent
from B17Dice import d10()

# Get year for mission
year = io.GetInt(1942, 1944, "What year for your mission (1942-44")

# Load data for the mission year
DataDict = Data()

DataDict = playerSetUp(DataDict)

# Loop over 25 missions in game
for i in range(25):
    
    # Determine Mission Event
    EventResult = DetermineEvent()
    
    # Determine Bomber position in formation
    DataDict = DeterminePosition(EventResult, DataDict)
    
    # Determine position in formation
    skill = dataDict["BomberData"]["Skill"]
    positionRoll = d10() + skill
    if positionRoll <= 6:
        position = "middle"
    elif positionRoll <= 8:
        position = "rear"
    elif positionRoll <=1 10:
        position = "front"
    else:
        position = "lead"
        
    if eventData["Bump2Lead"]:
        position = "lead"
        
    dataDict["BomberData"]["Position"] = position
    
    # Determine encounters
    encounters = DetermineEcounter(year)
    
    
    ############################
    # Loop through encounters  #
    ############################
    
    for encounter in encounters:
        
        if encounter == "2Bandits":
            AttackResults, dataDict, shotDown = BanditAttack(year,
                                                             position,
                                                             EventResult, 
                                                             dataDict
                                                             )
            if eventDict["EventSwitches"]["BanditAttack2"]:
                AttackResults += "\n Oh no! He's looping and coming \
                                    back for another pass"
                AttackResults, dataDict, shotDown = BanditAttack(year,
                                                                position,
                                                                EventResult, 
                                                                dataDict
                                                                )
                
            AttackResults += "\nF%$#@# no! Here comes another!"
            io.Report(AttackResults)
            AttackResults, dataDict, shotDown = BanditAttack(year, 
                                                             position, 
                                                             EventResult, 
                                                             dataDict
                                                             )
            
            if eventDict["EventSwitches"]["BanditAttack2"]:  
                AttackResults += "\nJeez, they just aren't giving up today!"
                AttackResults, dataDict, shotDown = BanditAttack(year,
                                                                position,
                                                                EventResult, 
                                                                dataDict
                                                                )
            io.Report(AttackResults)
            
        elif encounter == "Bandit":
            AttackResults, dataDict, shotDown = BanditAttack(year, 
                                                             position, 
                                                             event, 
                                                             dataDict
                                                             )
            io.Report(AttackResults)
            
        elif encounter == "Flack":
            FlackResult, dataDict, shotDown = FlackAttack(DataDict)
            io.Report(FlackResult)
            
        elif encounter == "BombRun":
            BombResult, dataDict = BombRun(DataDict)
            io.Report(BombResult)
        
        if shotDown:
            break
        
    if shotDown:
        io.Report("That is the end of the war for you.")
        break
    if i < 25:
        dataDict = BetweenMissions(dataDict)
        
if not shotDown:    
    io.Report("Congratulations!/nYou completed 25 missions./nNow back \
              to the States to sell war bonds!")
            
            
            



