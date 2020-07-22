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
        #instead   of paassing inn int ffiel I can puuuut ouutput and eerr files in tasll


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
        if(len(self.__schedule) > 0):
            status =self.__invokeTools(schedule=self.__schedule) 
        else: 
            Utils.printNotiMessage("NO SCANS MADE; IS THERE SRC CODE???")   
            return 

        for task in self.__schedule:  
            if task.status == False: 
                Utils.printErrorMessage(task.toolName + " SCAN FAILED: CHECK ITS LOGS") 
            else: 
                Utils.printNotiMessage(task.toolName + " SCAN SUCESSFUL") 

        if status == False:
             Utils.printNotiMessage("ALL SCANS WERE NOT SUCSESSFUL") 
        else: 
            Utils.printNotiMessage("ALL SCANS WERE SUCSESSFUL") 


       
       


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
            Utils.printNotiMessage("RUNNING " + task.toolName + "...") 
            procs.append(p)  
        
       

    

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
        commands = task.command  
       

        for command in commands: 
            #potential security input check?? 
            with open(Utils.getProjRoot() + task.output, "w") as output:  
                with open(Utils.getProjRoot() + task.error, "w") as errOutput:
                    retCode = subprocess.run(command,shell = True,stdout=output, stderr=errOutput).returncode
            if (set(task.sucRetCodes).__contains__(retCode) == False ): 
                #print(task.toolName + " " + str(retCode)) 
                os._exit(1)
        
       
          
        
