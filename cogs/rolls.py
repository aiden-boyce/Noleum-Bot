import discord
from discord.ext import commands
from functions.roll_functions import roll


class Rolls(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx: commands.Context):
        img = roll()
        embed = discord.Embed(
            color=discord.Color.dark_purple(),
            title="Singer Name",
            description="Band Name",
        )
        embed.set_footer("Click the button to claim!")
        # embed.set_image(url=img)
        await ctx.send("hello")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Rolls(bot))
