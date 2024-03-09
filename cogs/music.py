import discord
from discord.ext import commands
import yt_dlp
import asyncio
import settings

# TODO: ONLY FINDING ONE SEARCH RESULT
# TODO: NOT PLAYING THE FULL SONG
# TODO: MAKE QUEUE MESSAGE NICER


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.is_playing = False
        self.is_paused = False

        self.music_queue = []
        self.current_song = ""
        self.YDL_OPTIONS = {
            "format": "bestaudio/best",
            "default_search": "ytsearch10",
            "youtube_api_key": settings.YOUTUBE_KEY,
        }
        self.FFMPEG_OPTIONS = {"options": "-vn"}
        self.vc = None

    def search_youtube(self, query: str) -> list[dict]:
        # Given a Youtube Link
        if "youtube.com" in query or "youtu.be" in query:
            video_id = query.split("v=")[-1]
            if "&" in video_id:
                video_id = video_id.split("&")[0]

            with yt_dlp.YoutubeDL({}) as ydl:
                try:
                    info = ydl.extract_info(
                        f"https://www.youtube.com/watch?v={video_id}", download=False
                    )
                except Exception:
                    return []

            return [{"source": query, "title": info.get("title", "Custom URL")}]

        # Given a Query
        with yt_dlp.YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % query, download=False)[
                    "entries"
                ]
            except Exception:
                return []

        # Compile list of first 5 Results
        i = 0
        search_results = []
        for entry in info:
            if "url" in entry:
                search_results.append({"source": entry["url"], "title": entry["title"]})
                i += 1
            if i == 5:
                break
        return search_results

    def play_next(self) -> None:
        if len(self.music_queue) > 0:
            self.is_playing = True
            music_url = self.music_queue[0][0]["source"]

            self.music_queue.pop(0)
            self.vc.play(
                discord.FFmpegPCMAudio(music_url, **self.FFMPEG_OPTIONS),
                after=lambda e: self.play_next(),
            )
        else:
            self.is_playing = False

    async def play_music(self, ctx) -> None:
        if len(self.music_queue) == 0:
            self.is_playing = False
            return

        self.is_playing = True
        music_url = self.music_queue[0][0]["source"]

        if self.vc == None or not self.vc.is_connected():
            self.vc = await self.music_queue[0][1].connect()

        else:
            await self.vc.move_to(self.music_queue[0][1])

        self.current_song = self.music_queue[0]
        self.music_queue.pop(0)

        self.vc.play(
            discord.FFmpegPCMAudio(music_url, **self.FFMPEG_OPTIONS),
            after=lambda e: self.play_next(),
        )
        await ctx.send(f"Now playing: {self.current_song[0]['title']}")

    # Ask the user what song to play from 5 search results
    async def send_search_results(self, ctx, search_results: list[dict]) -> None:
        embed = discord.Embed(
            title="Search Results", description="Select a song to play:"
        )
        for index, result in enumerate(search_results, start=1):
            embed.add_field(
                name=f"{index}. {result['title']}", value=result["source"], inline=False
            )
        message = await ctx.send(embed=embed)
        return message

    # Select the song to play
    async def select_song(self, ctx, search_results: list[dict]) -> dict:
        # Only accept a choice from the user who searched for the query
        async def check(message):
            same_author = message.author == ctx.author
            is_digit = message.content.isdigit()
            valid_choice = 1 <= int(message.content) <= len(search_results)
            return same_author and is_digit and valid_choice

        # Ask for a choice
        try:
            await ctx.send("Please select a song by entering the corresponding number:")
            message = await self.bot.wait_for("message", check=check, timeout=30)
            choice = int(message.content) - 1
            return search_results[choice]
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond.")
            return None
        except ValueError:
            await ctx.send("Invalid choice. Please enter a valid number.")
            return None

    @commands.command(
        name="play", aliases=["p"], help="Play the selected song from youtube."
    )
    async def play(self, ctx, *args) -> None:
        query = " ".join(args)

        try:
            voice_channel = ctx.author.voice.channel
        except AttributeError:
            await ctx.send("Please connect to a Voice Channel.")
            return

        voice_channel = ctx.author.voice.channel

        search_results = self.search_youtube(query)
        print(search_results)  # TODO: ONLY FINDING 1 SEARCH RESULT

        # Check if search results is empty
        if not search_results:
            await ctx.send("No results found.")
            return

        if len(search_results) == 1:
            song = search_results[0]
        else:
            song = await self.select_song(ctx, search_results)

        # Add the song to queue
        await ctx.send("Song added to the queue.")
        self.music_queue.append([song, voice_channel])

        if not self.is_playing:
            await self.play_music(ctx)

    @commands.command()
    async def pause(self, ctx) -> None:
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()
        elif self.is_paused:
            self.is_playing = True
            self.is_paused = False
            self.vc.resume()

    @commands.command()
    async def resume(self, ctx) -> None:
        if self.is_paused:
            self.is_playing = True
            self.is_paused = False
            self.vc.resume()

    @commands.command()
    async def skip(self, ctx) -> None:
        if self.vc != None and self.vc:
            self.vc.stop()
            await self.play_music(ctx)

    @commands.command()
    async def queue(self, ctx) -> None:
        retval = "```"

        for i in range(0, len(self.music_queue)):
            if i > 4:
                break
            retval += f"{self.music_queue[i][0]['title']}\n"

        if retval != "```":
            retval += "```"
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue.")

    @commands.command()
    async def nowplaying(self, ctx) -> None:
        if self.current_song != "":
            await ctx.send(f"Now playing: {self.current_song[0]['title']}")
        else:
            await ctx.send("No song is playing.")

    @commands.command()
    async def clear(self, ctx, *args) -> None:
        if self.vc != None and self.is_playing:
            self.vc.stop()
        self.music_queue = []
        await ctx.send("Music queue cleared.")

    @commands.command()
    async def leave(self, ctx, *args) -> None:
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
