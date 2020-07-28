import os 

#This class is repsonsible for creating the schedule; the schedule is a list of task objects, 
#which is defined below.  The scheudle can be thought of as the list task that need to be completed to 
#preform a complete analysis on the compatible source code.  
#For each compatible file type, there should exist atleast one static analyzer that can scan it 
#the constructor takes in an intFile object, which is the deseralized contents of the internal file 
class Scheduler: 
#To do: 
    #Testign and bug handeling  
    #turn that list into a set mate

    #exposed public function, makes and returns schedule  

    def __init__(self, intFile):
        self.__intFile = intFile 

    #The makeSchedule function is the public interfacing function of the Scheduler 
    #It creates and returns the schedule 
    #The function scans what extentions exist in the current working directory and determines which 
    #which static analyzers in the internal file should be used to compeletly analyze the src files in the directory 
    def makeSchedule(self):   
        schedule = [] 

        #get file types and other info 
        exts = self.__getFileExt(); 
        tools = list(self.__intFile["tools"])  
        toolsObj = self.__intFile["tools"]  

        #make task to ensure that for each compatible type there's atleast one analyzer
        for ext in exts: 
            for tool in tools:  
                if ext in toolsObj[tool]["fileTypes"]: 
                    tools.remove(tool) 
                    schedule.append(Task(tool,toolsObj[tool]["invokeCommands"], 
                        toolsObj[tool]["method"], 
                        toolsObj[tool]["requestCommands"], 
                        toolsObj[tool]["sucRetCodes"], 
                        toolsObj[tool]["output"], 
                        toolsObj[tool]["error"], 
                        toolsObj[tool]["mapping"])) 
       
        return schedule

    #private function for getting the file types in the current working directory 
    #works by preforming a file walk in the current working directory, and for each file, adds 
    #the extension into the set, and then returns the set 
    def __getFileExt(self):  
        files = []  
        ext = []  

        for root, dirs, filenames in os.walk(".", topdown= True): 
            files.extend(filenames)  
        for file in files: 
            ext.append(file.split(".")[-1]) 

        return ext
        
#Task objects represents an analyzer job/scan that needs to be done and contains info to assist 
#each task is associated with a static analyzer  
#The contructor takes in: toolName a string of the name of the analyzer as indicated in the internal file
#command which is a of strings that is the invokeCommands indicated in the internal file 
#method which is a string that is the method attribute as indicated in the internal file  
#requestCommands which is a list of strings; is the requestCommands attribute as indicated in the internal file 
#sucRetCodes which is a list of integers; is the sucRetCodes attribute as indicated int the internal file 
#output which is a string; is the output attribute as indicated in the internal file 
#error which is a string; is the error attribute as indicated in the internal file 
#mapping which is a dictionary; is the mapping attribute indicated in the internal file 
class Task: 
    status = True 

    def __init__(self, toolName, command, method, 
    requestCommands, sucRetCodes, output, error, mapping ): 
        self.toolName = toolName 
        self.command = command   
        self.method = method 
        self.requestCommands = requestCommands 
        self.sucRetCodes = sucRetCodes  
        self.output = output
        self.error = error   
        self.mapping = mapping




    
     
    
