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


from ReportReader import ReportReader  
from Scheduler import Task  
import Utils

with open(ROOT_DIR + "/data/internalFile.json") as fp:  
            intFile = json.load(fp) 

RES_DIR = Utils.getProjRoot() + "test/testData/Test_ReportReader_data/"  

def printTestOutput(str): 
    print("TTT") 
    print(str) 
    print("TTT") 



class TestReportReader(unittest.TestCase): 

    def test_successRead(self):  
        #initalize   
        shutil.copytree(Utils.getProjRoot() + "test/src" , Utils.getProjRoot() + "data/temp")
        os.chdir(Utils.getProjRoot() + "data/temp") 
        
        reportReader = ReportReader([
                                Task(toolName = "Pylint", command= ["pylint temp --output-format=json"], 
                                method = "FILE",requestCommands = [ 
                                                                "../../test/testData/Test_ReportReader_data/pylint_sample_report.json"], 
                                                sucRetCodes=[0,16,22],output="NIL", error="NIL",
                                                mapping={})],intFile)

        result = reportReader.parseReports() 
        
        #deinitilize   
        os.chdir(Utils.getProjRoot() + "bin")  
        shutil.rmtree(Utils.getProjRoot() + "data/temp")  

        #assert 
        with open(RES_DIR + "test_successRead.txt") as expected:  
            assert expected.read().strip() == result.strip() 

    def test_falseTaskRead(self):  
        #initalize   
        shutil.copytree(Utils.getProjRoot() + "test/src" , Utils.getProjRoot() + "data/temp")
        os.chdir(Utils.getProjRoot() + "data/temp")  

        task1 = Task(toolName = "Pylint", command= ["pylint temp --output-format=json"], 
                                method = "FILE",requestCommands = [ 
                                                                "../../test/testData/Test_ReportReader_data/pylint_sample_report.json"], 
                                                sucRetCodes=[0,16,22],output="NIL", error="NIL",
                                                mapping={}) 
        task1.status = False
        
        reportReader = ReportReader([task1],intFile)

        result = reportReader.parseReports() 
        
        #deinitilize   
        os.chdir(Utils.getProjRoot() + "bin")  
        shutil.rmtree(Utils.getProjRoot() + "data/temp")  

        #assert 
        with open(RES_DIR + "test_falseTaskRead.txt") as expected:  
            assert expected.read().strip() == result.strip()


    
if __name__ == '__main__': 
    unittest.main()