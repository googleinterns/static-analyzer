from Engine import Engine  
from Scheduler import Task   
from ReportReader import ReportReader 
from Scheduler import Scheduler  
import Parser

#less priority task 
    #secuirty on engine calls 
    #delete scannerwork folder and make sure everything good 
    
Parser.start()
#schedule = [Task(toolName = "SonarQube", command ="/home/aagubuzo/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner")] 
# Task(toolName = "ShiftLeft", command = "scan -t java")



#engine = Engine(location = "/home/aagubuzo/testsrc", schedule= schedule)    
#reportReader = ReportReader(schedule=schedule) 
#print(reportReader.parseReports())
#engine.run()

#/home/aagubuzo/testsrc


