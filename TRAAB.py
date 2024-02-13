
import discord
import configparser
import logging

CONFIG_FILE = 'botconfig.ini'
LOG_FILE = 'bot.log'


class ConfigHandler:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read('defaultconfig.ini')
        self.config.read(CONFIG_FILE)
        # Cast config into variables for easier handling
        self.apikey = self.config['botConfig']['apikey']

    def save(self):
        self.config['botConfig']['apikey'] = self.apikey
        with open(CONFIG_FILE, 'w') as f:
            self.config.write(f)


class PlayerInfo:
    def __init__(self, member) -> None:
        self.member = member


class GameClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, **options) -> None:
        super().__init__(intents=intents, **options)
        self.config = ConfigHandler()
        self.run(self.config.apikey, log_handler=logging.FileHandler(
            LOG_FILE, mode='w', encoding='utf-8'))

    async def on_ready(self):
        print('ready')


# Main setup
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = GameClient(intents=discord.Intents.none())
