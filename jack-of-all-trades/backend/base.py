from flask import Flask, request
import json
from Helpers.CheckCredentials import CheckCredentials


api = Flask(__name__)

@api.route('/test')
def test():
    response = {
        "state": "test"
    }
    return response

@api.route("/api/login", methods=['POST'])
def verify_login():

    username = request.form.get("username")
    password = request.form.get("password")

    with open("./TempData.JSON") as userData:
        data = json.load(userData)
        
    id = CheckCredentials(listOfDict=data, Password=password, Username=username)
    return(
        str(id)
    )

@api.route("/api/loadDash", methods=["GET"])
def loadDash():
    with open("./userData.JSON") as userData:
        data = json.load(userData)

    return(
        data
    )

@api.route("/api/newCharacter", methods=["POST"])
def addCharacter():
    with open ("./userData.JSON", "r") as prevData:
        newId = len(json.load(prevData)) + 1

    dictionary = {newId: {
        "username" : request.form.get("username")
    }}
    
    
    with open ("./userData.JSON", "a") as userData:
        load_data = json.load(userData)
        load_data["userdata"].append(dictionary)
        userData.seek(0)
        json.dump
    return("200")