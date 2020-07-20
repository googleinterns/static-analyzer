with open("../analyzerOutput/PyLint.json", "r+") as output: 
    data = output.read() 
with open("../analyzerOutput/PyLint.json", "w+") as output: 
    newData = "{ \"vulList\": "  + data + " }" 
    output.write(newData)