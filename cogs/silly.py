from discord import Message
from discord.ext import commands


class Silly(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


# Ping Pong
@commands.command(
    aliases=["p"],
    help="Ping Pong",
    description="Answers back with pong",
    brief="pong",
    enabled=True,
    hidden=False,
)
async def ping(message: Message):
    await message.send("pong")


# Say a message
@commands.command(
    help="Repeat the user's message",
    description="Simon Says",
    brief="Say a message",
    enabled=True,
    hidden=False,
)
async def say(message: Message, *input: str):
    await message.send(" ".join(input))


async def setup(bot: commands.Bot):
    await bot.add_cog(Silly(bot))
