from discord import Message
from discord.ext import commands
from random import choice


class Slapper(commands.Converter):
    async def convert(self, context: Message, argument: str) -> str:
        name = context.author.name
        someone = choice(context.guild.members).name
        return f"{name} slaps {someone} with {argument}"


# Slap a user
@commands.command(
    help="Slap a random user with argument",
    description="Slap a random user with argument",
    brief="Slaps",
    enabled=True,
    hidden=False,
)
async def slap(context: Message, reason: Slapper) -> None:
    await context.send(reason)


async def setup(bot: commands.Bot):
    bot.add_command(slap)
