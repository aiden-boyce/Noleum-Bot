from noleum import Noleum
import settings

# TODO: Add a Currency
# TODO: Store a User's Photocards (AKA make a Database)
# TODO: Add an Enabled Category and Disabled Category


# Run the bot
def main() -> None:
    bot = Noleum()
    bot.run(settings.DISCORD_TOKEN, root_logger=True)


if __name__ == "__main__":
    main()
