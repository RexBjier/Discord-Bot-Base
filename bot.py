import os
import discord
from discord.ext import commands
import asyncio
import config

# Set up intents
intents = discord.Intents.default()

# Create the bot instance
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        self.synced = False

    async def setup_hook(self):
        # Load all command cogs
        for filename in os.listdir('./commands'):
            if filename.endswith('.py') and filename != '__init__.py':
                await self.load_extension(f'commands.{filename[:-3]}')
                print(f'Loaded extension: {filename[:-3]}')

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            # Always sync commands globally so they can be used in any server
            await self.tree.sync()
            print("Synced slash commands globally (may take up to an hour to propagate to all servers)")
            self.synced = True
        
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
        
# Initialize and run the bot
bot = Bot()

# Run the bot with the token
async def main():
    async with bot:
        await bot.start(config.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())