import os 

class Scheduler: 

    #exposed public function, makes and returns schedule  
    def makeSchedule(self):  
        self.__getFileExt(); 
        return "NTI"

    def __getFileExt(self):  
        files = [] 

        for root, dirs, filenames in os.walk(".", topdown= True): 
            files.extend(filenames)  

        
    
        print(files)


         

    



class Task: 

    def __init__(self, toolName, command): 
        self.__toolName = toolName 
        self.__command = command 

    def getToolName(self): 
        return self.__toolName 

    def getCommand(self): 
        return self.__command 
    
     
    
