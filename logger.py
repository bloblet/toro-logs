import discord
from discord.ext import commands

log_channel = None

class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='test')
    async def test(self, ctx, *, args):
        mydict = dict((k.strip(), v.strip()) for k,v in 
              (item.split(':') for item in str(args).split(',')))
        await self.on_log(mydict)

    async def on_log(self, log):
        #save the log to a json file
        typ = log['type']
        log = discord.Embed(
            title=typ,
            description =log['message'],
            color = discord.Color.red() if typ == 'SEVERE' else discord.Color.orange() if typ == 'SHOUT' else discord.Color.gold()
        )
        
        await log_channel.send(embed = log)
        blob_role = self.bot.get_guild(707253315469180953).get_role(707253654411018291)
        await log_channel.send(f'{blob_role.mention} **{typ}**')