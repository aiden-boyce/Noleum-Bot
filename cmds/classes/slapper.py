from discord import Message
from discord.ext import commands
from random import choice


class Slapper(commands.Converter):
    async def convert(self, context: Message, argument: str) -> str:
        name = context.author.name
        someone = choice(context.guild.members).name
        return f"{name} slaps {someone} with {argument}"
