# -*- coding: utf-8 -*-
playerSetUp(dataDict):
    """
    Created on Sat Aug 22 15:41:46 2020
    
    This routine shows the player the names of the crew and allows the
    player to change the names.
    
    Parameters
    ----------
    dataDict: Dictionary
        Dictionary containing all the data for the simulation
        
    Returns
    -------
    dataDict: Dictionary
        Dictionary containing all the data for the simulation
        
    @author: wtdic
    """
    import B17io as io
    
    print("Welcome commander, here is your crew, their positions and\n\
          nicknames. Let me know if you want to change any of these")
          
      bomberData = dataDict["BomberData"]

    print("     Position         Name      Nickname")
    for i in range(10):
        print(f"{i}:3 {bomberData['crewPosition'[i]:18} \
              {bomberData['crewNames'][i]:10}
              {bomberData['crewNickNames'][i]:12}
              )
            
    changeNamesA = io.getYesNo("Do you want to change any names or Nicknames?")
    
    if changeNamesA == "yes":
        while True:
            crewNumber = io.GetInt(1, 10, "Enter number of crewmember \
                                   whose name you want to change")
            nameOrNick = io.GetInt(1, 2, " Change name (1) or Nickname (2)?")
           
            if nameOrNick == 1:
               handle = "crewNames"
            else:
               handle = "crewNickNames"
           
            bomberData[handle][crewNumber] = io.getString("What is new name?")
            
            if "no" == io.getYesNo("Change more names?"):
                break
            
    dataDict["BomberData"] = bomberData
    
    return(dataDict)
    
