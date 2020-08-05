import subprocess 
import os 
import Utils 
#combine intomain tool
#script used to set up program on machine that has never ran the program before 
#mainly takes care of static analyzer installation and configuration  
ROOT = Utils.getProjRoot()
#make needed directories 
os.mkdir(ROOT + "data/analyzerOutput") 
os.mkdir(ROOT + "reports")

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

#pyLint  
pyLintRoot = ROOT + "static-analyzers/pyLint/" 
os.chdir(pyLintRoot)
subprocess.run("pip install pylint", shell=True)