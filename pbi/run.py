import json
from pickle import FALSE
import requests

class Embed() :

    def __init__(self) :
        self.hostname = "login.microsoftonline.com"
        self.application_id = "72510915-eef4-41c6-80f2-c0dec001cdc1"
        self.report_id = "9f9203e2-4a97-4d37-82e8-4ef67756078f"
        self.group_id = "dc363ede-3a8d-4163-9036-cbd09e2427ee"
        self.username = "jair.pieritz@ekwdobrasil.com.br"
        self.password = "Ekwdobrasil2020@"
    
    def getToken(self):      
        url = f'https://{self.hostname}/common/oauth2/token'

        header = {
            'Accept': 'application/json'
        }

        body = {
            'grant_type': 'password',
            'scope': 'openid',
            'resource': 'https://analysis.windows.net/powerbi/api',
            'client_id': self.application_id,
            'username': self.username,
            'password': self.password
        }

        try:
            response = requests.post(url, headers=header, data=body)
            self.access_token = json.loads(response.text)['access_token']
            return self.access_token
        except Exception as error:
            return error
    
    def getEmbedURL(self):
        access_token = self.getToken()

        header = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        url = f'https://api.powerbi.com/v1.0/myorg/reports/{self.report_id}'
        try:
            response = requests.get(url, headers=header)
            return json.loads(response.text)['embedUrl']
        except Exception as err:
            return err