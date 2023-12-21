import discord
import yt_dlp
from youtubesearchpython import SearchVideos
import json
import requests

def verificar_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong with the request:",err)
    else:
        return True
    return False

def buscar_cancion(query):
    search = SearchVideos(query, offset = 1, mode = "json", max_results = 1)
    result = search.result()
    video_info = json.loads(result)['search_result'][0]
    url = video_info['link']
    if verificar_url(url):
        return url
    else:
        raise Exception("La URL del video no es válida o no se pudo acceder a ella.")

def get_audio_source(url, volume=0.5):
    if verificar_url(url):
        with yt_dlp.YoutubeDL({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}]}) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            if verificar_url(url2):
                audio_source = discord.FFmpegPCMAudio(url2)
                audio_source = discord.PCMVolumeTransformer(audio_source)
                audio_source.volume = volume
                return audio_source
            else:
                raise Exception("La URL del audio no es válida o no se pudo acceder a ella.")
    else:
        raise Exception("La URL del video no es válida o no se pudo acceder a ella.")

def get_playlist_urls(url):
    if verificar_url(url):
        with yt_dlp.YoutubeDL({'format': 'bestaudio'}) as ydl:
            info = ydl.extract_info(url, download=False)
            video_urls = [video['url'] for video in info['entries']]
            for video_url in video_urls:
                if not verificar_url(video_url):
                    raise Exception("Una o más URLs de la lista de reproducción no son válidas o no se pudo acceder a ellas.")
            return video_urls
    else:
        raise Exception("La URL de la lista de reproducción no es válida o no se pudo acceder a ella.")
