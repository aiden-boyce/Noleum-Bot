from discord.ext import commands
from random import choice


class Slapper(commands.Converter):
    async def convert(self, ctx: commands.Context, argument: str) -> str:
        name = ctx.author.name
        someone = choice(ctx.guild.members).name
        return f"{name} slaps {someone} with {argument}"


# Slap a user
@commands.command(
    help="Slap a random user with argument",
    description="Slap a random user with argument",
    brief="Slaps",
    enabled=True,
    hidden=False,
)
async def slap(ctx: commands.Context, reason: Slapper):
    await ctx.send(reason)


async def setup(bot: commands.Bot):
    bot.add_command(slap)
