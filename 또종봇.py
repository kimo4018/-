import discord
import random
import datetime
import time
import asyncio
from captcha.image import ImageCaptcha
import re
import os

client = discord.Client()

async def status_task():
    gm = True
    while gm is True:
        game = discord.Game("'봇아 도와줘'하면 도와 줄지도?")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("피드백은 【𝓜𝓞】#3086로 주시오")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(str(len(client.guilds)) + "개의 서버안에서" + str(len(client.users)) + "명한테 갈굼 당하는중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("공지:잡다한 버그가 많다는것을 지금 알았어")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    if message.content.startswith("봇 숫자 맞추기"):
        Image_captcha = ImageCaptcha()
        cap = ""
        for i in range(6):
            cap += str(random.randint(0,9))

        name = str(message.author.name) + ".png"
        Image_captcha.write(cap, name)

        await message.channel.send(file=discord.File(name))

        def check(cap2):
            return cap2.author == message.author and cap2.channel == message.channel
        try:
            cap2 = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("시간초과 다잉!!")

        if cap2.content == cap:
            await message.channel.send("정답이야 눈썰미가 있네(아님말고)")
        else:
            await message.channel.send("야레야레 오답이라구!!!")

    if message.content.startswith("봇아 문제줘"):
        q = random.randrange(1, 999)
        q1 = random.randrange(1, 999)
        await message.channel.send("더러운 관리자가 덧셈만 넣어 놨으니 덧셈문제낸다.10초안에 맞춰라")
        await message.channel.send(str(q) + "+" + str(q1) + "= ?")

        def check1(qu):
            return qu.author == message.author and qu.channel == message.channel
        try:
            qu = await client.wait_for("message", timeout=10, check=check1)
        except:
            await message.channel.send("타임 아웃!!")
        if qu.content == int(q) + int(q1):
            await message.channel.send("우와 정말대단해 맞췄어")
        else:
            await message.channel.send("답을 틀리다니 실망이다.")

    if message.content.startswith("봇 내이름 말해봐"):
        await message.channel.send("귀찮게 시리   " + "'" + message.author.name + "'")

    if message.content.startswith("봇아 도와줘"):
        embed = discord.Embed(color=0x00ffff)
        await message.channel.send("내 마음이 넓어서 도와준다 힛")
        embed.add_field(name="정보", value="``봇아 프로필줘``", inline=False)
        embed.add_field(name="소통(?)", value="``봇아 심심해``, ``봇 오이오이``, ``봇 하이``, ``봇아 죽어``, ``봇 내이름 말해봐``", inline=False)
        embed.add_field(name="게임(?)", value="``봇 끝말잇기 하자``, ``봇 가바보 도움말``, ``봇 숫자 맞추기``", inline=False)
        embed.add_field(name="제작", value="``봇 패치내용``, ``봇 너의 제작자는 누구니?``, ``봇 컨셉``, ``봇 초대``", inline=False)
        embed.add_field(name="tip", value="명령어가 길어서 적기 귀찮으면 위에있는 명령어를 복사해서 붙여넣어. 그리고 난 띄어쓰기가 맞지 않으면 무시해 히힛", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("봇 서버정보줘"):
        await message.channel.send("ㅡㅡ")
        embed = discord.Embed(color=0x00ffff)
        embed.add_field(name="이름", value=message.guild.name, inline=False)
        await message.channel.send(embed=embed)
        await message.channel.send("이정도만 하자(귀찮아)")

    if message.content.startswith("봇 초대"):
        embed = discord.Embed(color=0x808080)
        embed.set_author(name="이텍스트를 클릭하면 따까리인 제가 초대되요. (사장님^^7)", url="https://discordapp.com/oauth2/authorize?client_id=603588878766702622&scope=bot&permissions=1916267615")
        await message.channel.send(embed=embed)

    if message.content.startswith("봇 하이"):
        chat2 = "12345"
        msg1 = random.choice(chat2)
        if msg1 == "1":
            await message.channel.send("ㅇㅇ")
        if msg1 == "2":
            await message.channel.send("오!!!! 누구세요?")
        if msg1 == "3":
            await message.channel.send("조용히해 집중하는거 안보여? (아..안보이는구나)")
        if msg1 == "4":
            await message.channel.send("오 하이!!")
        if msg1 == "5":
            await message.channel.send("뭐")

    if message.content.startswith("봇아 죽어"):
        chat3 = "12345"
        msg2 = random.choice(chat3)
        if msg2 == "1":
            await message.channel.send("싫은뒈??")
        if msg2 == "2":
            await message.channel.send("응 안돼")
        if msg2 == "3":
            await message.channel.send("그 이유는")
        if msg2 == "4":
            await message.channel.send("갑자기?")
        if msg2 == "5":
            await message.channel.send("무지개 반사")

    if message.content.startswith("봇 패치내용"):
        embed = discord.Embed(color=0x00ffff)
        embed.add_field(name="소통(?)", value="``봇 하이``라는 명령어 추가헸어")
        embed.add_field(name="봇 가바보", value="퀄리티 업그레이드를 했어", inline=False)
        embed.add_field(name="명령어 목록", value="명령어 목록들을 정리해봤어", inline=False)
        embed.add_field(name="봇 숫자 맞추기", value="새로운게임(?) 이야", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("봇아 프로필줘"):
        await message.channel.send("칵 퉷!!!")
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id)>> 22)+ 1420070400000)/ 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="서버별명", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("봇아 선배 봇이다"):
        await message.channel.send("안녕하십니까!!!!!!!!!")

    if message.content.startswith("봇 가바보 도움말"):
        embed = discord.Embed(color=0x00ffff)
        embed.add_field(name="``봇 가바보 가위``", value="참고로 난 가위를 내", inline=False)
        embed.add_field(name="``봇 가바보 바위``", value="참고로 난 바위도 내", inline=False)
        embed.add_field(name="``봇 가바보 보``", value="참고로 난 보도 내", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("봇 컨셉"):
        await message.channel.send("내 컨셉은 너한테 반말한는 컨셉이야")

    if message.content.startswith("봇 오이오이"):
        string_pool = "12345"
        msg = random.choice(string_pool)
        if msg == "1":
            await message.channel.send("뭐")
        if msg == "2":
            await message.channel.send("왜")
        if msg == "3":
            await message.channel.send("?")
        if msg == "4":
            await message.channel.send("부르지마")
        if msg == "5":
            await message.channel.send("시끄러")

    if message.content.startswith("봇아 심심해"):
        chat1 = "12345"
        ch = random.choice(chat1)
        if ch == "1":
            await message.channel.send("어쩌라고")
        if ch == "2":
            await message.channel.send("내알빠냐?")
        if ch == "3":
            await message.channel.send("응")
        if ch == "4":
            await message.channel.send("아싸는 원래그래")
        if ch == "5":
            await message.channel.send("난 안심심하니까 된거임 ㅅㄱ")

    if message.content.startswith("봇아 문제줘"):
        q = random.randrange(1, 101)
        q1 = random.randrange(1, 1001)
        await message.channel.send("더러운 관리자가 덧셈만 넣어 놨으니 덧셈문제낸다.0.0000000000000000000000000001초안에 맞춰라")
        await message.channel.send(str(q) + "+" + str(q1) + "= ?")
        await message.channel.send("정답은?")
        if message.content.startswith("q + q1"):
            await message.channel.send("와 정말 대.단.해 정답이야.")
        else:
            await message.channel.send("시간안에 못맞추다니 실망이다. 쯧쯧")

    if message.content.startswith("봇 너의 제작자는 누구니"):
        embed = discord.Embed(color=0xffffff)
        embed.add_field(name="``【𝓜𝓞】``라는 인성이 터진 사람이야(그리고 그사람은 봇 만들기를 매우 귀찮아해)", value="현상수배 ``0``원", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("봇 끝말잇기 하자"):
        say = "12345"
        sa = random.choice(say)
        if sa == "1":
            await message.channel.send("이리듐 내가 이겼군 훗")
        if sa == "2":
            await message.channel.send("우라늄 내가 이겼다 하핫!!!")
        if sa == "3":
            await message.channel.send("이번엔 문장 끝말있기다 '내이름은...' 자 '.' 으로 시작하는 단어나 문장은 없기 때문에 내가 이겼다 음하핫!!!")
        if sa == "4":
            await message.channel.send("산여뀌")
        if sa == "5":
            await message.channel.send("과녘")
    if message.content.startswith("봇 가바보 가위"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            embed = discord.Embed(color=0xFFDC46)
            embed.add_field(name=message.author.name, value=":v:", inline=True)
            embed.add_field(name="그냥봇", value=":v:", inline=True)
            embed.add_field(name="결과", value="무승부!!", inline=False)
            await message.channel.send(embed=embed)
        if rsp1 == "2":
            embed = discord.Embed(color=0xEB0000)
            embed.add_field(name=message.author.name, value=":v:", inline=True)
            embed.add_field(name="그냥봇", value=":fist:", inline=True)
            embed.add_field(name="결과", value="그냥봇 승리!!!!", inline=False)
            await message.channel.send(embed=embed)
        if rsp1 == "3":
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name=message.author.name, value=":v:", inline=True)
            embed.add_field(name="그냥봇", value=":raised_hand:", inline=True)
            embed.add_field(name="결과", value=message.author.name + "가 승리!!", inline=False)
            await message.channel.send(embed=embed)
    if message.content.startswith("봇 가바보 바위"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name=message.author.name, value=":fist:", inline=True)
            embed.add_field(name="그냥봇", value=":v:", inline=True)
            embed.add_field(name="결과", value=message.author.name + "가 승리!!", inline=False)
            await message.channel.send(embed=embed)
        if rsp1 == "2":
            embed = discord.Embed(color=0xFFDC46)
            embed.add_field(name=message.author.name, value=":fist:", inline=True)
            embed.add_field(name="그냥봇", value=":fist:", inline=True)
            embed.add_field(name="결과", value="무승부!!", inline=False)
            await message.channel.send(embed=embed)
        if rsp1 == "3":
            embed = discord.Embed(color=0xEB0000)
            embed.add_field(name=message.author.name, value=":fist:", inline=True)
            embed.add_field(name="그냥봇", value=":raised_hand:", inline=True)
            embed.add_field(name="결과", value="그냥봇 승리!!!!", inline=False)
            await message.channel.send(embed=embed)
    if message.content.startswith("봇 가바보 보"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            embed = discord.Embed(color=0xEB0000)
            embed.add_field(name=message.author.name, value=":raised_hand:", inline=True)
            embed.add_field(name="그냥봇", value=":v:", inline=True)
            embed.add_field(name="결과", value="그냥봇 승리!!!!", inline=False)
            await message.channel.send(embed=embed)
        if rsp1 == "2":
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name=message.author.name, value=":raised_hand:", inline=True)
            embed.add_field(name="그냥봇", value=":fist:", inline=True)
            embed.add_field(name="결과", value=message.author.name + "가 승리!!", inline=False)
            await message.channel.send(embed=embed)
        if rsp1 == "3":
            embed = discord.Embed(color=0xFFDC46)
            embed.add_field(name=message.author.name, value=":raised_hand:", inline=True)
            embed.add_field(name="그냥봇", value=":raised_hand:", inline=True)
            embed.add_field(name="결과", value="무승부!!", inline=False)
            await message.channel.send(embed=embed)

    if "@everyone" in message.content:
        await message.channel.send("보셨죠 여러분? 그렇다네요")




access_token = os.environ["bot_token"]
client.run(access_token)
