import requests
from requests.structures import CaseInsensitiveDict


class API():
    """ the API Class"""
    def __init__(self):
        """ Initialize a API Class"""
        self.url = "https://api.pushbullet.com/"

    def set_token(self, token):
        """ Authenticate with the API"""
        self.token = token
        #simply set the token

    def send_note(self, title, body):
        """ Send a note as a push notification """
        headers = CaseInsensitiveDict()
        headers["Access-Token"] = self.token
        headers["Content-Type"] = "application/json"
        data = '{"body":"' + body + '","title":"' + title + '","type":"note"}'
        url = self.url + "v2/pushes"
        resp = requests.post(url, headers=headers, data=data)
        print(resp.status_code)

    def send_link(self, title, body, url_to_send):
        """ Send a link as a push notification """
        headers = CaseInsensitiveDict()
        headers["Access-Token"] = self.token
        headers["Content-Type"] = "application/json"
        data = '{"body":"' + body + '","title":"' + title + '","type":"link", "url":"' + url_to_send + '"}'
        url = self.url + "v2/pushes"
        resp = requests.post(url, headers=headers, data=data)
        print(resp.status_code)

    def send_file(self, title, body, file_name, file_type, file_url):
        """ Send a file as a push notification """
        headers = CaseInsensitiveDict()
        headers["Access-Token"] = self.token
        headers["Content-Type"] = "application/json"
        data = '{"body":"' + body + '","title":"' + title + '","file_name":"' + file_name + '","file_type":"' + file_type + '","file_url":"' + file_url + '","type":"file"}'
        url = self.url + "v2/pushes"
        resp = requests.post(url, headers=headers, data=data)
        print(resp.status_code)
