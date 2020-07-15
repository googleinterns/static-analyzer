import sys
#need an error exit protocal (deleets temp)
def printErrorMessage(message): 
   
    #stderr print
    print("**************************", file = sys.stderr)
    print("ERROR: " +  message, file = sys.stderr) 
    print("**************************", file = sys.stderr)   

def printNotiMessage(message):  
    print("**************************")
    print("NOTICE: " +  message) 
    print("**************************")  
    