import os
from apiclient import discovery
import httplib2
from oauth2client import client

def login(authCode):
    CLIENT_SECRET_FILE = os.getcwd() + '/client_secret.json'
    credentials = client.credentials_from_clientsecrets_and_code(
        CLIENT_SECRET_FILE,
        [],
        authCode[1:-1])

    return { 
        'email' : credentials.id_token['email'], 
        'id' : credentials.id_token['sub'] 
    }