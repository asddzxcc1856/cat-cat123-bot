import discord
from cores.classes import Cog_Extension
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

def setup(bot):
    bot.add_cog(Main(bot))        
