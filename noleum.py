from discord import Intents
from discord.ext import commands
import settings
import asyncpg


# TODO: Add a Currency
# TODO: Store a User's Photocards (AKA make a Database)
# TODO: Add an Enabled Category and Disabled Category

# Get logger
logger = settings.logging.getLogger("bot")


class Noleum(commands.Bot):
    def __init__(self, **options):
        bot_intents: Intents = Intents.default()
        bot_intents.message_content = True
        super().__init__(
            command_prefix="!",
            description="Learning to make a bot.",
            intents=bot_intents,
            **options,
        )
        # self.loop.run_until_complete(self.create_db_pool())

    # Bot start up
    async def on_ready(self) -> None:
        logger.info(f"User: {self.user} (ID: {self.user.id})")
        # Load all the commands
        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file != "__init__.py":
                await self.load_extension(f"cmds.{cmd_file.name[:-3]}")
        # Load all cogs
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file != "__init__.py":
                await self.load_extension(f"cogs.{cog_file.name[:-3]}")

    # Create the Data Base Pool
    async def create_db_pool(self):
        self.db = await asyncpg.create_pool(
            database="Noleum", user="postgres", password=settings.DB_PASSWORD
        )


# Run the bot
def main() -> None:
    pass


if __name__ == "__main__":
    main()
