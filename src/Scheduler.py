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
                    schedule.append(Task(tool,toolsObj[tool]["invokeCommands"], 
                        toolsObj[tool]["method"], 
                        toolsObj[tool]["requestCommands"], 
                        toolsObj[tool]["sucRetCodes"], 
                        toolsObj[tool]["output"], 
                        toolsObj[tool]["error"], 
                        toolsObj[tool]["mapping"])) 
       
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




    
     
    
