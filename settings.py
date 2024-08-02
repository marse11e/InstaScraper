from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read("config.ini")


USER = CONFIG["instaloader"]["user"]
PASSWORD = CONFIG["instaloader"]["password"]