import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    game = discord.Game('서버 상태 관찰')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("봇이 온라인으로 변경되었습니다")

@client.event
async def on_message(message):
    if message.content.startswith("!on"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.send("@everyone")
                embed = discord.Embed(title="서버 온 안내", description="voice 서버가 열렸습니다. 즐거운 RP생활 되세요", color=0x62c1cc)
                embed.add_field(name="다이렉트 주소", value="cfx.re/join/84ol95", inline=False)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass

    if message.content.startswith("!r"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.send("@everyone")
                embed = discord.Embed(title="서버 리붓 안내", description="voice 서버가 리붓되었습니다. 즐거운 RP생활 되세요", color=0xFFE400)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass
    if message.content.startswith("!off"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.send("@everyone")
                embed = discord.Embed(title="서버 오프 안내", description="서버 문제 및 패치로 서버가 닫혔습니다", color=0xff0000)
                embed.add_field(name="서버 온 되면 들어와주세요", value="저희 voice 서버는 패치 및 버그에 최선를 다합니다", inline=False)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
