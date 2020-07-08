import multiprocessing 
import time
import subprocess 
import os 
import shutil 

class Engine:   

    def __init__(self, location, schedule):    
        self.location = location 
        self.schedule = schedule 


    def initialize(self):

        curr = shutil.copytree(self.location, "temp") 
        print(os.listdir("temp"))  
        os.chdir("temp")
        print("calling sonar...")  
        subprocess.run([os.environ["SONAR_SCAN"]])  
        os.chdir(os.path.dirname(os.getcwd()))  
        shutil.rmtree("temp")

        #go to repo 
        #clone repo  
        #go into clone repo  
        #call invokeTools 



    def invokeTools(self, schedule):
        procs = []   
        print("run sonarqube") 
        subprocess.run([os.environ["SONAR_SCAN"]])  
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
        