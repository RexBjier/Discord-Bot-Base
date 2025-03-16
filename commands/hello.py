import discord
from discord import app_commands
from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Get a friendly greeting from the bot")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}! Hope you're having a great day!")

async def setup(bot):
    await bot.add_cog(Hello(bot))