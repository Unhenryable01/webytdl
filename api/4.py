import os

print("Thanks for using YTWebDL! v1.7.2 by ItzScratchy")

urltag = input("Paste URL Here: ")

url = 'https://master-cdn.dl-api.com/api/widget?url='

os.system("python -m webbrowser -t "+url+urltag)
