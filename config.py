from os import environ

API_ID = int(environ.get("API_ID", "27975779"))
API_HASH = environ.get("API_HASH", "378062eb0a32d8d6b1bbbe97cb63a75a")
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002558820684"))
ADMINS = int(environ.get("ADMINS", "1416841137"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
import os
DB_URI = os.getenv("DB_URI") #Warning - Give Db uri in deploy server environment variable, don't give in repo.
import os
DB_NAME = os.getenv("DB_NAME")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
