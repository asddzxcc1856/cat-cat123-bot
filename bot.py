import discord
import json
import random
intents = discord.Intents.default()
intents.members = True


from discord.ext import commands

with open('setting.json','r',encoding='utf-8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is Online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Leave_channel"]))
    await channel.send(f"{member} leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

bot.run(jdata['TOKEN'])

