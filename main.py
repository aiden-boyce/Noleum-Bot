from discord import Intents, Message
from discord.ext import commands
from responses import get_response
import settings


# Setup the Bot
bot_intents: Intents = Intents.default()
bot_intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=bot_intents)

# Get logger
logger = settings.logging.getLogger("bot")


# Process Commands
@bot.event
async def send_message(message: Message, user_message: str) -> None:
    # Empty Message
    if not user_message:
        print("Intents not properly enabled: Message empty")
        return

    # Not a bot command
    if user_message[0] != "$":
        return

    try:
        user_message = user_message[1:]
        response = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


# Handle incoming messages
@bot.event
async def on_message(message: Message) -> None:
    # Don't send a message responding to itself
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Run the bot
def main() -> None:
    # Get logger
    logger = settings.logging.getLogger("bot")

    # Bot start up
    @bot.event
    async def on_ready() -> None:
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    bot.run(settings.TOKEN, root_logger=True)


if __name__ == "__main__":
    main()
