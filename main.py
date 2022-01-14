import requests
from requests.structures import CaseInsensitiveDict
from replit import db

mainurl = "https://api.pushbullet.com/"
access_token = db["access_token"]


def sendPush(title,body,type):
  headers = CaseInsensitiveDict()
  headers["Access-Token"] = access_token
  headers["Content-Type"] = "application/json"
  data = '{"body":"'+body+'","title":"'+title+'","type":"'+type+'"}'
  url = mainurl + "v2/pushes"
  resp = requests.post(url, headers=headers, data=data)
  print(resp.status_code)


sendPush("Hallo!", "Wie geht es dir? Ich hoffe gut.", "note")

