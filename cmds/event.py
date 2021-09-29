import discord
import json
from cores.classes import Cog_Extension
intents = discord.Intents.default()
intents.members = True


from discord.ext import commands

with open('setting.json','r',encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata["Welcome_channel"]))
        await channel.send(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata["Leave_channel"]))
        await channel.send(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['apple','pen','pie','abc']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('hi')


def setup(bot):
    bot.add_cog(Event(bot))        