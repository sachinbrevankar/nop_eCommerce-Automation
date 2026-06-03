import configparser
from typing import Any

config=configparser.RawConfigParser()
config.read("Configurations/config.ini")

class readConfig:
    @staticmethod
    def getApplicationurl() -> str | Any:
        url=config.get('Common Data','baseurl')
        return url

    @staticmethod
    def getUsername():
        username=config.get('Common Data','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('Common Data','password')
        return password