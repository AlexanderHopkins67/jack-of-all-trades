import json


def CheckCharData(requestList, CharId=str):
    with open ("./GameData/characterData.JSON", "r") as data:
        all_data = json.load(data)[CharId]
        specified_data = {}
        for i in requestList: 
            specified_data[i] = all_data[i]
        return(specified_data)