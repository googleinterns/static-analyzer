import shutil 
import Utils 
import os 
from Scheduler import Scheduler 

#makes the temp directory by either copying selected files or copying whole repo  


def start(): 
    #cloning repo and go into it   
    cloneRepo(location = "/home/aagubuzo/testsrc/src")
    os.chdir("temp")  

    #make schedule  
    scheduler = Scheduler() 
    scheduler.makeSchedule() 

    return "NTI"

#clones 
def cloneRepo(location): 
    try: 
        shutil.copytree(location, "temp")  
    except FileExistsError as excp:
        Utils.printErrorMessage(message="TEMP ALREADY EXISTES PLEASE RENAME OR DELETE") 
        exit(1) 
    except FileNotFoundError as excp: 
        Utils.printErrorMessage(message="PATH TO SRC DOSEN'T EXIST") 
        exit(1)
    except shutil.Error as excp: 
        Utils.printErrorMessage(message ="CHOULDN'T COPY FILES TO SCAN") 
        exit(1) 

    

        