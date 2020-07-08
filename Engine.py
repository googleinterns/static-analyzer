import multiprocessing 
import time
import subprocess

class Engine: 

    def invokeTools(self, schedule):
        procs = []  
        subprocess.run(["cd", "~/sonarqube-8.3.1.34397/bin/linux-x86-64"])  
        suborocess.run(["./sonar.sh"])
        for task in schedule: 
            #make new process 
            #call invokeTool(task) in process 
            # start process  
            #add process into array 
            print("invoking static analyzers...")
            p = multiprocessing.Process(target = self.invokeTool(task=task))  
            p.start() 
            procs.append(p) 

    

        #wait for all threads to finish   
        for proc in procs: 
            proc.join() 

        print("scans done")

    def invokeTool(self, task): 
        print("calling tool " + task + "...")  
        time.sleep(1)  
       
        print("tool " + task + " is done")