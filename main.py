from discord import Intents, Message
from discord.ext import commands
import settings


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


# Handle errors
@BOT.event
async def on_command_error(context: Message, error) -> None:
    if isinstance(error, commands.MissingRequiredArgument):
        await context.send("handled error globally")


# Run the BOT
def main() -> None:
    BOT.run(settings.TOKEN, root_logger=True)


if __name__ == "__main__":
    main()
