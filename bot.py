import discord
intents = discord.Intents.default()
intents.members = True

from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is Online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(846916301364527177)
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(846917170947424256)
    await channel.send(f"{member} leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


bot.run('ODkxMzIzMTgzMjk3MzMxMjAw.YU8rZg.JX5_sCQX91uvJsVPwBT1_DJ7TAg')

