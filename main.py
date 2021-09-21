import sys
import os
import json

try:
    from utils import Start
    from utils import Balance
except ModuleNotFoundError:
    pass


def print_referral(referral):
    try:
        pyperclip.copy(
            'Join me on Salad and use code ' + str(referral['code']) + ' for a 2x earning rate bonus!'
                                                                       ' https://www.salad.io')
        print('Code copied to clipboard!')
    except FileNotFoundError:
        input("an error occured with copying the referral to your clip board")


def setup():
    sys.stdout.write("\x1b]2;Salad CLI+ SETUP\x07")
    salad_key = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsInZlcnNpb24iOiIyIn0=.eyJzZXNzaW9uSGFuZGxlIjoiYWNkNWQ0ODAtZmYyYy00YmJkLWI4YzMtNzMwYjA3ZWE4YmY5IiwidXNlcklkIjoiYmU5OTVhZDMtNmMzMi00NDBkLWEyODUtY2MxNjQ5NjIyOGE3IiwicmVmcmVzaFRva2VuSGFzaDEiOiIyMjY4Y2Q1NzA0NTM1MTY1YmM4NzRiMTk5NmQ0NDRmZTM0NDcxNmI3NTA5ZDkzZTM3YmM2ODVhZjNjMGNhYWFiIiwidXNlckRhdGEiOnt9LCJleHBpcnlUaW1lIjoxNjMyMjY2NjkwODI5LCJ0aW1lQ3JlYXRlZCI6MTYzMjI2MzA5MDgyOSwibG1ydCI6MTYzMjI2MzA5MDgyOX0=.NaweJWaoz3/B+iGPuaNVRTzZLhpg0j8JUb3RZlAnKCI0qe+ESLQKf+rPQfA9jOBl2KwFbfHpED92STS8IhU8x7gwVy3fxV/4wqhaYS8YUS6vcNkJ+d3Era7h/Xnma5snIpr0wGFPhBWaFuQqCcoamjKkFOPtZb2WxAl/VQUOVqJIEbvIs5WKeTYXy+pZc1PDPrfLaI/FRSGL70GCOL8IKa3yYbxISVCvPZG7a1vBs39RW5kd6DZXisVTtK7UNN3Rfp2len8f6lGZ7R/MoMtkk8BUpJrOawi2vzf2fup9qCta1i+ghKb60RpWtPnDnCMf3lXTb29D7bDrZTPIySeGJQ=='
    wallet = ''
    refresh_token = 'VcYzKh9+tFAh6fjOZx+GNdsIGcUruJKuX+ekg7ndaccSlx98W14+R0hY5wOho3RXIhFC/H7hV5CRVqqP8JQvvtauxJQ+tl1Vw0hPL8Zf/rfEKtu8yNbwwEDC7mwhzbzxcxWLsWfVFGzzkA3UUl1jPS2ehYr5zVBb0zyUTq8kIyGqYRzqy4FCc681KPEr+lant9E4EU+5+L+KUCYZncYVacw8fXCKeD8JI9hSdvJZ+J7DAe26BV6BafS8UKRhxRuFgMqtvF5x2+EtHRL3Kf9n.ac0d9be84385883b9124525d3be6d9769659f37e176d644f7735b5b540ef84a7.V2'
    data = {
        "salad_key": salad_key,
        "wallet": wallet,
        "salad_refresh_token": refresh_token
    }
    with open("config.json", "w+") as file:
        json.dump(data, file)
    python_var = 'python3'
    print("installing required libraries")
    os.system(f"{python_var} -m pip install --upgrade pip")
    os.system(f"{python_var} -m pip install pyperclip")
    os.system(f"{python_var} -m pip install python-dateutil")
    os.system(f"{python_var} -m pip install argparse")
    os.system(f"{python_var} -m pip install requests")


switch = {
    1: "Balance.Salad_Balance()",
    2: "Lifetime.Salad_Lifetime()",
    3: "XP.Salad_XP()",
    4: "salad_earnings_update.Salad_Earnings()",
    5: "print_referral(info[1])",
    6: "Mining.Salad_Mining()"
}

try:
    with open("config.json") as file:
        pass
except FileNotFoundError:
    setup()

from utils import Start
from utils import Balance
from utils import Mining
from utils import XP
from utils import Lifetime
from utils import salad_earnings_update
import pyperclip

while True:
    info = Start.get_info()
    dun = False
    while not dun:
        # os.system('clear')
        action = 6 #Start.starting(info)
        try:
            int(action)
            dun = True
        except TypeError or KeyError:
            pass
        if dun:
            exec(switch[int(action)])
            dun = True
