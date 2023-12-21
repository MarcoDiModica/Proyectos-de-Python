import discord
from discord.ext import commands
import configuracion
import Comands.music as music

bot = commands.Bot(command_prefix=configuracion.BOT_PREFIX)

bot.add_cog(music.Music(bot))

@bot.event
async def on_ready():
    print('Bot Ready to use AWE.')

bot.run(configuracion.BOT_TOKEN)