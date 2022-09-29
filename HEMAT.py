import os, platform
os.system("pkg install play-audio")
os.system('git pull')



import requests

bit = platform.architecture()[0]

if bit == '64bit':
    os.system("play-audio WELCOME_TO_HEMAT_RANDOM_CLONE_TOOL.mp3")
    from HE-RANDOM import xyz
    xyz()
