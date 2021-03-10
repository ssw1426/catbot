import discord

client = discord.Client()
token = "ODE4NzAzMjI1NDU2Njg5MTgz.YEb6yw.KRKJduNxaZDX_psSrk8NhI8Y7ZE"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

client.run(token)