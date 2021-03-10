import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
