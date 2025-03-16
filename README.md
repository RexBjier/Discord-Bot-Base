# 🤖 Discord Bot Base

A super-awesome, lightweight Discord bot using Python and discord.py with cool slash commands! ✨

## ⭐ Features

- 🎮 Modern slash command support (`/` prefix)
- 🧩 Modular architecture for easy expansion
- 🔌 Extensible cog-based command system
- ⚡ Simple setup and configuration

## 🚀 Getting Started

### 📝 Prerequisites

- 🐍 Python 3.8 or higher
- 👾 A Discord account and access to the [Discord Developer Portal](https://discord.com/developers/applications)

### 🔧 Installation

1. 📥 Clone this repository or download the files
   ```
   git clone https://github.com/RexBjier/discord-bot-base.git
   cd discord-bot-base
   ```

2. 🌍 Set up a virtual environment (optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. 📦 Install the required dependencies
   ```
   pip install -r requirements.txt
   ```

4. ⚙️ Create a new Discord application
   - Click "New Application" in the Developer Portal
   - Navigate to the "Bot" tab and create a bot
   - Enable the "MESSAGE CONTENT" intent under Bot settings

5. 🔑 Configure your bot
   - Copy your bot token from the Discord Developer Portal
   - Open `config.py` and replace `YOUR_BOT_TOKEN_HERE` with your token

6. 🎉 Invite the bot to your server
   - Go to OAuth2 > URL Generator
   - Select `applications.commands` and `bot` scopes
   - Choose permissions (minimum: Send Messages, Use Slash Commands)
   - Use the generated URL to add your bot!

### 🎯 Running the Bot

Fire up your bot with:
```
python bot.py
```

## 💬 Available Commands

- `/ping` - 🏓 Check the bot's latency
- `/hello` - 👋 Get a friendly greeting

## 📁 Project Structure

```
/discord-bot  
│── bot.py           # Main bot file
│── config.py        # Configuration settings
│── commands/        # Commands directory
│   ├── ping.py      # Ping command
│   ├── hello.py     # Hello command
│── requirements.txt # Required packages
```

## ✨ Adding New Commands

Create your own awesome commands in 3 easy steps:

1. 📝 Create a new Python file in `commands/`
2. ✍️ Use this magical template:

```python
import discord
from discord import app_commands
from discord.ext import commands

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mycommand", description="My custom command description")
    async def mycommand(self, interaction: discord.Interaction):
        await interaction.response.send_message("This is my custom command! ✨")

async def setup(bot):
    await bot.add_cog(MyCommand(bot))
```

3. 🔄 Restart your bot and voilà!

## 📜 License

This project is available under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py) - The awesome Discord API wrapper for Python

---

## ❤️ Support & Credits

Created with 💖 by [RexBjier](https://github.com/RexBjier)

If you find this bot template helpful, please consider:
- ⭐ Giving it a star on GitHub
- 🔄 Sharing it with others
- 🐛 Contributing to its development

Your support keeps this project growing! 🚀

###### Made with 🎮 for the Discord Community
