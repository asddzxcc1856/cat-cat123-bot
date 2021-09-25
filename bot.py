import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
    print(">> Bot is Online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

bot.run('ODkxMzIzMTgzMjk3MzMxMjAw.YU8rZg.JX5_sCQX91uvJsVPwBT1_DJ7TAg')

