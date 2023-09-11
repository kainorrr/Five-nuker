import urllib.request
import shutil
import os
from pathlib import Path
import urllib3
from colorama import Fore
import colorama
os.system("title Five Nuker - Launcher")
colorama.init(autoreset=True)

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def clear_installator():
    try:
        os.system('taskkill /f /im installer.exe')
        clear()
        os.remove('installer.exe')
    except: pass


clear_installator()



def remade_bin_folder():
    try:
        os.mkdir('Bin')
    except:
        shutil.rmtree('Bin')
        os.mkdir('Bin')

def move_stuff(type):
    if type == 'no':
        nuker = str(Path('fn.exe'))
        ver_file = str(Path('curent_version.fnv'))
        work_folder = str(os.getcwd())
        bin_folder = work_folder + '\Bin'
        shutil.move(nuker, bin_folder)
        shutil.move(ver_file, bin_folder)
    elif type == 'yes':
        icon = str(Path('icon.PNG'))
        nuker = str(Path('fn.exe'))
        ver_file = str(Path('curent_version.fnv'))
        work_folder = str(os.getcwd())
        bin_folder = work_folder + '\Bin'
        shutil.move(icon, bin_folder)
        shutil.move(nuker, bin_folder)
        shutil.move(ver_file, bin_folder)





http = urllib3.PoolManager()

get_launcher_last_ver = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/launcher_last_ver')
get_last_ver = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/curent_version.fnv')
get_changelog = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/ver/changelog')
get_last_ver = get_last_ver.data.decode('utf-8')
get_launcher_last_ver = get_launcher_last_ver.data.decode('utf-8')
get_changelog = get_changelog.data.decode('utf-8')

curent_launcher_ver = str('1.0')
print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Checking for updates...')
if not get_launcher_last_ver == curent_launcher_ver:
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} New version detected!')
    urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/installer.exe", "installer.exe")
    os.system('installer.exe')
else:
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Launcher does not require updating!')


def install_nuker():
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Installing...')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading fn.exe...')
    urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/five%20nuker.exe", "fn.exe")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading curent_version.fnv...')
    urllib.request.urlretrieve("https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/curent_version.fnv", "curent_version.fnv")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading icon.PNG...')
    urllib.request.urlretrieve("https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/main/icon.PNG", "icon.PNG")
    remade_bin_folder()
    move_stuff('yes')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Installed!')

def launch_nuker():
    os.system('Bin\\fn.exe')

def n_check():
    try:
        curent_version = open('Bin\curent_version.fnv', 'r')
        curent_version = curent_version.read()
        if curent_version == get_last_ver:
            print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Nuker does not require updating!')
            launch_nuker()
        else:
            update_nuker()
    except:
        install_nuker()
        launch_nuker()



def backup_user_files():
    config = str(Path('Bin\cfg.ini'))
    icon = str(Path('Bin\icon.PNG'))
    work_folder = str(os.getcwd())
    shutil.move(config, work_folder)
    shutil.move(icon, work_folder)

def restore_user_files():
    config = str(Path('cfg.ini'))
    icon = str(Path('icon.PNG'))
    work_folder = str(os.getcwd())
    bin_folder = work_folder + '\\Bin'
    shutil.move(config, bin_folder)
    shutil.move(icon, bin_folder)

def update_nuker():
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Updating nuker...')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading fn.exe...')
    urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/five%20nuker.exe", "fn.exe")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading curent_version.fnv...')
    urllib.request.urlretrieve("https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/curent_version.fnv", "curent_version.fnv")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Backuping user files...')
    backup_user_files()
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Updating nuker...')
    remade_bin_folder()
    move_stuff('no')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} restoring user files...')
    restore_user_files()
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Done!')
    launch_nuker()





n_check()
