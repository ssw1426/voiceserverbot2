import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('상메')
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_message(message):
    if message.content.startswith('/공지'):
                try:
                    msg = message.content[4:]
                    channel = 채널 ID
                    if message.author.guild_permissions.manage_messages:
                        await client.get_channel(channel).send("@everyone")
                        embed = discord.Embed(title=" OO 공지사항", description= "```yaml" + "\n" + msg  + "```", color=0x1DDB16, timestamp=message.created_at)
                        embed.set_footer(text=f"담당 관리자 :  {message.author}")
                        embed.set_image(url="밑에 들어갈 사진 링크 안쓸꺼면 주석 하셈")
                        await client.get_channel(int(channel)).send(embed=embed)
                        await message.delete()
                    else:
                        await message.channel.send(f'> ** <@!{message.author.id}>님 명령어를 사용 할수 없습니다.**')
                        await message.delete()
                except:
                    pass


client.run('봇 토근 넣으셈')