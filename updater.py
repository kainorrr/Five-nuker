import zipfile
import os
import urllib.request
import shutil
from time import sleep

print("Five nuker is being updated please wait...")
os.system("title Five nuker is being updated please wait...")

print("Closing the nuker process...")
os.system('taskkill /f /im Five-nuker.exe')

sleep(2)

os.remove("Five-nuker.exe")
shutil.rmtree("_internal")

print("Downloading release.zip...")
urllib.request.urlretrieve("https://github.com/glitch65/Five-nuker/raw/Rework/release.zip", "release.zip")

with zipfile.ZipFile("release.zip", "r") as release:
    release.extractall()

os.remove("release.zip")
os.remove("updater.zip")

os.system("Five-nuker.exe")