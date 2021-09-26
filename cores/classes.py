import discord
from discord.ext import commands
intents = discord.Intents.default()

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot