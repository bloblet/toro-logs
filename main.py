import discord
from discord.ext import commands
import config
import logger

bot = commands.Bot(command_prefix=config.prefix)

bot.add_cog(logger.Logger())

log_channel_setup = False
@bot.event
async def on_ready():
    global log_channel_setup
    if not log_channel_setup:
        for channel in bot.get_all_channels():
            if channel.name == 'logs':
                logger.log_channel = channel
                log_channel_setup = True

bot.run(config.token)