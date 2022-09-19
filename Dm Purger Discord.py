import discord, subprocess, sys, time, os, colorama, ctypes, json, requests, random, pytz
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from sys import argv
from colorama import Fore
from discord.ext import commands

def clear():
    os.system('cls')

def startup():
    print(f'{Fore.MAGENTA}d')
clear()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))


token = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA+"skulls" +
              Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+"Enter Token: " + Fore.WHITE+" ")
purgemessage = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA+"skulls" +
              Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+"Enter prefix: " + Fore.WHITE+" ")


class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="purge_server"):
            channels=message.channel.guild.channels
        elif(message.content==purgemessage):
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(f'{Fore.RED}Purging In:{Fore.RED} {channel}')
            try:
                async for mss in channel.history(limit=None):

                    if(mss.author==self.user):
                        print(f'{Fore.MAGENTA}Message {Fore.MAGENTA}Deleted {Fore.WHITE}-> {Fore.MAGENTA}{mss.content}')
                        try:
                            await mss.delete()
                        except:
                            print("Couldn't delete!")
            except:
                print("Can't read history!\n")

def start():
    print(f'''
{Fore.MAGENTA}╔═╗┬┌─┬ ┬┬  ┬  ┌─┐
{Fore.MAGENTA}╚═╗├┴┐│ ││  │  └─┐
{Fore.MAGENTA}╚═╝┴ ┴└─┘┴─┘┴─┘└─┘

 Send [{Fore.MAGENTA}{purgemessage}{Fore.MAGENTA}] To Delete Msgs
''')
os.system(f'title Discord Dm Purge')
clear()
start()

bot=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
bot.run(token, bot=False)