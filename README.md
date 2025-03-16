# Discord Bot Base

A lightweight, modular Discord bot using Python and discord.py with slash command support.

## Features

- Modern slash command support (`/` prefix)
- Modular architecture for easy expansion
- Extensible cog-based command system
- Simple setup and configuration

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A Discord account and access to the [Discord Developer Portal](https://discord.com/developers/applications)

### Installation

1. Clone this repository or download the files
   ```
   git clone https://github.com/RexBjier/discord-bot-base.git
   cd discord-bot-base
   ```

2. Set up a virtual environment (optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```

4. Create a new Discord application in the [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Navigate to the "Bot" tab and create a bot
   - Enable the "MESSAGE CONTENT" intent under Bot settings

5. Configure your bot
   - Copy your bot token from the Discord Developer Portal
   - Open `config.py` and replace `YOUR_BOT_TOKEN_HERE` with your actual token

6. Invite the bot to your server
   - Go to OAuth2 > URL Generator in the Discord Developer Portal
   - Select the `applications.commands` and `bot` scopes
   - Choose appropriate bot permissions (at minimum: Send Messages, Use Slash Commands)
   - Copy and visit the generated URL to add the bot to your server

### Running the Bot

Run the bot using Python:
```
python bot.py
```

## Available Commands

- `/ping` - Check the bot's latency
- `/hello` - Get a friendly greeting from the bot

## Project Structure

```
/discord-bot  
│── bot.py           # Main bot file
│── config.py        # Configuration settings
│── commands/        # Commands directory
│   ├── ping.py      # Ping command
│   ├── hello.py     # Hello command
│── requirements.txt # Required packages
```

## Adding New Commands

To add a new command:

1. Create a new Python file in the `commands` directory (e.g., `commands/mycommand.py`)
2. Use the following template:

```python
import discord
from discord import app_commands
from discord.ext import commands

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mycommand", description="My custom command description")
    async def mycommand(self, interaction: discord.Interaction):
        await interaction.response.send_message("This is my custom command!")

async def setup(bot):
    await bot.add_cog(MyCommand(bot))
```

3. Restart the bot to load the new command

## License

This project is available under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py) - The Discord API wrapper for Python
