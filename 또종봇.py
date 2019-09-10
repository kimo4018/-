import discord
import asyncio
import os

client = discord.Client()

async def status_task():
    gm = True
    while gm is True:
        game = discord.Game("또종 디스코드에 오신것을 환영합니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("버그는【𝓜𝓞】#3086로 주시길바랍니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(str(len(client.users)) + "시청자와 함께하는중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("'또종봇 도와줘' 라고하면 도움말이 나타나요!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("'또종봇은 개발중입니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    if message.content.startswith("또종봇"):
        await message.channel.send(str(message.author.name) + " 넹?")
        
        
        
access_token = os.environ["bot_token"]
client.run(access_token)
