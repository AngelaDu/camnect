import mysql.connector
from mysql.connector.constants import ClientFlag
from credFileHandler import getCred, inputCred, removeCred,eraseFile
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from connectToCalendar import readCalendar


config = {'user': 'root', 'password': 'Calgary123!', 'host': '34.66.86.129', 'client_flags': [ClientFlag.SSL],
          'ssl_ca': 'server-ca.pem', 'ssl_cert': 'client-cert.pem', 'ssl_key': 'client-key.pem',
          "database": "CamnectDb"}

# to establish our connection
conn = mysql.connector.connect(**config)
cursor = conn.cursor()


def createTable():
    query = """CREATE TABLE IF NOT EXISTS users(username VARCHAR(255) PRIMARY KEY)"""
    cursor.execute(query)
    conn.commit()


def removeUser(username):
    query = "DELETE FROM users WHERE username='{}'".format(username)
    cursor.execute(query)
    conn.commit()

    removeCred(username)

    print(username, "removed")


def getData():
    query = "SELECT username FROM users"
    cursor.execute(query)

    for user in cursor:
        for data in user:
            print(data)


def deleteTable():
    query = "DROP TABLE users"
    cursor.execute(query)
    conn.commit()


def registerUser(username, credentials):
    query = "INSERT INTO users VALUES('{}')".format(username)
    cursor.execute(query)
    conn.commit()

    inputCred(username, credentials)

    print(username, "Registered")


def loginUser(username):
    credentials = getCred(username)
    if credentials is None:
        scopes = ["https://www.googleapis.com/auth/calendar"]
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
        credentials = flow.run_console()
        registerUser(username, credentials)

    print(username, "logged in")
    return credentials


def addFriend(username, friendName):
    query = "SELECT friend3 FROM users WHERE username='{}'".format(username)
    cursor.execute(query)

    for data in cursor:
        for friend in data:
            if friend is None:
                query = "UPDATE users SET friend3='{}' WHERE username='{}'".format(friendName, username)

    query = "SELECT friend2 FROM users WHERE username='{}'".format(username)
    cursor.execute(query)

    for data in cursor:
        for friend in data:
            if friend is None:
                query = "UPDATE users SET friend2='{}' WHERE username='{}'".format(friendName, username)

    query = "SELECT friend1 FROM users WHERE username='{}'".format(username)
    cursor.execute(query)

    for data in cursor:
        for friend in data:
            if friend is None:
                query = "UPDATE users SET friend1='{}' WHERE username='{}'".format(friendName, username)

    cursor.execute(query)
    conn.commit()
    print(friendName, "Added to list of friends")


def findService(credentials):
    service = build("calendar", "v3", credentials=credentials)
    return service


getData()
#user = loginUser("Allen")
#print(readCalendar(findService(user)))

conn.close()
