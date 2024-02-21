from discord import Message
from discord.ext import commands


@commands.group()
async def math(context: Message) -> None:
    if context.invoked_subcommand is None:
        await context.send(f"No, {context.subcommand_passed} does not belong to math")


@math.command()
async def add(context: Message, num1: int, num2: int) -> None:
    await context.send(num1 + num2)


@math.command()
async def subtract(context: Message, num1: int, num2: int) -> None:
    await context.send(num1 - num2)


@math.command()
async def multiply(context: Message, num1: int, num2: int) -> None:
    await context.send(num1 * num2)


@math.command()
async def divide(context: Message, num1: int, num2: int) -> None:
    await context.send(num1 / num2)


async def setup(bot):
    bot.add_command(math)
