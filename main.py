import colorama 
import requests
import os
import random
import tasksio
import asyncio

from colorama import Fore, Style, init
from tasksio import TaskPool

b = Style.BRIGHT
sent = 0

class Axcey():
    def __init__(self):
        self.tokens = []
        
        for token in open('tokens.txt'):
            if token != '':
                self.tokens.append(token.replace("\n", "").replace("\r", "").replace("\n\r", ""))
    
    async def Menu(self):
        os.system(f'cls & mode 85,20 & title [Axcey Report] - Menu')
        print(f'''
{b+Fore.BLUE}
       ▄████████ ▀████    ▐████▀  ▄████████    ▄████████ ▄██   ▄   
      ███    ███   ███▌   ████▀  ███    ███   ███    ███ ███   ██▄ 
      ███    ███    ███  ▐███    ███    █▀    ███    █▀  ███▄▄▄███ 
      ███    ███    ▀███▄███▀    ███         ▄███▄▄▄     ▀▀▀▀▀▀███ 
    ▀███████████    ████▀██▄     ███        ▀▀███▀▀▀     ▄██   ███ 
      ███    ███   ▐███  ▀███    ███    █▄    ███    █▄  ███   ███ 
      ███    ███  ▄███     ███▄  ███    ███   ███    ███ ███   ███ 
      ███    █▀  ████       ███▄ ████████▀    ██████████  ▀█████▀  {Fore.RESET}

{b+Fore.RED}─────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{b+Fore.BLUE}Axcey Reporter{Fore.RESET} {b+Fore.RED}[Menu]{Fore.RESET}
                {b+Fore.MAGENTA}└─{Fore.RESET}[{b+Fore.BLUE}1{Fore.RESET}] {b+Fore.RED}Single Token{Fore.RESET}
                {b+Fore.MAGENTA}└─{Fore.RESET}[{b+Fore.BLUE}2{Fore.RESET}] {b+Fore.RED}Multiple Tokens{Fore.RESET}              
              ''')
        choice = input(f'{b+Fore.BLUE}> {Fore.RESET}Choice{b+Fore.BLUE}: {Fore.RESET}')
        if choice == '1':
            self.SingleReport()
        elif choice == '2':
            await self.MassReport()
        elif choice is None:
            await self.Menu()
        else:
            print(f'{b+Fore.RED}[!] {Fore.RESET}Invalid Choice')
            await self.Menu()
            
    def SingleReport(self):
        os.system(f'cls & mode 85,20 & title [Axcey Report] - Single Report')
        print(f'''
{b+Fore.BLUE}Axcey Reporter{Fore.RESET} {b+Fore.RED}[Single Token]{Fore.RESET}
[{b+Fore.BLUE} {1} {Fore.RESET}] Illegal Content        
[{b+Fore.BLUE} {2} {Fore.RESET}] Harassment            
[{b+Fore.BLUE} {3} {Fore.RESET}] Spam or phishing links 
[{b+Fore.BLUE} {4} {Fore.RESET}] Hateful Content        
[{b+Fore.BLUE} {5} {Fore.RESET}] NSFW Content                  
              ''')
        guild = input(f'{b+Fore.BLUE}> {Fore.RESET}Server ID{b+Fore.BLUE}: {Fore.RESET}')
        if guild is None:
            self.SingleReport()
        channel = input(f'{b+Fore.BLUE}> {Fore.RESET}Channel ID{b+Fore.BLUE}: {Fore.RESET}')
        if channel is None:
            self.SingleReport()
        message = input(f'{b+Fore.BLUE}> {Fore.RESET}Message ID{b+Fore.BLUE}: {Fore.RESET}')
        if message is None:
            self.SingleReport()
        reason = int(input(f'{b+Fore.BLUE}> {Fore.RESET}Option{b+Fore.BLUE}: {Fore.RESET}'))
        if reason is None:
            reasons = ['1', '2', '3', '4', '5']
            reason = random.choice(reasons)
        token = input(f'{b+Fore.BLUE}> {Fore.RESET}Token{b+Fore.BLUE}: {Fore.RESET}')
        if token is None:
            self.SingleReport()
        print()
        global sent
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            "Content-Type": "application/json"
        }

        json = {
        "guild_id": guild, 
        "channel_id": channel,
        "message_id": message, 
        "reason": reason
        }

        while True:
            src = requests.post("https://discord.com/api/v9/report", headers=headers, json=json)
            if src.status_code in [200, 201, 204]:
                print(f"{Fore.GREEN} > Sent Report{Fore.RESET} \x1b[38;5;21m[%s" % sent + '\x1b[38;5;21m]\033[0m')
            elif src.status_code == 401:
                print(f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}Invalid Token {Fore.RESET}')
                
    async def MassReport(self):
        os.system(f'cls & mode 85,20 & title [Axcey Report] - Multiple Report')
        print(f'''
{b+Fore.BLUE}Axcey Reporter{Fore.RESET} {b+Fore.RED}[Multiple Report]{Fore.RESET}
[{b+Fore.BLUE} {1} {Fore.RESET}] Illegal Content        
[{b+Fore.BLUE} {2} {Fore.RESET}] Harassment            
[{b+Fore.BLUE} {3} {Fore.RESET}] Spam or phishing links 
[{b+Fore.BLUE} {4} {Fore.RESET}] Hateful Content       
[{b+Fore.BLUE} {5} {Fore.RESET}] NSFW Content          
    ''')
        guild = input(f'{b+Fore.BLUE}> {Fore.RESET}Server ID{b+Fore.BLUE}: {Fore.RESET}')
        if guild is None:
            self.SingleReport()
        channel = input(f'{b+Fore.BLUE}> {Fore.RESET}Channel ID{b+Fore.BLUE}: {Fore.RESET}')
        if channel is None:
            self.SingleReport()
        message = input(f'{b+Fore.BLUE}> {Fore.RESET}Message ID{b+Fore.BLUE}: {Fore.RESET}')
        if message is None:
            self.SingleReport()
        reason = int(input(f'{b+Fore.BLUE}> {Fore.RESET}Option{b+Fore.BLUE}: {Fore.RESET}'))
        if reason is None:
            reasons = ['1', '2', '3', '4', '5']
            reason = random.choice(reasons)
        global sent
        for token in self.tokens:
            async with TaskPool(5_000) as pool:
                await pool.put(self.MassReportExecute(token, guild, channel, message, reason))
        
    async def MassReportExecute(self, token, guild, channel, message, reason):
        headers = {
            "Authorization": token,
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            "Content-Type": "application/json"
        }

        json = {
            "guild_id": guild,
            "channel_id": channel,
            "message_id": message,
            "reason": reason
        }
        
        while True:
            src = requests.post("https://discord.com/api/v6/report", headers=headers, json=json)
            total_tokens = len(self.tokens)
            if src.status_code in [200, 201, 204]:
                print(f'\x1b[38;5;196m[Mass Reported Succesfully%s]\033[37m \x1b[38;5;34mID: %s\033[37m [Tokens: %s]' % sent, guild, total_tokens)
                
Axcey = Axcey()
loop = asyncio.get_event_loop()
loop.run_until_complete(Axcey.Menu())