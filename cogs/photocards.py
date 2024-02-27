import discord
from discord.ext import commands
from functions.roll_functions import roll_photocard
from views.rolls_view import RollsView
from settings import logging

LOGGER = logging.getLogger("bot")


# TODO: Add a Currency
# TODO: Store a User's Photocards (AKA make a Database)
# TODO: Add an Enabled Category and Disabled Category


class Photocards(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["r"])
    async def roll(self, ctx: commands.Context):
        photocard = roll_photocard()
        view = RollsView(timeout=60)

        embed = discord.Embed(
            color=discord.Color.dark_purple(),
            title=photocard["name"],
            description=photocard["category"],
        )
        embed.set_footer(text=f"ID: {photocard['id']}")
        embed.set_image(url=photocard["link"])

        await ctx.send(embed=embed, view=view)
        await view.wait()
        if view.claimed:
            LOGGER.info(f"{view.user} claimed {photocard['id']}")
            await ctx.send(
                f"{view.user} claimed {photocard['name']} - ID: {photocard['id']}"
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Photocards(bot))
