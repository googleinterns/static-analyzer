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


from Engine import Engine  
from Scheduler import Task  
import Utils

with open(ROOT_DIR + "/data/internalFile.json") as fp:  
            intFile = json.load(fp) 

RES_DIR = Utils.getProjRoot() + "test/testData/Test_Engine_data/"  

def printTestOutput(str): 
    print("TTT") 
    print(str) 
    print("TTT") 



           

class TestEngine(unittest.TestCase): 

    def test_successRun(self):  
        #initalize   
        shutil.copytree(Utils.getProjRoot() + "test/src" , Utils.getProjRoot() + "data/temp")
        os.chdir(Utils.getProjRoot() + "data/temp") 
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput

        engine = Engine([Task(toolName ="SonarQube", command = ["../../static-analyzers/sonarQube/sonarqube-8.3.1.34397/bin/linux-x86-64/sonar.sh start",
                                "python3 ../../static-analyzers/sonarQube/scripts/waitForServer.py 300", 
                                "../../static-analyzers/sonarQube/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner"], 
                                method = "NIL",requestCommands = "NIL", sucRetCodes=[0,1],output="NIL", error="NIL",
                                mapping={}),
                                Task(toolName = "Pylint", command= ["pylint temp --output-format=json"], 
                                method = "NIL",requestCommands = "NIL", sucRetCodes=[0,16,22],output="NIL", error="NIL",
                                mapping={})],intFile) 
        engine.run() 

           

        #deinitilize   
        sys.stdout = sys.__stdout__
        os.chdir(Utils.getProjRoot() + "bin")  
        shutil.rmtree(Utils.getProjRoot() + "data/temp")  

        #assert 
        with open(RES_DIR + "test_successRun.txt") as expected:  
            assert expected.read().strip() == capturedOutput.getvalue().strip() 

    def test_failSQPassPLRun(self):  
        #initalize   
        shutil.copytree(Utils.getProjRoot() + "test/src" , Utils.getProjRoot() + "data/temp")
        os.chdir(Utils.getProjRoot() + "data/temp") 
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput

        engine = Engine([Task(toolName ="SonarQube", command = ["BAD COMMAND"], 
                                method = "NIL",requestCommands = "NIL", sucRetCodes=[0,1],output="NIL", error="NIL",
                                mapping={}),
                                Task(toolName = "Pylint", command= ["pylint temp --output-format=json"], 
                                method = "NIL",requestCommands = "NIL", sucRetCodes=[0,16,22],output="NIL", error="NIL",
                                mapping={})],intFile)
        engine.run() 

           

        #deinitilize   
        sys.stdout = sys.__stdout__
        os.chdir(Utils.getProjRoot() + "bin")  
        shutil.rmtree(Utils.getProjRoot() + "data/temp")  

        
        #assert 
        with open(RES_DIR + "test_failSQPassPLRun.txt") as expected:  
            assert expected.read().strip() == capturedOutput.getvalue().strip() 

    def test_failBothSARun(self):  
        #initalize   
        shutil.copytree(Utils.getProjRoot() + "test/src" , Utils.getProjRoot() + "data/temp")
        os.chdir(Utils.getProjRoot() + "data/temp") 
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput

        engine = Engine([Task(toolName ="SonarQube", command = ["BAD COMMAND"], 
                                method = "NIL",requestCommands = "NIL", sucRetCodes=[0,1],output="NIL", error="NIL",
                                mapping={}),
                                Task(toolName = "Pylint", command= ["BAD COMMAND"], 
                                method = "NIL",requestCommands = "NIL", sucRetCodes=[0,16,22],output="NIL", error="NIL",
                                mapping={})],intFile)
        engine.run() 

           

        #deinitilize   
        sys.stdout = sys.__stdout__
        os.chdir(Utils.getProjRoot() + "bin")  
        shutil.rmtree(Utils.getProjRoot() + "data/temp") 

        #assert 
        with open(RES_DIR + "test_failBothSARun.txt") as expected:  
            assert expected.read().strip() == capturedOutput.getvalue().strip() 

    
    

    def test_emptySch(self):  
        #initalize   
        shutil.copytree(Utils.getProjRoot() + "test/src" , Utils.getProjRoot() + "data/temp")
        os.chdir(Utils.getProjRoot() + "data/temp") 
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput

        engine = Engine([],intFile) 
        engine.run() 
       

        #deinitilize   
        sys.stdout = sys.__stdout__
        os.chdir(Utils.getProjRoot() + "bin")  
        shutil.rmtree(Utils.getProjRoot() + "data/temp") 

        
        
        #assert 
        with open(RES_DIR + "test_emptySch.txt") as expected:  
            assert expected.read().strip() == capturedOutput.getvalue().strip()

if __name__ == '__main__': 
    unittest.main()