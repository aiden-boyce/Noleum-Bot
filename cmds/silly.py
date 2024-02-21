from discord import Message
from discord.ext import commands
import cmds.classes.slapper as Slapper


@commands.group()
async def silly(context: Message) -> None:
    if context.invoked_subcommand is None:
        await context.send(f"No, {context.subcommand_passed} does not belong to silly")


# Ping Pong
@silly.command(
    aliases=["p"],
    help="Ping Pong",
    description="Answers back with pong",
    brief="pong",
    enabled=True,
    hidden=False,
)
async def ping(context: Message) -> None:
    await context.send("pong")


# Say a message
@silly.command(
    help="Repeat the user's message",
    description="Simon Says",
    brief="Say a message",
    enabled=True,
    hidden=False,
)
async def say(context: Message, *message: str) -> None:
    await context.send(" ".join(message))


# Slap a user
@silly.command(
    help="Slap a random user with argument",
    description="Slap a random user with argument",
    brief="Slaps",
    enabled=True,
    hidden=False,
)
async def slap(context: Message, reason: Slapper) -> None:
    await context.send(reason)


async def setup(bot):
    bot.add_command(silly)
