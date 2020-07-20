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

    def __init__(self,schedule, intFile):    
        self.__schedule = schedule  
        self.__intFile = intFile

    #Overall workflow of Enigne 
        #public interfacing function run 
        #for each task in schedule, makes a new process to run static analyzer on files  
        #exits when all processes are done 
    def run(self):

       #should be in repo right now 

        #run static analyzers 
        status =self.__invokeTools(schedule=self.__schedule) 

        for task in self.__schedule:  
            if task.status == False: 
                Utils.printErrorMessage(task.getToolName() + " SCAN FAILED: CHECK ITS LOGS") 
            else: 
                Utils.printNotiMessage(task.getToolName() + " SCAN SUCESSFUL") 

        return status 

       
       


    #makes a process for each task and runs the task
    def __invokeTools(self, schedule):  
        #were tools invoked with no problem 
        sucsess = True

        procs = []     
        Utils.printNotiMessage("BOOTING STATIC ANALYZERS...") 

        for task in schedule: 
            #make and start new process
            
            p = multiprocessing.Process(target = self.__invokeTool, args= (task,))   
            
            p.start() 
            procs.append(p)  
        
        Utils.printNotiMessage("RUNNING ALL STATIC ANALYZERS")

    

        #wait for all threads to finish   
        for proc in procs: 
            proc.join()  
 
        #check for sucsess and failures 
        index = 0
        for proc in procs:   
            if proc.exitcode != 0: 
                sucsess = False  
                schedule[index].status = False
            index += 1 


        Utils.printNotiMessage("SCANS DONE") 
        return sucsess

    #invokes the tool via provided command (absolute path)
    def __invokeTool(self, task):  
        Utils.printNotiMessage("RUNNING " + task.getToolName() + "...") 
        commands = task.getCommand()  
       

        for command in commands: 
            #potential security input check?? 
            with open(self.__intFile["tools"][task.getToolName()]["output"], "w") as output:  
                with open(self.__intFile["tools"][task.getToolName()]["error"], "w") as errOutput:
                    retCode = subprocess.run(command,shell = True,stdout=output, stderr=errOutput).returncode
            if (set(self.__intFile["tools"][task.getToolName()]["sucRetCodes"]).__contains__(retCode) == False ): 
                print(task.getToolName() + " " + str(retCode)) 
                os._exit(1)
        
       
          
        