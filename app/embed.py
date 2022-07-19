import json
import requests

class Embed() :

    def __init__(self) :
        self.hostname = "login.microsoftonline.com"
        self.application_id = "5b324588-2377-4986-aa91-927943c8442a"
        self.report_id = "d029e176-f082-4448-84f9-0a5b09ffbe78"
        self.username = "melvin@2btec.com.br"
        self.password = "@IIbtec2022#"
    
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