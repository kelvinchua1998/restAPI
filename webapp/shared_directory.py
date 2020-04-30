import requests #pip3 install request

r = requests.get("http://127.0.0.1:8000/speedresult/")

shared = open("shared.txt","w")
shared.write(r.json())