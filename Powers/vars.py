from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default="6019105479:AAEHrwEuCPTxNR1VCUh1JOJuAvqVzM32FYo")
    API_ID = int(config("API_ID", default=19895724))
    API_HASH = config("API_HASH", default="124f7fd46b505885a5c37d64e603568a")
    OWNER_ID = int(config("OWNER_ID", default=1205330781))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default="-1001306927879"))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="1205330781",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="1205330781",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="1205330781",
        ).split(" ")
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = config("DB_NAME", default="queen")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="dangerbots")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="dangerbots")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""
    owner_username = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "1835579588:AAFcoI4oymlR2dCbBKvHfYid2Z3G1iqyFKs"
    API_ID = 19895724  # Your APP_ID from Telegram
    API_HASH = "124f7fd46b505885a5c37d64e603568a"  # Your APP_HASH from Telegram
    OWNER_ID = 6248131995  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001306927879  # Your Private Group ID for logs
    DEV_USERS = [1205330781,6556349444,6970517110]
    SUDO_USERS = [1205330781]
    WHITELIST_USERS = [1205330781]
    DB_URI = "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "queen"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = ""
    AuDD_API = ""
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "dangerbots"
    SUPPORT_CHANNEL = "danger_bots"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
