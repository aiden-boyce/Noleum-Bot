from discord import Intents
from discord.ext import commands
import settings
import cogs.greetings

# Setup the Bot
INTENTS: Intents = Intents.default()
INTENTS.message_content = True
BOT = commands.Bot(command_prefix="$", intents=INTENTS)

# Get LOGGER
LOGGER = settings.logging.getLogger("bot")


# BOT start up
@BOT.event
async def on_ready() -> None:
    LOGGER.info(f"User: {BOT.user} (ID: {BOT.user.id})")
    # Load all the commands
    for cmd_file in settings.CMDS_DIR.glob("*.py"):
        if cmd_file != "__init__.py":
            await BOT.load_extension(f"cmds.{cmd_file.name[:-3]}")
    # Load all cogs
    for cog_file in settings.COGS_DIR.glob("*.py"):
        if cog_file != "__init__.py":
            await BOT.load_extension(f"cogs.{cog_file.name[:-3]}")


# Load a cog
@BOT.command(hidden=True)
async def load(context: commands.Context, cog: str):
    await BOT.load_extension(f"cogs.{cog.lower()}")


# Reload a cog
@BOT.command(hidden=True)
async def reload(context: commands.Context, cog: str):
    await BOT.reload_extension(f"cogs.{cog.lower()}")


# Unload a cog
@BOT.command(hidden=True)
async def unload(context: commands.Context, cog: str):
    await BOT.unload_extension(f"cogs.{cog.lower()}")


# Handle errors
@BOT.event
async def on_command_error(context: commands.Context, error) -> None:
    if isinstance(error, commands.MissingRequiredArgument):
        await context.send("handled error globally")


# Run the BOT
def main() -> None:
    BOT.run(settings.TOKEN, root_logger=True)


if __name__ == "__main__":
    main()
