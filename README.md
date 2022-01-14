# pushbullet-python
#### A Python wrapper around the Pushbullet API to send different types of push notifications to your phone or/and computer.

## Installation
```commandline
pip3 install pushbullet-python
```
Required Package:
- [requests](https://requests.readthedocs.io/en/master/)

## Usage Example
```python
import os
from pushbullet import API

# set the API Class and link it to the api object
api = API()

# now set the token
access_token = os.environ['access_token']
api.set_token(access_token)

# now you can use the API Wrapper

# sending a note, arguments: title, message
api.send_note(
    "Hello",
    "How are you? This is a test from the Pushbullet Python API wrapper.")

# sending a link, arguments: title, message, url
api.send_link("A Link", "Here is my website.", "http://www.lingeswaran.com")

# sending a file, arguments: title, message, file name, file type, file url
api.send_file("An Example Image", "Check out the example image!",
              "test_image.png", "image/png",
              "https://dummyimage.com/600x400/000/fff")
```