#Code ammended from github andrewbeattycourseware/datarepresentation/code/Topic04-apis/csodao.py
#https://github.com/andrewbeattycourseware/datarepresentation/blob/main/code/Topic04-apis/csodao.py
import requests
import json 

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

#Stores data in file
def getAllAsFile():
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)

#Requests data from url and returns
def getAll():
    response = requests.get(url)
    return response.json()

#Stores formatted data in file
def getFormattedAsFile():
    with open("cso-formatted.json", "wt") as fp:
        print(json.dumps(getFormatted()), file=fp)

#Formats data
def getFormatted():
    data = getAll()
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0
    result = {}

    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0]={}
        
        print(label0)
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            #print("\t",label1)
            result[label0][label1]={}
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                #print("\t\t",label2)
                result[label0][label1][label2]=values[valuecount]
                valuecount+=1
        
    return result

if __name__ == "__main__":
    getAllAsFile()
    getFormattedAsFile()
