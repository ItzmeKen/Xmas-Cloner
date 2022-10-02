import os

import discord, asyncio, json, sys, ctypes, time, logging
from discord.ext import commands
from os import system
    
logging.basicConfig(level=logging.CRITICAL,format="\x1b[38;5;83m[\x1b[0m%(asctime)s\x1b[38;5;83m]\x1b[0m %(message)s\x1b[0m",datefmt="%H:%M:%S")
class misc:
    def clear():
         return system("cls & mode 95,30")

    def title():
        return ctypes.windll.kernel32.SetConsoleTitleW("Xmas-Clone V1")
    clear()
    def load(text):
        try:
          for sex in text:
            print('' + sex, end="")
            sys.stdout.flush()
            time.sleep(0.0100)
        except:
          pass

    ctypes.windll.kernel32.SetConsoleTitleW("Xmas-Clone V1 - Loading")
    load("""
                         \u001b[38;5;255m         ▀▄░▄▀ █▀▄▀█ █▀▀█ █▀▀   █▀▀█ █── █▀▀█ █▀▀▄ █▀▀ \u001b[0m 
                         \u001b[38;5;246m         ─░█── █─▀─█ █▄▄█ ▀▀█   █─── █── █──█ █──█ █▀▀ \u001b[0m 
                         \u001b[38;5;240m         ▄▀░▀▄ ▀───▀ ▀──▀ ▀▀▀   █▄▄█ ▀▀▀ ▀▀▀▀ ▀──▀ ▀▀▀ \u001b[0m 
                                            \u001b[38;5;244m Loading..
    """)



with open('settings.json', 'r') as x:
    settings = json.load(x)

token = settings.get('token')
prefix = settings.get('prefix')
headers = {
            "Authorization": f'Bot {token}'
            }


intents = discord.Intents.all()
intents.members = True 
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command('help')

class Init:
    @client.event 
    async def on_ready():
        misc.clear()
        misc.title()
        print(f'''
                         \u001b[38;5;255m         ▀▄░▄▀ █▀▄▀█ █▀▀█ █▀▀   █▀▀█ █── █▀▀█ █▀▀▄ █▀▀ \u001b[0m 
                         \u001b[38;5;246m         ─░█── █─▀─█ █▄▄█ ▀▀█   █─── █── █──█ █──█ █▀▀ \u001b[0m 
                         \u001b[38;5;240m         ▄▀░▀▄ ▀───▀ ▀──▀ ▀▀▀╝  █▄▄█ ▀▀▀ ▀▀▀▀ ▀──▀ ▀▀▀ \u001b[0m 
                         
                        \u001b[38;5;244m          User:\u001b[0m \u001b[1m\u001b[38;5;255m{client.user.name}#{client.user.discriminator}\u001b[0m 
                        \u001b[38;5;244m          Prefix:\u001b[0m \u001b[1m\u001b[38;5;255m{prefix}xmasc\u001b[0m 
                                                  
                         
                         
                         
                         
                         '''.center(os.get_terminal_size().columns))


    @client.command()
    async def zardc(ctx): 
        await ctx.message.delete()
        zard = await client.create_guild(f'XmasClone | {ctx.guild.name}')
        await asyncio.sleep(2)
        for sex in client.guilds:
            if f'XmasClone | {ctx.guild.name}' in sex.name:
                for f in sex.channels:
                    await f.delete()
                for category in ctx.guild.categories:
                    x = await sex.create_category(f"{category.name}")
                    logging.critical(f" Cloned Category \u001b[38;5;245m[\u001b[0m{category.name}\u001b[38;5;245m]\u001b[0m")
                    for channels in category.channels:
                        if isinstance(channels, discord.VoiceChannel):
                            await x.create_voice_channel(f"{channels}")
                            logging.critical(f" Cloned Voice Channel \u001b[38;5;245m[\u001b[0m{channels}\u001b[38;5;245m]\u001b[0m")
                        if isinstance(channels, discord.TextChannel):
                            await x.create_text_channel(f"{channels}")
                            logging.critical(f" Cloned Channel \u001b[38;5;245m[\u001b[0m{channels}\u001b[38;5;245m]\u001b[0m")
        for role in ctx.guild.roles[::-1]:
            if role.name != "@everyone":
                try:
                    await zard.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                    logging.critical(f"Cloned Role  [{role.name}]")
                except:
                    break

        print()
        print()
        logging.critical(f" Successfully Cloned Server - [{ctx.guild.name}] ")
    try:
        
        client.run(token, bot=False)
    except discord.LoginFailure:
        logging.critical(f"The token you entered is invalid. ");os.system("PAUSE")

if __name__ == "__main__":
    Init()
