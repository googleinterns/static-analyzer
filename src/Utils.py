import sys 
import os 
import shutil 
import requests 
import time 
from pathlib import Path 

#Utils.py is a collection of fucntionalites commonly used throughout the program 

#prints error message to standard error  
#message is a string argument; the message that is supposed to be printed
def printErrorMessage(message): 
   
    #stderr print
    print("**************************", file = sys.stderr)
    print("ERROR: " +  message, file = sys.stderr) 
    print("**************************", file = sys.stderr)   

#prints notfication message to standard output 
#message is strign argument; the message that is supposed to be printed
def printNotiMessage(message):  
    print("**************************")
    print("NOTICE: " +  message) 
    print("**************************")   

#quits the program in an error state 
#message to print to standard error indicating why the exit happend; string argument 
#prints to stderr, preforms some clean up, and then exits with 1 exit code
def quitInError(message): 
    printErrorMessage(message)  

    #check if in temp or not and delete temp 
    if os.getcwd().split("/")[-1] == "temp": 
         os.chdir(os.path.dirname(os.getcwd())) 
         shutil.rmtree("temp") 
    os._exit(1)  

#returns the path of the root dirctory of the program
def getProjRoot():  
    return str(Path.home()) + "/staticAnaProj/" 

    

