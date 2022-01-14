import os
from pushbullet_python import API

#set the API Class and linkt it to the api object
api = API()

#now set the token
access_token = os.environ['access_token']
api.set_token(access_token)

#now you can use the API Wrapper
api.send_note(
    "Hello!",
    "How are you? This is a test from the Pushbullet Python API wrapper.")
api.send_link("A Link!", "Here is my website.", "http://www.lingeswaran.de")
api.send_file("Example Image", "Check out the example image!",
              "test_image.png", "image/jpeg",
              "https://dummyimage.com/600x400/000/fff")
