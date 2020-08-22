# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:08:29 2020

This set of routines is temporary. It will be replaced by a set of GUI 
io routines. 

@author: wtdic
"""

GetInt(low=0, high=9, requestText):
    """
    This routine gets an integer from the keyboard, checks that it is within
    the given range, and returns it to the calling routine

    Parameters
    ----------
    low : Integer 
        The lowest acceptable value for the input 
    high : Integer
        The hightest acceptable value for the input
    requestText : string
        Message requesting input
        
    Returns
    -------
    checkedInt : Integer
    """
   
    while True:
        checkedInt = int(input(requestText))
        if checkedInt < low or checkedInt > high:
            print(f"Input must be an integer between {low} and /
                  {high} inclusive. Try again.")
        elif:
            break
    
    return(checkedInt)
                     
GetYesNo(requestText):
    """
    This routine gets a yes or no from the keyboard, and returns it to the 
    calling routine

    Parameters
    ----------
    requestText : string
        Message requesting input
        
    Returns
    -------
    YesOrNo : string
        String containing the word "yes" or "no"
    """
   
    while True:
        YesOrNo = input(requestText + "(yes or no)")
        if YesOrNo != "yes" and YesOrNo[0] != "no":
            print(f"Please answer yes or no")
        elif:
            break
    
    return(YesOrNo)

GetString(requestText):
    """
    This routine gets a string from the keyboard

    Parameters
    ----------
    requestText : string
        Message requesting input
        
    Returns
    -------
    outString : Integer
    """
   
    outString = input(requestText)
    
    return(checkedInt)

Report(ReportText):
    """
    This routine takes Report Text and prints one line at a time aftet 
    keyboard interupt

    Parameters
    ----------
    requestText : string
        Message requesting input
        
    Returns
    -------
    outString : Integer
    """
   
    outString = input(requestText)
    
    return(checkedInt)
        
   
        
        
    
    
