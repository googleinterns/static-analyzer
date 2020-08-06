from datetime import datetime 
import Utils 
import json 
class ReportGenerator: 

    def __init__(self,report,name,verbose):
        self.__report = report   
        self.__fileName = name + str(datetime.now()) 
        self._verbose = verbose  

    def generateReports(self): 
        self.__genString() 
        self.__genHTML() 
        self.__genJSON()  
        self.__genCl() 
        self.__genGerrit()
    
    def __genString(self): 
        jsonObj =json.loads(self.__report)   

        string = "passed: " + str(jsonObj["passed"]) + " " + "numOfVuls: " + str(jsonObj["numOfVuls"]) + " \n"

        for vul in jsonObj["listOfVuls"]:
            string += "\ndescription: " + vul["description"] + "\n" 
            string +=  "toolName: " + vul["toolName"] + "\n" 
            string += "file: " + vul["file"] + "\n"
            string += "location: " + str(vul["location"]) + "\n"

        self.__string = string  

    def __genHTML(self): 
        string = "" 
        string += "<!DOCTYPE HTML>\n" 
        string += "<html lang = \"en\">\n" 
        string += "<head>\n" 
        string += "     <title>" + self.__fileName + "</title>\n" 
        string += "     <meta charset = \"UTF-8\" />\n" 
        string += "</head>\n" 
        string += "<body>\n" 
        string += self.__string +"\n" 
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
        string += "Check Reports For Verbose Info or use -v" 
        Utils.printNotiMessage(string)

        if self._verbose: 
            Utils.printNotiMessage(self.__string)

    def __genGerrit(self): 
        gerritList = [] 
        
        jsonObj =json.loads(self.__report)   
        for vul in jsonObj["listOfVuls"]: 
            obj = {"path": vul["file"], "message": vul["description"], "startLine":vul["location"]} 
            gerritList.append(obj) 
        
        with open(Utils.getProjRoot() + "reports/" + "gerrit_comments.json", "w") as file: 
            file.write(json.dumps(gerritList))
        
    
        
       


