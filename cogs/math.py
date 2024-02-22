from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def add(self, context: commands.Context, num1: int, num2: int) -> None:
        await context.send(num1 + num2)

    @commands.command()
    async def subtract(self, context: commands.Context, num1: int, num2: int) -> None:
        await context.send(num1 - num2)

    @commands.command()
    async def multiply(self, context: commands.Context, num1: int, num2: int) -> None:
        await context.send(num1 * num2)

    @commands.command()
    async def divide(self, context: commands.Context, num1: int, num2: int) -> None:
        await context.send(num1 / num2)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Math(bot))
