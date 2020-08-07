import sys 
import os 
import shutil 
import requests 
import time  
import subprocess
from pathlib import Path 

#Utils.py is a collection of fucntionalites commonly used throughout the program 

#prints error message to standard error  
#message is a string argument; the message that is supposed to be printed
def printErrorMessage(message): 
   
    #stderr print
    print("**************************", file = sys.stderr)
    print("ERROR: " +  message, file = sys.stderr) 
    print("**************************", file = sys.stderr)   

#prints notfication message to standard output 
#message is strign argument; the message that is supposed to be printed
def printNotiMessage(message):  
    print("**************************")
    print("NOTICE: " +  message) 
    print("**************************")   

#quits the program in an error state 
#message to print to standard error indicating why the exit happend; string argument 
#prints to stderr, preforms some clean up, and then exits with 1 exit code
def quitInError(message): 
    printErrorMessage(message)  

    #check if in temp or not and delete temp 
    if os.getcwd().split("/")[-1] == "temp": 
         os.chdir(os.path.dirname(os.getcwd())) 
         shutil.rmtree("temp") 
    os._exit(1)  

#returns the path of the root dirctory of the program
def getProjRoot():  
    return str(Path.home()) + "/static-analyzer/"  

def setup():  
    printNotiMessage("INITIALIZING") 
    ROOT = getProjRoot()
    if os.path.isdir(ROOT + "data/analyzerOutput") == False:  
        #make needed directories 
        os.mkdir(ROOT + "data/analyzerOutput")  
    if os.path.isdir(ROOT + "reports") == False:
        os.mkdir(ROOT + "reports")

    if os.path.isdir(ROOT + "static-analyzers/sonarQube/sonarqube-8.4.1.35646") == False:
        #sonarQube   
        sonarQubeRoot = ROOT + "static-analyzers/sonarQube"
        #download and unzip sonarQube dependices
        os.chdir(sonarQubeRoot) 
        subprocess.run("curl -LO https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-8.4.1.35646.zip", shell=True) 
        subprocess.run("unzip sonarqube-8.4.1.35646.zip", shell=True) 
        subprocess.run("curl -LO https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.4.0.2170-linux.zip", shell=True) 
        subprocess.run("unzip sonar-scanner-cli-4.4.0.2170-linux.zip", shell=True)   
        #set up config file 
        properties = "----- Default SonarQube server \n" 
        properties += "sonar.host.url=http://localhost:9000 \n" 
        properties += "----- Default source code encoding \n" 
        properties += "sonar.sourceEncoding=UTF-8 \n" 
        properties += "sonar.projectKey=SATool \n" 
        properties += "sonar.projectName=SATool \n" 
        properties += "sonar.projectVersion=1.0 \n" 
        properties += "sonar.sources=. \n" 
        properties += "sonar.language=java \n"
        with open(sonarQubeRoot + "/sonar-scanner-4.4.0.2170-linux/conf/sonar-scanner.properties","w") as file: 
            file.write(properties) 
        #grant permissions 
        subprocess.run("chmod +x " + sonarQubeRoot +"/sonarqube-8.4.1.35646/bin/linux-x86-64/sonar.sh", shell=True) 
        subprocess.run("chmod +x " + sonarQubeRoot +"/sonarqube-8.4.1.35646/bin/linux-x86-64/wrapper", shell=True) 
        subprocess.run("chmod +x " + sonarQubeRoot +"/sonarqube-8.4.1.35646/elasticsearch/bin/elasticsearch", shell=True) 
        subprocess.run("chmod +x " + sonarQubeRoot +"/sonarqube-8.4.1.35646/elasticsearch/bin/elasticsearch-env", shell=True)  
        subprocess.run("chmod +x " + sonarQubeRoot +"/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner", shell=True) 
        subprocess.run("chmod +x " + sonarQubeRoot +"/sonar-scanner-4.4.0.2170-linux/jre/bin/java", shell=True) 

    #pip already checks  for  installations before 
    #pyLint  
    pyLintRoot = ROOT + "static-analyzers/pyLint/" 
    os.chdir(pyLintRoot)  
    subprocess.run("pip install pylint", shell=True)


    

