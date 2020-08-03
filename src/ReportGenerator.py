from datetime import datetime 
import Utils 
import json 
class ReportGenerator: 

    def __init__(self,report,name):
        self.__report = report   
        self.__fileName = name + str(datetime.now())  

    def generateReports(self): 
        self.__genHTML() 
        self.__genJSON()  
        self.__genCl() 
    
    def __genString(self): 
        jsonObj =json.loads(self.__report)   

        string = "passed: " + str(jsonObj["passed"]) + " " + "numOfVuls: " + str(jsonObj["numOfVuls"]) + " \n"

        for vul in jsonObj["listOfVuls"]:
            string += "description: " + vul["description"] + "\n" 
            string +=  "toolName: " + vul["toolName"] + "\n" 
            string += "file: " + vul["file"] + "\n"
            string += "location: " + str(vul["location"]) + "\n"

        return string  

    def __genHTML(self): 
        string = "" 
        string += "<!DOCTYPE HTML>\n" 
        string += "<html lang = \"en\">\n" 
        string += "<head>\n" 
        string += "     <title>" + self.__fileName + "</title>\n" 
        string += "     <meta charset = \"UTF-8\" />\n" 
        string += "</head>\n" 
        string += "<body>\n" 
        string += self.__genString() +"\n" 
        string += "</body>\n" 
        string += "</html>" 

        with open(Utils.getProjRoot() + "reports/" + self.__fileName + ".html", "w") as file: 
            file.write(string) 
        



    def __genJSON(self): 
       with open(Utils.getProjRoot() + "reports/" + self.__fileName + ".json", "w") as file: 
            file.write(self.__report) 

    def __genCl(self):  
        jsonObj = json.loads(self.__report) 
        string = "\n"
        string += "Pass?: " + str(jsonObj["passed"]) +"\n" 
        string += "NoOfIssues " + str(jsonObj["numOfVuls"]) + "\n" 
        string += "Check Reports For Robust Info"
        Utils.printNotiMessage(string)
       

    
