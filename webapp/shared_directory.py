import requests #pip3 install request

payload = {"date" : ' 2017', "download": '112.812',"upload": '212.82000'}

r = requests.post("http://127.0.0.1:8000/speedresult/",json = payload)
