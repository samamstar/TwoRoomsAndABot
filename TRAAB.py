
import discord
import configparser

CONFIG_FILE = 'botconfig.ini'

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


config = ConfigHandler()
print(config.apikey)