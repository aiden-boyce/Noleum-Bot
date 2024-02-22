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
    async def ping(self, context: commands.Context) -> None:
        await context.send("pong")

    # Say a context
    @commands.command(
        help="Repeat the user's context",
        description="Simon Says",
        brief="Say a context",
        enabled=True,
        hidden=False,
    )
    async def say(self, context: commands.Context, *input: str) -> None:
        await context.send(" ".join(input))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Silly(bot))
