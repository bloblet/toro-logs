import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix=config.prefix)



bot.run(config.token)