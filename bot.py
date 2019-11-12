import discord
import random
import datetime
import time
import asyncio
from captcha.image import ImageCaptcha
import re
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")


@client.event
async def on_member_join(member):
    await client.get_channel(508981703511900198).send(member.mention + "님 " + "``" + member.guild.name + "``" + " 에 오신것을 환영합니다!!")


@client.event
async def on_message(message):
    if message.content == "펌킨봇 핑":
        embed = discord.Embed(color=0x00ffff)
        embed.add_field(name="퐁! ", value='``' + str(int(client.latency * 1000)) + '``' + 'ms', inline=False)
        await message.channel.send(embed=embed)
    if message.content == "펌킨봇 인증":
        await message.channel.send("30초안에 인증번호를 입력해주세요.")
        Image_captcha = ImageCaptcha()
        cap = ""
        for i in range(6):
            cap += str(random.randint(0, 9))

        name = str(message.author.name) + ".png"
        Image_captcha.write(cap, name)

        await message.channel.send(file=discord.File(name))

        def check(cap2):
            return cap2.author == message.author

        try:
            cap2 = await client.wait_for("message", timeout=30, check=check)
        except:
            await message.channel.send("시간초과가 되었습니다.")

        if cap2.content == cap:
            await message.channel.send("확인돼었습니다.")
            role = ""
            for i in message.author.guild.roles:
                if i.name == "[인증됨]":
                    role = i
                    break
            await message.author.add_roles(role)
            role = ""
            for i in message.author.guild.roles:
                if i.name == "인증되지 않음":
                    role = i
                    break
            await message.author.remove_roles(role)
        else:
            await message.channel.send("인증번호가 맞지 않습니다.")
    if message.content == "펌킨봇 개발자":
        embed = discord.Embed(color=0xffffff)
        embed.add_field(name="``키모`` 라는 인성이 터진 사람이에요(그리고 그사람은 봇 만들기를 매우 귀찮아해요)", value="현상수배 ``-10000``원", inline=False)
        embed.set_thumbnail(url=client.get_user(474936819197411338).avatar_url)
        await message.channel.send(embed=embed)


bot_token = os.environ["token"]
client.run(bot_token)
