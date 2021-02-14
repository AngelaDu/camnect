import pickle

filename = "CredentialFile.dat"


def createFile():
    with open(filename, "xb") as credFile:
        pass


def inputCred(username, credentials):
    with open(filename, "ab") as credFile:
        data = {"username": username, "credentials": credentials}
        pickle.dump(data, credFile)


def getCred(username):
    with open(filename, "rb") as credFile:
        try:
            while True:
                data = pickle.load(credFile)
                if username == data["username"]:
                    cred = data["credentials"]
                    print(username, "credentials extracted")
                    return cred
        except EOFError:
            pass
    return None


def removeCred(username):
    temp = []
    with open(filename, "rb") as credFile:
        try:
            while True:
                temp.append(pickle.load(credFile))
        except EOFError:
            pass

    with open(filename, "wb") as credFile:
        for data in temp:
            if data["username"] == username:
                pass
            else:
                pickle.dump(data, credFile)


def eraseFile():
    with open(filename, "wb"):
        pass

    print("File data erased")

