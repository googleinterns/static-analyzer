import sys 
import os 
import shutil 
import requests 
import time
#need an error exit protocal (deleets temp)
def printErrorMessage(message): 
   
    #stderr print
    print("**************************", file = sys.stderr)
    print("ERROR: " +  message, file = sys.stderr) 
    print("**************************", file = sys.stderr)   

def printNotiMessage(message):  
    print("**************************")
    print("NOTICE: " +  message) 
    print("**************************")   

def quitInError(message): 
    printErrorMessage(message)  

    #check if in temp or not and delete temp 
    if os.getcwd().split("/")[-1] == "temp": 
         os.chdir(os.path.dirname(os.getcwd())) 
         shutil.rmtree("temp") 
    os._exit(1)
    
def waitForServer(url,waitTime):  
    cycles = int(waitTime)/5 

    while cycles > 0:  
        try:
            status = requests.get(url).status_code    
            if status == 200: 
                printNotiMessage("SERVER UP") 
                return 
        except requests.exceptions.ConnectionError: 
            printNotiMessage("Trying To Connect Agian To Server...")
        
    
        time.sleep(5) 
        cycles -=1  

    printErrorMessage("SERVER TIMED OUT")
    os._exit(1) 
