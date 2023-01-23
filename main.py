import asyncio
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
mudae_channel =  1067153232104796293
min_claim = 200
counter = 0
rate_limit = 40
start_time = time.time()
bot = commands.Bot(command_prefix='>', self_bot=True)

@bot.event
async def on_ready():
    print('-'*20)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-'*20)

@bot.event
async def on_message(message):
    currtime = time.time()
    if (message.channel.id == mudae_channel and message.author.id == 432610292342587392):
        embeds = message.embeds
        if(len(embeds) > 0 and not (embeds[0].footer)):
            kakera = embeds[0].description.split('**')
            if (len(kakera) > 2 and int(kakera[1]) > min_claim):
                await message.add_reaction('😉')
                print (embeds[0].name)
                print (time.time() - currtime) # show time used to react to message
    global start_time
    global counter
    counter+=1
    if (currtime-start_time >= 1):
        start_time = currtime
        counter = 0
    if (counter >= rate_limit):
        time.sleep(1)
        print ('Program temporarily paused to avoid rate limit')

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
