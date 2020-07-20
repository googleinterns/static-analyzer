import json 
import requests  
import Utils  
import subprocess
from Scheduler import Task
class ReportReader:  

    #To-Do: 
        #finish get report (local & cli) functions  
        #error prevention (espically keys errors, connection errors)
        #other details for report 
        #multi cmd calls 
        #dont get files when scans fail 

    #As far as I know three ways to get the json reports of statix analyzers based off 
    #of where they put them and acsess 
    #1. get local file 
    #2. get CL output 
    #3. api call from server 
    #Thus I'll make functions that support all three of these methods and have the user specficyu what method to use and how  

    #Overall workflow of ReportReader
        #public interfacing function parseReports 
        #collect all generated reports as report objects in array 
        #for each report object create vulnarbitly objects 
        #create big strings from vulnrability objects
       
    def __init__(self, schedule, intFile): 
        self.__schedule = schedule   
        self.__intFile = intFile
        
         

    def parseReports(self):  
        reports = []   
        genReport = ""

        #load report strings into array 
        requests = self.__getRequests() 
        for request in requests:  
           
            if (request.method == "FILE"): 
                reports.append(Report(request.toolName, self.__getLocalFile(request.requestCommands))) 
            elif(request.method == "API"):  
                #returns strign from file
                 reports.append(Report(request.toolName,self.__getApiFile(request.requestCommands)))    
            elif(request.method == "CL"): 
                print("run file commands")  
            else:  
                Utils.printErrorMessage("INVALID REQUEST METHOD")  

        
       

         
        for report in reports: 
            repObj = json.loads(report.json)   
            mapping = self.__intFile["tools"][report.toolName]["mapping"] 
            vuls = repObj[mapping["vulList"]]  
            for vul in vuls: 
                genReport = self.__addToGenReport(genReport=genReport, vul=vul, mapping = mapping, toolName=report.toolName )  


        return genReport




        

        


    #gets the method of how to reterive report
    def __getRequests(self):  
        requests = []
        #loads internal file 
        # creates method objects for each tool in schedule 
        # based on internal file  
        # adds request objects into list  

        #get tools array
        tools = self.__intFile["tools"] 
        #for the tools in each task in the schedule, get request methods/info
        for task in self.__schedule: 
            if task.status == True: 
                tool = tools[task.getToolName()]   
                requests.append(Request(toolName = tool["toolName"],method = tool["method"], requestCommands = tool["requestCommands"])) 
        
        return requests  


    #adds vulanbilites, in general format into report string 
    def __addToGenReport(self, genReport, vul, mapping, toolName): 
        genReport += "\n" 
        genReport += "description: " + vul[mapping["description"]] + "\n" 
        genReport += "toolName: " + str(toolName) + "\n"  
        genReport += "file: " + vul[mapping["file"]] + "\n"  
        #some issues may not have locations
        try:
            genReport += "location: " + str(vul[mapping["location"]]) + "\n"  
        except KeyError:  
            genReport += "location: " + "NO LOCATION" + "\n" 
            

        return genReport 


    

     

    def __getLocalFile(self, requestCommands): 
        length = len(requestCommands)
        curr = 0
        for command in requestCommands:  
            curr +=1  
            if(curr == length):  
                with open(command) as output:
                    return output.read() 
            else: 
                subprocess.run(command, shell=True)  
        subprocess.run(command,shell = True,stdout=output).returncode 
    
    def __getApiFile(self,requestCommands):  
        #method objects contain strings that help get files 
        #an API method will contain uri's for acsessing the report 

         
        #last api call is for report, others may be for auth, 
        length = len(requestCommands)
        curr = 0
        for command in requestCommands:  
            curr +=1  
            if(curr == length):  
                jsonReport = requests.get(command).text 
                return jsonReport 
            else: 
                requests.post(command) 

        

            
        


class Report: 
    def __init__(self, toolName, json): 
        self.toolName = toolName 
        self.json = json   
        
    
    
class Request: 
    def __init__(self, toolName, method, requestCommands): 
        self.toolName = toolName 
        self.method = method 
        self.requestCommands = requestCommands  

    

