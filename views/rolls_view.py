import discord


class RollsView(discord.ui.View):

    claimed: bool = False
    user: discord.user = None

    @discord.ui.button(label="✔️", style=discord.ButtonStyle.success)
    async def claim_button(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.defer()
        self.claimed = True
        self.user = interaction.user
        self.stop()
