import discord
from discord.ext import commands
from functions.roll_functions import roll_photocard


class Rolls(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx: commands.Context):
        img_info = roll_photocard()
        embed = discord.Embed(
            color=discord.Color.dark_purple(),
            title=img_info["name"],
            description=img_info["category"],
        )
        embed.set_footer(text=f"ID: {img_info['id']}")
        embed.set_image(url=img_info["link"])
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Rolls(bot))
