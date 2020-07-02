import discord
from discord.ext import commands

log_channel = None

class Logger(commands.Cog):
    @commands.command(name='test')
    async def test(self, ctx):
        await log_channel.send('Your magic is working properly ^.^')