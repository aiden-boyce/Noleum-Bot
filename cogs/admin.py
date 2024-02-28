from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Load a cog
    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx: commands.Context, cog: str):
        try:
            await self.bot.load_extension(f"cogs.{cog.lower()}")
        except commands.ExtensionNotFound:
            await ctx.send(f"Cog {cog} not found.")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f"Cog {cog} is already loaded.")

    # Reload a cog
    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, cog: str):
        try:
            await self.bot.reload_extension(f"cogs.{cog.lower()}")
        except commands.ExtensionNotFound:
            await ctx.send(f"Cog {cog} not found.")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"Cog {cog} is not loaded.")

    # Unload a cog
    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, cog: str):
        try:
            await self.bot.unload_extension(f"cogs.{cog.lower()}")
        except commands.ExtensionNotFound:
            await ctx.send(f"Cog {cog} not found.")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"Cog {cog} is not loaded.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
