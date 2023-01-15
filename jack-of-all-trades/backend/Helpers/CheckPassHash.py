import hashlib
import json


def CheckPassHash(username=str, password=str, secretSalt=str):
    testHash = password + secretSalt
    rehashed = hashlib.md5(testHash.encode())
    with open("./GameData/userData.JSON", "r") as userData:
        designatedUser = json.load(userData)
        hashedPass = designatedUser[username]["hashedPass"]
    if hashedPass == rehashed.hexdigest():
        return(True)
    else:
        return(False)
