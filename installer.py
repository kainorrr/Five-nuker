import urllib.request
import os


print('updating installer...')


os.system('title installer')





def remove_old_launcher():
    try:
        os.system('taskkill /f /im launcher.exe')
        work_folder = str(os.getcwd())
        os.remove(work_folder + 'launcher.exe')
    except: pass

remove_old_launcher()

urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/launcher.exe", "launcher.exe")

os.system('launcher.exe')