from discord import Member
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        description="Noleum says hello to a specified user",
        brief="Hello [user]",
    )
    async def hello(self, ctx: commands.Context, *, member: Member):
        await ctx.send(f"Hello {member.name}")

    @commands.Cog.listener()
    async def on_ctx(self, ctx: commands.Context):
        """Waves to any ctx that contains [hello]"""
        if "hello" in ctx.content.lower():
            await ctx.add_reaction("👋")


async def setup(bot: commands.Bot):
    await bot.add_cog(Greetings(bot))
