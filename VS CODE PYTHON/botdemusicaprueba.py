import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx, url):
    voice_channel = ctx.voice_client

    if not voice_channel:
        await ctx.send("El bot no está en un canal de voz.")
        return

    voice_channel.stop()

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
        'executable': 'C:\\ffmpeg\\bin\\ffmpeg.exe', 
    }

    try:
        voice_channel.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS))
    except Exception as e:
        print(f'Error al reproducir audio: {e}')
        raise  # Levanta la excepción para obtener más detalles en la consola


bot.run('MTE3NTYxNDQyNjUzNjIxODcyNg.GLzbSt.34TUTgLEmxjXBGCvuRVNAXHVYzea58LPWb1VRs')
