import shutil 
import Utils 
import os  
import json  
import sys 
import re
from Scheduler import Scheduler  
from Engine import Engine 
from ReportReader import ReportReader

#ToDO 
    #file directory organization (static analyzer scanners in a folder)
    #-l listing option 
#makes the temp directory by either copying selected files or copying whole repo  
# 




def start():   
    #process arugments 
    processArgs()  

    #temp src file will be set up by the time 
    #process arguments returns 
     

    #open internal file and turn it ot json object 
    with open("../data/internalFile.json","r") as fp:  
            intFile = json.load(fp)    

    os.chdir("../mem/temp")


    #make schedule  
    scheduler = Scheduler(intFile= intFile) 
    schedule = scheduler.makeSchedule()   
     
    #runs engine  
    engine = Engine(schedule) 
    engine.run()  

    #generate report 
    reportReader = ReportReader(schedule=schedule,intFile=intFile)
    print(reportReader.parseReports())

    


    #delete repo when processes and scans are done 
    os.chdir(os.path.dirname(os.getcwd()))  
    shutil.rmtree("temp")


    return "NTI"

    

def processArgs():
    args = sys.argv  
    args.pop(0) 
    map = {}  
    filesProvided = False
    
    
    #create mapping between options and its list of arguments  
    currOpt = "" 
   
    for arg in args: 
        if re.match("^-",arg):  
            map[arg] = []  
            currOpt = arg 
        else: 
            map[currOpt].append(arg) 
    
    #functional cases if arguments exist; should be added onto if more options/args are beign deved  
    options = list(map) 
    for opt in options: 
        if opt == "-r":  
            if(filesProvided == True): 
                Utils.printErrorMessage("CAN'T USE BOTH REPO(-r) AND LIST(-l) OPTIONS") 
                exit(1)
            repoOptionFunc(map["-r"])  
            filesProvided = True #indicates wether or not src files were prodvided for scan 
        elif opt == "-l":  
            if(filesProvided == True): 
                Utils.printErrorMessage("CAN'T USE BOTH REPO(-r) AND LIST(-l) OPTIONS") 
                exit(1) 
            listOptionFunc(map["-l"]) 
            filesProvided = True 
        
    
    if filesProvided == False: 
        Utils.printErrorMessage("PLEASE PROVIDE SRC FILES USING -r OR -l")  
        exit(1)









#functions for different options and their args 
#wanted to keep the fucntions sepreate for logical organization and ease of arg extention  
def repoOptionFunc(location):  
    #cloning repo provided by location    
    try: 
        shutil.copytree(location[0], "../mem/temp")  
    except FileExistsError as excp:
        Utils.printErrorMessage(message="TEMP ALREADY EXISTES PLEASE RENAME OR DELETE") 
        exit(1) 
    except FileNotFoundError as excp: 
        Utils.printErrorMessage(message="PATH TO SRC DOSEN'T EXIST") 
        exit(1)
    except shutil.Error as excp: 
        Utils.printErrorMessage(message ="CHOULDN'T COPY FILES TO SCAN") 
        exit(1)  

def listOptionFunc(list):   
    return "nil"

start()
     

    

    

        