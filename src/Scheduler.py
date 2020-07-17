import os 

class Scheduler: 
#To do: 
    #Testign and bug handeling 

    #exposed public function, makes and returns schedule  

    def __init__(self, intFile):
        self.__intFile = intFile 

    def makeSchedule(self):   
        schedule = [] 

        exts = self.__getFileExt(); 
        tools = list(self.__intFile["tools"])  
        toolsObj = self.__intFile["tools"]  

        for ext in exts: 
            for tool in tools:  
                if ext in toolsObj[tool]["fileTypes"]: 
                    tools.remove(tool) 
                    schedule.append(Task(tool,toolsObj[tool]["invokeCommands"])) 
        print(schedule)
        return schedule


    def __getFileExt(self):  
        files = []  
        ext = []  

        for root, dirs, filenames in os.walk(".", topdown= True): 
            files.extend(filenames)  
        for file in files: 
            ext.append(file.split(".")[-1]) 

        return ext
        
    
class Task: 

    def __init__(self, toolName, command): 
        self.__toolName = toolName 
        self.__command = command 

    def getToolName(self): 
        return self.__toolName 

    def getCommand(self): 
        return self.__command 
    
     
    
