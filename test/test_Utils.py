import unittest
from src.Engine import Engine  
from src.Scheduler import Task

class TestEngine(unittest.TestCase): 

    def test_sucsessRun(self): 
        engine = Engine([Task("toolName =SonarQube", command = ["../../static-analyzers/sonarQube/sonarqube-8.3.1.34397/bin/linux-x86-64/sonar.sh","../../static-analyzers/sonarQube/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner"])]) 
        self.assertEqual(engine.run()) 