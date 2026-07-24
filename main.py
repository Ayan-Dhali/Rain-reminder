import requests
from dotenv import load_dotenv
import os

load_dotenv(".env")

DISCORD_BOT_TOKEN=os.environ.get("Bot_token")
DISCORD_CHANNEL_ID=os.environ.get("channel_id")

API_KEY=os.environ.get("API_KEY")

parameter={
    "lat":52.2297,
    "lon":21.0122,
    "units":"metric",
    "lang":"en",
    "cnt":4,
    "appid":API_KEY
}

API="https://api.openweathermap.org/data/2.5/forecast"

response=requests.get(API,parameter)

data=response.json()

will_rain = False

for hourly_data in data["list"][:4]:
    code=hourly_data["weather"][0]["id"]

    if code<700:
        will_rain=True


if will_rain==True:
    discord_url=f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages"

    headers={
        "Authorization":f"Bot {DISCORD_BOT_TOKEN}",
        "Content-Type":"application/json"
    }

    payload={
        "content":"**Rain Alert!** Grab an umbrella before going out"
    }

    response=requests.post(discord_url,json=payload,headers=headers)
    response.raise_for_status()

    print("Send suucseesfully")
else:
    print("Don't")