import requests
from playsound import playsound
from PIL import Image
import os

root = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(root,".cached/img.jpg")

# check if file exists
if not os.path.isfile(filepath):
    print("File not found:", filepath)
    exit()

azdrisyafunction = {
    'endpoint' : "https://ocrttsdrishya.azurewebsites.net/api/ocr?code=rg3LAQvvajAsl8tuXVOBrzGzmCtzM0mG5g4qMkT_av76AzFuwLwIqw==",
    'language': 'en'
    }

img = Image.open(filepath)
print(img.width,img.height)
if img.width > 300:
    img = img.resize((300, int(img.height * 300 / img.width)), Image.LANCZOS)
    img.save(filepath,optimize=True)


with open( filepath , "rb") as image_file:
    resp = requests.post(
            azdrisyafunction['endpoint'],
            data = image_file,
            headers={"locale": azdrisyafunction["language"]},
            timeout=20
            )

if (resp.status_code == 200) and (resp.content != None):
    with open("speech.wav", "wb") as audio_file:
        audio_file.write(resp.content)
    if (len(resp.content) > 100):
        playsound("speech.wav")
else:
    print("Error:", resp.text)
