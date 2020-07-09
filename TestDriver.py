from Engine import Engine  
from Schedule import Task 

schedule = [Task(toolName = "SonarQube", command ="/home/aagubuzo/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner"), Task(toolName = "ShiftLeft", command = "scan -t java")]



engine = Engine(location = "/home/aagubuzo/testsrc", schedule= schedule)   
engine.run()

#/home/aagubuzo/testsrc

