from discord.ext import commands
import settings

# Get LOGGER
LOGGER = settings.logging.getLogger("bot")


class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.errors):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("You are missing required arguments.")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("Unknown command.")
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send("Command is still on cooldown.")
        else:
            LOGGER.error(error)
            raise error


async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))
