class Schedule: 

    #exposed public function, makes and returns schedule  
    def makeSchedule(self):  
        #load list of file types in repo 
        #load internal file  
        #for every file type, add all tools that can scan it as task  

        
         

    



class Task: 

    def __init__(self, toolName, command): 
        self.__toolName = toolName 
        self.__command = command 

    def getToolName(self): 
        return self.__toolName 

    def getCommand(self): 
        return self.__command 
    
     
    
