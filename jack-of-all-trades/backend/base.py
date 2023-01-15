from functools import wraps
import imp
from operator import truediv
from flask import Flask, request
import json
import jwt
from Helpers.CheckCredentials import CheckCredentials
from Helpers.CheckCharData import CheckCharData
from Helpers.CheckPassHash import CheckPassHash
from config import SECRET_KEY


api = Flask(__name__)

@api.route('/test')
def test():
    response = {
        "state": "test"
    }
    return response

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return("Error: Valid Token Not Found")
        try:
            public_id = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            with open ("./GameData/userData.JSON") as users:
                current_user = users[public_id]
        except:
            return("Error: Invalid Token")
        return f(current_user, *args, **kwargs)
    return(decorator)



@api.route("/api/login", methods=['POST', 'GET'])
def verify_login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    with open("./GameData/userData.JSON", "r") as userData:
        users = json.load(userData)
        designatedUser = users[username]

    if CheckPassHash(username=username, password=password, secretSalt=SECRET_KEY):
        token = jwt.encode({"public_id": designatedUser["public_id"]}, SECRET_KEY, algorithm="HS256")
        return(token)
    else:
        return("Error")

    

@api.route("/api/loadDash", methods=["GET"])
def loadDash():
    with open("./GameData/userData.JSON") as userData:
        data = json.load(userData)

    return(
        data
    )

@api.route("/api/newCharacter", methods=["POST"])
def addCharacter():
    with open ("./GameData/userData.JSON", "r") as prevData:
        newId = len(json.load(prevData)) + 1

    dictionary = {newId: {
        "username" : request.form.get("username")
    }}
    
    
    with open ("./GameData/userData.JSON", "a") as userData:
        load_data = json.load(userData)
        load_data["userdata"].append(dictionary)
        userData.seek(0)
        json.dump
    return("200")

@api.route("/api/gameData/get", methods=["GET"])
def getActionData():
    isHostile = CheckCharData(CharId="character", requestList=["isHostile"])
    # return(str(isHostile.values()))
    with open ("./GameData/actionTypes.JSON", "r") as actions:
        allActions = json.load(actions)
        availableActions = []

        for i in range(0, len(allActions["actions"])):
            if allActions["actions"][i]["isHostile"] == isHostile["isHostile"]:
                availableActions.append(
                    {
                        "name" : allActions["actions"][i]["name"],
                        "id": allActions["actions"][i]["id"]
                        }
                    )
    return(availableActions)

@api.route("/api/authTest", methods=["GET", "POST"])
@token_required
def updatePlayerData():
    return("worked")
