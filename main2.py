import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('후원 기록')
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_message(message):
    if message.content.startswith('!후원'):
                try:
                    msg = message.content[4:]
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(title="후원 감사합니다", description= "```" + msg + " 후원 진심으로 감사합니다```", color=0x00D8FF)
                        await message.channel.send(embed=embed)
                        await message.delete()
                    else:
                        await message.channel.send(f'> ** <@!{message.author.id}>님 명령어를 사용 할수 없습니다.**')
                        await message.delete()
                except:
                    pass

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
