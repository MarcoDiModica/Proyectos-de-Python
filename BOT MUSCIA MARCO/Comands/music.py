import discord
from discord.ext import commands
import Utility.youtube as yt

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.is_playing = False

    async def play_next(self, ctx):
        if len(self.queue) > 0:
            self.is_playing = True

            # Obtiene la siguiente canción de la cola
            url = self.queue.pop(0)

            # Reproduce la canción
            await self.play(ctx, url)

            # Cuando la canción termine, reproduce la siguiente
            await self.play_next(ctx)
        else:
            self.is_playing = False
            await ctx.send('La cola de reproducción está vacía.')

    @commands.command(pass_context=True, brief="Haz que el bot se una a tu canal de voz.")
    async def join(self, ctx, *, channel: discord.VoiceChannel = None):
        if channel is None:
            channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(pass_context=True, brief="Haz que el bot se vaya de tu canal de voz.")
    async def leave(self, ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(pass_context=True, brief="Reproduce una canción de YouTube o añade una lista de reproducción a la cola.")
    async def play(self, ctx, *, query):
        try:
            server = ctx.message.guild.voice_client

            # Si el bot no está en un canal de voz, únete al canal del autor del mensaje
            if server is None:
                channel = ctx.message.author.voice.channel
                await channel.connect()

            # Comprueba si la consulta es una URL de YouTube
            if 'youtube.com' in query or 'youtu.be' in query:
                url = query
                if 'playlist' in query:
                    # Si es una lista de reproducción, añade todas las canciones a la cola
                    playlist_urls = yt.get_playlist_urls(url)
                    self.queue.extend(playlist_urls)
                    await ctx.send(f'Se han añadido {len(playlist_urls)} canciones a la cola de reproducción.')
                else:
                    # Si es una sola canción, añádela a la cola
                    self.queue.append(url)
                    await ctx.send('Canción añadida a la cola de reproducción.')
            else:
                url = yt.buscar_cancion(query)
                self.queue.append(url)
                await ctx.send('Canción añadida a la cola de reproducción.')

            # Si no se está reproduciendo ninguna canción, reproduce la siguiente
            if not self.is_playing:
                await self.play_next(ctx)
        except Exception as e:
            await ctx.send(f'Ha ocurrido un error: {str(e)}')


    @commands.command(pass_context=True, brief="Cambia el volumen del audio.")
    async def volume(self, ctx, volume: int):
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


    @commands.command(pass_context=True, brief="Pausa la canción actual.")
    async def pause(self, ctx):
        server = ctx.message.guild.voice_client
        if server.is_playing():
            server.pause()

    @commands.command(pass_context=True, brief="Reanuda la canción actual.")
    async def resume(self, ctx):
        server = ctx.message.guild.voice_client
        if server.is_paused():
            server.resume()

    @commands.command(pass_context=True, brief="Detiene la canción actual.")
    async def stop(self, ctx):
        server = ctx.message.guild.voice_client
        if server.is_playing():
            server.stop()


def setup(bot):
    bot.add_cog(Music(bot))
