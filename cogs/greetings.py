from discord import Member
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        description="Noleum says hello to a specified user",
        brief="Hello [user]",
    )
    async def hello(self, context: commands.Context, *, member: Member):
        await context.send(f"Hello {member.name}")

    @commands.Cog.listener()
    async def on_context(self, context: commands.Context):
        """Waves to any context that contains [hello]"""
        if "hello" in context.content.lower():
            await context.add_reaction("👋")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Greetings(bot))
