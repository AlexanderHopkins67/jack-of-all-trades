
def CheckCredentials(listOfDict, Password=str, Username=str):
    '''
    Receives a list of dictionaries containing user data, iterates through the data checking for a match,
    Returns user ID if valid match exists, else returns error.
    
    '''
    for i in range(0, len(listOfDict)):
        if listOfDict[i]["username"] == Username and listOfDict[i]["password"] == Password:
            return(listOfDict[i]['id'])
    return("null")