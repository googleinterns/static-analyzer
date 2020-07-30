import unittest  
import os 
import sys 
import json   
from pathlib import Path  
import shutil
import io 
import difflib 

ROOT_DIR = str(Path.home()) + "/staticAnaProj/"
SRC_DIR = ROOT_DIR +"src"  
sys.path.append(SRC_DIR) 

import Parser 

def printTestOutput(str): 
    print("TTT") 
    print(str) 
    print("TTT")  

class TestParser(unittest.TestCase): 

    def test_successRepoOption(self):  
        #initilize  
        files = [] 
        expFiles = []   
        for root, dirs, fileL in os.walk(ROOT_DIR + "test/src"): 
            for file in fileL:
                expFiles.append(os.path.join(ROOT_DIR + "data/temp",file)) 


        expFiles = set(expFiles)

        #test
        Parser.repoOptionFunc([ROOT_DIR + "test/src"]) 
        
        for root, dirs, fileL in os.walk(ROOT_DIR + "data/temp"):  
            for file in fileL: 
                files.append(os.path.join(root,file))  

        printTestOutput("blah " + str(files))
        printTestOutput(expFiles) 
        
        files = set(files)  

        #deintialize  
        shutil.rmtree(ROOT_DIR + "data/temp")

        #results
        assert expFiles == files 

    def test_successListOption(self):  
        #initilize  
        files = [] 
        expFiles = [ROOT_DIR + "data/temp/test.java"]   
        expFiles = set(expFiles) 

        #test 
        Parser.listOptionFunc([ROOT_DIR + "test/src/test.java"]) 

        for root, dirs, fileL in os.walk(ROOT_DIR + "data/temp"):  
            for file in fileL: 
                files.append(os.path.join(root,file))  

        files = set(files)  
        
        #deintialize 
        shutil.rmtree(ROOT_DIR + "data/temp") 

        #results 
        assert expFiles == files 

    
    def test_successExcTypesOpt(self):  
        #initilize  
        files = [] 
        expFiles = []   
        expFiles = set(expFiles) 
        Parser.repoOptionFunc([ROOT_DIR + "test/src"]) 

        #test 
        Parser.excTypeOptionFunc(["py","java"]) 

        for root, dirs, fileL in os.walk(ROOT_DIR + "data/temp"):  
            for file in fileL: 
                files.append(os.path.join(root,file))  

        files = set(files)  
        
        #deintialize 
        shutil.rmtree(ROOT_DIR + "data/temp") 

        #results 
        assert expFiles == files 

    def test_successExcFilesOpt(self):  
        #initilize  
        files = [] 
        expFiles = [ROOT_DIR + "data/temp/test.java", ROOT_DIR + "data/temp/__init__.py"]   
        expFiles = set(expFiles) 
        Parser.repoOptionFunc([ROOT_DIR + "test/src"]) 

        #test  
        #under the assumption that testp.py is the only file path in the exlcude file 
        Parser.excFilesOpt()  

        

        for root, dirs, fileL in os.walk(ROOT_DIR + "data/temp"):  
            for fileName in fileL:
                files.append(os.path.join(root,fileName))  

         

        files = set(files)  
        
        #deintialize 
        shutil.rmtree(ROOT_DIR + "data/temp") 

       
        #results 
        assert expFiles == files


if __name__ == '__main__': 
    unittest.main()     
