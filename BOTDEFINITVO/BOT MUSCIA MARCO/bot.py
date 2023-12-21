import discord
from discord.ext import commands
import yt_dlp
from youtubesearchpython import SearchVideos
import json
import configuracion as config

queue = []
is_playing = False

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix=config.BOT_PREFIX, intents=intents)

def buscar_cancion(query):
    search = SearchVideos(query, offset = 1, mode = "json", max_results = 1)
    result = search.result()
    video_info = json.loads(result)['search_result'][0]
    return video_info['link']

def get_audio_source(url, volume=0.5):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['formats'][0]['url']  # Obtiene la URL directa del audio sin descargar
        audio_source = discord.FFmpegPCMAudio(audio_url)
        audio_source = discord.PCMVolumeTransformer(audio_source)
        audio_source.volume = volume
    return audio_source

def get_playlist_urls(url):
    with yt_dlp.YoutubeDL({'format': 'bestaudio'}) as ydl:
        info = ydl.extract_info(url, download=False)
        video_urls = [video['url'] for video in info['entries']]
    return video_urls

@bot.command(pass_context=True, brief="Haz que el bot se una a tu canal de voz.")
async def join(ctx, *, channel: discord.VoiceChannel = None):
    if channel is None:
        channel = ctx.message.author.voice.channel
    await channel.connect(deafen=True)

@bot.command(pass_context=True, brief="Haz que el bot se vaya de tu canal de voz.")
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

async def play_next(ctx):
    global queue
    global is_playing

    server = ctx.message.guild.voice_client
    if server is None:
        channel = ctx.message.author.voice.channel
        await channel.connect(deafen=True)

    if len(queue) > 0:
        is_playing = True
        url = queue.pop(0)
        audio_source = get_audio_source(url)
        server.play(audio_source)
    else:
        is_playing = False
        await ctx.send('La cola de reproducción está vacía.')

@bot.command(pass_context=True, brief="Reproduce una canción de YouTube o añade una lista de reproducción a la cola.")
async def play(ctx, *, query):
    global queue
    global is_playing
    try:
        server = ctx.message.guild.voice_client
        if server is None:
            channel = ctx.message.author.voice.channel
            await channel.connect(deafen=True)
        if 'youtube.com' in query or 'youtu.be' in query:
            url = query
            if 'playlist' in query:
                playlist_urls = get_playlist_urls(url)
                queue.extend(playlist_urls)
                await ctx.send(f'Se han añadido {len(playlist_urls)} canciones a la cola de reproducción.')
            else:
                queue.append(url)
                await ctx.send('Canción añadida a la cola de reproducción.')
        else:
            url = buscar_cancion(query)
            queue.append(url)
            await ctx.send('Canción añadida a la cola de reproducción.')
        if not is_playing:
            await play_next(ctx)
    except Exception as e:
        await ctx.send(f'Ha ocurrido un error: {str(e)}')

@bot.command(pass_context=True, brief="Cambia el volumen del audio.")
async def volume(ctx, volume: int):
    try:
        if volume < 0 or volume > 100:
            await ctx.send('El volumen debe estar entre 0 y 100.')
        else:
            server = ctx.message.guild.voice_client
            if server.source:
                server.source.volume = volume / 100
                await ctx.send(f'Volumen establecido a {volume}%')
            else:
                await ctx.send('No se está reproduciendo ninguna canción.')
    except Exception as e:
        await ctx.send(f'Ha ocurrido un error: {str(e)}')

@bot.command(pass_context=True, brief="Pausa la canción actual.")
async def pause(ctx):
    server = ctx.message.guild.voice_client
    if server.is_playing():
        server.pause()

@bot.command(pass_context=True, brief="Reanuda la canción actual.")
async def resume(ctx):
    server = ctx.message.guild.voice_client
    if server.is_paused():
        server.resume()

@bot.command(pass_context=True, brief="Detiene la canción actual.")
async def stop(ctx):
    server = ctx.message.guild.voice_client
    if server.is_playing():
        server.stop()

@bot.event
async def on_ready():
    print('READY READY READY READY READY READY')

bot.run(config.BOT_TOKEN)