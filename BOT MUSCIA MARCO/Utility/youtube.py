import discord
import youtube_dl
from youtubesearchpython import SearchVideos
import json

def buscar_cancion(query):
    search = SearchVideos(query, offset = 1, mode = "json", max_results = 1)
    result = search.result()
    video_info = json.loads(result)['search_result'][0]
    return video_info['link']

def get_audio_source(url, volume=0.5):
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}]}) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        audio_source = discord.FFmpegPCMAudio(url2)
        audio_source = discord.PCMVolumeTransformer(audio_source)
        audio_source.volume = volume
    return audio_source

def get_playlist_urls(url):
    with youtube_dl.YoutubeDL({'format': 'bestaudio'}) as ydl:
        info = ydl.extract_info(url, download=False)
        video_urls = [video['url'] for video in info['entries']]
    return video_urls