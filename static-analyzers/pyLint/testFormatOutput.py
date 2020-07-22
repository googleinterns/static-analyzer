with open("../../test/testData/Test_ReportReader_data/pylint_sample_report.json", "r+") as output: 
    data = output.read() 
with open("../../test/testData/Test_ReportReader_data/pylint_sample_report.json", "w+") as output: 
    newData = "{ \"vulList\": "  + data + " }" 
    output.write(newData)