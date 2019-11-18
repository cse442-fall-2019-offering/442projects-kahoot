import os
from apiclient import discovery
import httplib2
from oauth2client import client
import sqlite3

def login(authCode):
    db = sqlite3.connect('users.db')

    c = db.cursor()

    CLIENT_SECRET_FILE = os.getcwd() + '/client_secret.json'
    credentials = client.credentials_from_clientsecrets_and_code(
        CLIENT_SECRET_FILE,
        [],
        authCode[1:-1])

    if credentials.refresh_token:
        c.execute("DELETE FROM users WHERE id = '"
            + credentials.id_token['sub']
            + "'")

    c.execute("INSERT INTO users (id, refresh_token) VALUES ('"+
        credentials.id_token['sub']+"', '"+
        credentials.refresh_token+"')")

    db.commit()

    db.close()

    return { 
        'email' : credentials.id_token['email'], 
        'id' : credentials.id_token['sub'] 
    }