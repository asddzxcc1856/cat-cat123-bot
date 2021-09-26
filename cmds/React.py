import discord
from cores.classes import Cog_Extension
from discord.ext import commands
import json
import random
intents = discord.Intents.default()
intents.members = True

with open('setting.json','r',encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 圖片(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

def setup(bot):
    bot.add_cog(React(bot))        
