import discord
import token

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
                    channel = 818390444265832481
                    if message.author.guild_permissions.manage_messages:
                        await client.get_channel(channel).send("@everyone")
                        embed = discord.Embed(title="후원 감사합니다", description= "```" + msg + " 후원 진심으로 감사합니다```", color=0x00D8FF)
                        await client.get_channel(int(channel)).send(embed=embed)
                        await message.delete()
                    else:
                        await message.channel.send(f'> ** <@!{message.author.id}>님 명령어를 사용 할수 없습니다.**')
                        await message.delete()
                except:
                    pass

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)