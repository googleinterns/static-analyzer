import multiprocessing 
import time
import subprocess 
import os 
import shutil  
import Utils  
import sys


class Engine:  
    #TO-DO: 
        #implementing multi cmd calls (sonarQube server -> scanner) 


    #tried to avoid linux sepcific commands   

    def __init__(self,schedule):    
        self.__schedule = schedule 

    #Overall workflow of Enigne 
        #public interfacing function run 
        #for each task in schedule, makes a new process to run static analyzer on files  
        #exits when all processes are done 
    def run(self):

       #should be in repo right now 

        #run static analyzers 
        return self.__invokeTools(schedule=self.__schedule)

       
       


    #makes a process for each task and runs the task
    def __invokeTools(self, schedule):  
        #were tools invoked with no problem 
        sucsess = True

        procs = []    
        Utils.printNotiMessage("BOOTING STATIC ANALYZERS...") 

        for task in schedule: 
            #make and start new process
            
            p = multiprocessing.Process(target = self.__invokeTool(task=task))  
            p.start() 
            procs.append(p) 

    

        #wait for all threads to finish   
        for proc in procs: 
            proc.join()  

        for proc in procs: 
           if proc.exitcode != 0: 
                sucsess = False 
                break 

        Utils.printNotiMessage("SCANS DONE") 
        return sucsess

    #invokes the tool via provided command (absolute path)
    def __invokeTool(self, task): 
        Utils.printNotiMessage("RUNNING " + task.getToolName() + "...") 
        commands = task.getCommand() 

        for command in commands: 
            #potential security input check?? 
            retCode = subprocess.run(command,shell = True).returncode
            if (retCode != 0): 
                Utils.printErrorMessage(task.getToolName() +": SCAN FAILED; CHECK ITS LOGS") 
                self.terminate()

        
        if(retCode == 0):
            Utils.printNotiMessage(task.getToolName() + " SCAN SUCESSFUL") 
          
        