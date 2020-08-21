# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:33:13 2020

Main Program for B17 simulation

This program runs the B17 25 mission simulator

@author: wtdic
"""
from B17Data import Data
import B17io as io
import DetermineEvent
from B17Dice import d10()

# Get year for mission
year = io.GetInt(1942, 1944, "What year for your mission (1942-44")

# Load data for the mission year
DataDict = Data()

# Loop over 25 missions in game
for i in range(25):
    
    # Determine Mission Event
    EventResult = DetermineEvent()
    
    # Determine Bomber position in formation
    DataDict = DeterminePosition(EventResult, DataDict)
    
    # Determine encounters
    encounters = DetermineEcounter(year)
    
    # Loop through encounters
    for encounter in encounters:
        
        if encounter == "2Bandits":
            AttackResults, dataDict, shotDown = BanditAttack(year, 
                                                             position, 
                                                             event, 
                                                             dataDict
                                                             )
            io.Report(AttackResults)
            AttackResults, dataDict, shotDown = BanditAttack(year, 
                                                             position, 
                                                             event, 
                                                             dataDict
                                                             )
            io.Report(AttackResults)
            
        elif encounter == "Bandit":
            io.Report(AttackResults)
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

if not shotDown:    
    io.Report("Congratulations!/nYou completed 25 missions./nNow back /
              to the States to sell war bonds!")
            
            
            



