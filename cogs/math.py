from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx: commands.Context, a: int, b: int):
        """a + b = c"""
        await ctx.send(a + b)

    @commands.command()
    async def subtract(self, ctx: commands.Context, a: int, b: int):
        """a - b = c"""
        await ctx.send(a - b)

    @commands.command()
    async def multiply(self, ctx: commands.Context, a: int, b: int):
        """a * b = c"""
        await ctx.send(a * b)

    @commands.command()
    async def divide(self, ctx: commands.Context, a: int, b: int):
        """a / b = c"""
        await ctx.send(a / b)


async def setup(bot: commands.Bot):
    await bot.add_cog(Math(bot))
