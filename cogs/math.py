from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx: commands.Context, num1: int, num2: int):
        await ctx.send(num1 + num2)

    @commands.command()
    async def subtract(self, ctx: commands.Context, num1: int, num2: int):
        await ctx.send(num1 - num2)

    @commands.command()
    async def multiply(self, ctx: commands.Context, num1: int, num2: int):
        await ctx.send(num1 * num2)

    @commands.command()
    async def divide(self, ctx: commands.Context, num1: int, num2: int):
        await ctx.send(num1 / num2)


async def setup(bot: commands.Bot):
    await bot.add_cog(Math(bot))
