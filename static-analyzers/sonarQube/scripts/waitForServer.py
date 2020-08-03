import sys  
import requests 
import time 
import os
def printErrorMessage(message): 
   
    #stderr print
    print("**************************", file = sys.stderr)
    print("ERROR: " +  message, file = sys.stderr) 
    print("**************************", file = sys.stderr)   

def printNotiMessage(message):  
    print("**************************")
    print("NOTICE: " +  message) 
    print("**************************")   
 

waitTime = sys.argv[1] 



cycles = int(waitTime)/5 
printNotiMessage("Attemptign To Connect To SonarQube....")
while cycles > 0:  
    try:
        response = requests.get("http://localhost:9000/api/system/status")  
        if response.status_code == 200:  
            if response.json()["status"] == "UP": 
                printNotiMessage("SonarQube UP") 
                os._exit(0)  
            else: 
                printNotiMessage("Trying To Connect Agian To SonarQube...")
            
    except requests.exceptions.ConnectionError:  
        printNotiMessage("Trying To Connect Agian To SonarQube...")
        
    
    time.sleep(5) 
    cycles -=1  

printErrorMessage("SERVER TIMED OUT")
os._exit(1)  

