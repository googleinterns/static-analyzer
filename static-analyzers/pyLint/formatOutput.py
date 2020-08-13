with open("../analyzerOutput/PyLint.json", "r+") as output: 
    data = output.read()  
if data.replace(" ","") == "": 
    data = "[]"
with open("../analyzerOutput/PyLint.json", "w+") as output: 
    newData = "{ \"vulList\": "  + data + " }" 
    output.write(newData)