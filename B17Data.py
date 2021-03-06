# -*- coding: utf-8 -*-
def Data():
    """
    Created on Sun Jul 26 13:35:41 2020

    This Routine initializes the data for the B17 simulation

    Parameters
    ----------
    none

    Returns
    -------
    DataDict : Python dictionary
        This dictionary contains the data for the simulation for 
        the given year

    @author: wtdic
    """
    # Bandit Data
    banditType = {1 : "BF-109",
                  2 : "BF-109",
                  3 : "BF-109",
                  4 : "FW-190",
                  5 : "FW-190",
                  6 : "FW-190",
                  7 : "BF-110",
                  8 : "BF-110",
                  9 : "ME-410",
                  10 : "ME-410"
                  }

    banditAtA = {"BF-109": 8,
                 "FW-190": 6,
                 "Bf-110": 9,
                 "ME-410": 7
                 }

    # Celebration text
    celebrate = {1: "YeeeeHaw! Smoked em!",
                 2: "I got him! I got him!",
                 3: "Gerry is popping silk!",
                 4: "{} Trailing smoke! I got him.",
                 5: "Scratch one {}!",
                 6: "YES!\nAnother swastika for the nose",
                 7: "Oh Yea! Say goodbye Gerry!",
                 8: "Got 'em! One less Nazi prick",
                 9: "Bandit down.",
                 10: "Whew! Got 'em"
                 }

    # Bomber Data
    ata = {"Front": 9,
           "Port": 8,
           "Starboard": 8,
           "Rear": 7
           }

    damageStatus = {"Engine": "OK", "Frame": "OK"}

    crewStatus = {1: "healthy",
                  2: "healthy",
                  3: "healthy",
                  4: "healthy",
                  5: "healthy",
                  6: "healthy",
                  7: "healthy",
                  8: "healthy",
                  9: "healthy",
                  10: "healthy"
                  }

    crewNickNames = {1: "Captain",
                     2: "Lieutenant",
                     3: "WrongWay",
                     4: "Dropper",
                     5: "Tops",
                     6; "Sparks",
                     7: "Lucky",
                     8: "Fats",
                     9: "Cooler",
                     10: "Aces"
                     }

    crewNames = {1: "Wilson",
                 2: "Johnson",
                 3: "Batelle",
                 4: "Dickens",
                 5: "Finnegan",
                 6: "Broadrick",
                 7: "Dubeck",
                 8: "Miller",
                 9: "Jones",
                 10: "O'Leary"
                 }

    crewPositions = {1: "Pilot",
                     2: "Co-pilot",
                     3: "Navigator",
                     4: "Bombardier",
                     5: "Engineer",
                     6: "Radio Operator",
                     7: "Ball Gunner",
                     8: "Port Waist Gunner",
                     9: "Stbd. Waist Gunner",
                     10: "Tail Gunner"
                     }

    hitLocations = {1: "the side",
                    2: "the top",
                    3: "the floor",
                    4: "the tail feathers",
                    5: "my canteen",
                    6: "the turret",
                    7: "the windscreen",
                    8: "the wing",
                    9: "the ailerons",
                    10: "an empty ammo case"
                    }

    bomberData = {"Skill": -2,
                  "AtG": -2,
                  "AtA": ata,
                  "Tactics": [],
                  "Position": "middle",
                  "DamageStatus": damageStatus,
                  "CrewStatus": crewStatus,
                  "CrewNickNames": crewNickNames,
                  "CrewNames": crewNames,
                  "CrewPositions": crewPositions,
                  "HitLocations": hitLocations,
                  }

    DataDict = {"BanditType" : banditType,
                "BanditAtA": banditAtA,
                "Celebrate" : celebrate,
                "BomberData" : bomberData
                }
