import discord
import time
# Import bot modules
from modules.adminmodule import *
from modules.redditmodule import *
from modules.urbandictmodule import *
from modules.respondmodule import *
from modules.walphamodule import *
from modules.wikipediamodule import *
from modules.physicsmodule import Mastro

tb = False
#import traceback;tb = True # This import is for debugging purpose (see except blocks)



def main():
    global tb
    userdata = {
        "mail" : "",
        "pw"   : "",
        "waapi": ""
    }
    # Read credentials and API codes from .login if available
    try:
        with open(".login","r") as lfile:
            login = lfile.readlines()
        for line in login:
            cmd = line.split()
            if len(cmd)==2:
                userdata[cmd[0]] = cmd[1]
    except:
        if tb: traceback.print_exc()
        print ("No .login file found.")

    # Set the values that were not initialized by .login
    if userdata["mail"]=="":
        userdata["mail"] = input("Email: ")
    if userdata["pw"]=="":
        userdata["pw"] = input("Password: ")
    if userdata["waapi"]=="":
        userdata["waapi"] = input("Wolfram Alpha API ID:")

    # Initialize Modules

    print("Connecting to APIs.")
    try:
        client = discord.Client()
        client.login(userdata["mail"],userdata["pw"])
        reddit = Mreddit(client)
        astro = Mastro(client)
        walpha = Mwalpha(client,userdata["waapi"])
        urbandict = Murbandict(client)
        respond = Mrespond(client)
        admin = Madmin(client,userdata["pw"])
        wiki = Mwikipedia(client)
    except:
        print("Some APIs could not be initialized.")
        if tb: traceback.print_exc()
        return -1


    #=========================================
    #==============EVENT HANDLER==============
    #=========================================
    @client.event
    def on_message(message):
        reddit.check(message)
        urbandict.check(message)
        admin.check(message)
        respond.check(message)
        walpha.check(message)
        wiki.check(message)
        astro.check(message)


    @client.event
    def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    def on_disconnect():
        print("Disconnected!")

    @client.event
    def on_error(event, type, value, traceback):
        print("####ERROR IN DISCORD API:####")
        print(value)

    try:
        client.run()
    except KeyboardInterrupt:
        print("Stopping bot!")
    except Exception as e:
        print("[!] Error: %s"%e)

if __name__ == "__main__":
    main()
