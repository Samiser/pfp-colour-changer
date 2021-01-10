from PIL import Image
import itertools
import time
import colorsys
import numpy as np
import random
import json
import tweepy

size = (400, 400)

def authenticate():
    with open('credentials.json', 'r') as c:
        creds = json.loads(c.read())
    
    auth = tweepy.OAuthHandler(
        creds['api_key'],
        creds['api_secret_key']
    )

    auth.set_access_token(
        creds['access_token'],
        creds['access_token_secret']
    )

    return tweepy.API(auth)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def create_image():
    bunny = Image.open("bunny-400x400.png")

    colour = hsv2rgb(random.random(), 0.5, 0.95)
    back = Image.new('RGB', size, colour)

    back.paste(bunny, (0, 0), bunny)
    back.save("out.png", "PNG")

if __name__ == '__main__':
    create_image()
    api = authenticate()    
    api.update_profile_image('out.png')
