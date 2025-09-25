import os

API_ID    = os.environ.get("API_ID", "22009162")
API_HASH  = os.environ.get("API_HASH", "d361b273d231fc05d29c6cf9824b263e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "
8445043931:AAHkla1sIB4WyrL3q_tWFpQjx1_nMAO88dQ") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
