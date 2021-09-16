import cv2
import mediapipe as mp
import os
import time
import discord
from discord import Webhook, RequestsWebhookAdapter

### Before running code, make sure to have set the webhook url and the ###
### location for writing the image, preferably the same folder as this ###
### file. Url can be found in discord server settings - integrations   ###

client = Webhook.from_url(
    "https://discordapp.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN",
    adapter=RequestsWebhookAdapter())

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

try:
    os.remove('image.png')
except:
    pass

n = 0
prev_detected = False

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        detected = True
    else:
        detected = False

    if str(prev_detected) == 'False' and str(detected) == 'True':
        client.send("Human detected")
        time.sleep(0.3)
        _, new_img = cap.read()
        try:
            os.remove('image.png')
        except:
            pass
        cv2.imwrite('Enter location for image', new_img)
        client.send(file=discord.File('image.png'))
    else:
        if n == 20:
            try:
                os.remove('image.png')
            except:
                pass
            cv2.imwrite('Enter location for image', img)
            n = 0
    n += 1

    prev_detected = detected
    cv2.imshow("Image", img)
    cv2.waitKey(1)



