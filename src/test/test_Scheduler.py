import unittest  
import os 
import sys 
import json   
from pathlib import Path  
import shutil
import io 
import difflib


ROOT_DIR = str(Path.home()) + "/staticAnaProj/"
SRC_DIR = ROOT_DIR +"/src"  
sys.path.append(SRC_DIR)


from Scheduler import Scheduler 
from Scheduler import Task  
import Utils

with open(ROOT_DIR + "/data/internalFile.json") as fp:  
            intFile = json.load(fp) 

RES_DIR = Utils.getProjRoot() + "test/testData/Test_Scheduler_data/"  

def printTestOutput(str): 
    print("TTT") 
    print(str) 
    print("TTT") 



class TestScheduler(unittest.TestCase): 

    def test_sucsessSch(self):  
        #initalize   
        os.chdir(Utils.getProjRoot() + "mem/testTemp") 
        
        scheduler = Scheduler(intFile)
        schedule = scheduler.makeSchedule() 
        
        #deinitilize   
        os.chdir(Utils.getProjRoot() + "bin")  

        result = set({schedule[1].toolName, schedule[0].toolName})
        expected = set({"Pylint","SonarQube"})

       
        #assert 
        assert expected == result 

    

    
if __name__ == '__main__': 
    unittest.main()