import multiprocessing 
import time
import subprocess 
import os 
import shutil  
import Utils  
import sys 
import re

#The Engine class is responsible for invoking the scans of the appropiate static analyzers  
#Its constructor takes in a schedule which is a list of task objects; (Task objects are defined in schedule.py) 
#The Engine parallely invokes each of the static analyzers associated with a task in the schedule, these static analyzers are called on the 
#current working directory of the process
class Engine:  
    
    def __init__(self,schedule):    
        self.__schedule = schedule  


    #The run function is the public interfacing function of Engine 
    #It processes the schedule, executes the static analyzers, and communicates status 
    def run(self):

        #run static analyzers  
        if(len(self.__schedule) > 0):
            status =self.__invokeTools(schedule=self.__schedule) 
        else: 
            #is there compaatible src code
            Utils.printNotiMessage("NO SCANS MADE; IS THERE SRC CODE???")   
            return

        #notify user about the static analyzers that failed or succsseded 
        for task in self.__schedule:  
            if task.status == False: 
                Utils.printErrorMessage(task.toolName + " SCAN FAILED: CHECK ITS LOGS") 
            else: 
                Utils.printNotiMessage(task.toolName + " SCAN SUCCESSFUL") 

        if status == False:
             Utils.printNotiMessage("ALL SCANS WERE NOT SUCCESSFUL") 
        else: 
            Utils.printNotiMessage("ALL SCANS WERE SUCCESSFUL") 


    #private function for the execution of the static analyzers associated with the task in schedule 
    #the fucntion takes in the same schedule that was provided via the constructor 
    #for each task in the schedule a process is made to execute the commands regarding the analyzer described in the task object
    def __invokeTools(self, schedule):  
        #boolean used to keep track of execution succsess
        success = True

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
 
        #check for success and failures and indicate it in task object
        index = 0
        for proc in procs:   
            if proc.exitcode != 0: 
                success = False  
                schedule[index].status = False
            index += 1 


        Utils.printNotiMessage("SCANS DONE") 
        return success

    #private function that invokes the analyzer associated with provided task 
    #the function takes in a task object (defined in scheduler.py) which describes a task involving a static analyzer 
    #The function executes the series of commands provided by the task object invokeCommands attribute and redirects the stdout and 
    #stderr of the execution to the corresponding files also delinated on the task object. It finally returns the exit code of the executions 
    def __invokeTool(self, task): 

        commands = task.command  
       
        for command in commands: 
            #potential security input check?? 
            with open(Utils.getProjRoot() + task.output, "w") as output, open(Utils.getProjRoot() + task.error, "w") as errOutput: 
                    #execute command in invokeCommands list and store exit code
                    retCode = subprocess.run(command,shell = True,stdout=output, stderr=errOutput).returncode 
            #determine wether the exit code maps to succsessful execution 

            if  re.match(task.sucRetCodes, str(retCode)) == None:
                #print(task.toolName + " " + str(retCode)) 
                # if failed execution then kill the process running the task 
                os._exit(1)
        
       
          
        
