import os
from os import getenv


API_ID = int(getenv("API_ID", "11796331"))
API_HASH = getenv("API_HASH", "a089161b52f234bb90a6eb915551e8c0")
BOT_USERNAME = getenv("BOT_USERNAME", "Oreo_x_music_bot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "5964346248:AAHsWn5GbMj2-zKxyppJy1Si_UPo7It1uHk")
OWNER_ID = int(getenv("OWNER_ID", "6045293810"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6045293810").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://IRO:IRO@cluster0.1nfrzbl.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQCz_2sAqOGEx6x_Zi3fWEyXE4zmTWeJ3hX7m29P8cAYZ_14GNpb3073Rjm__Dcx1nLYnFmb8QZSEurCfu-JaQQIqzG-0hMV4sMDK2ceGkYA3i1n1eZll_40RzJWjlFzeEjtQaUcB25jiWvERlIC1XNqdqIaX7pj_w-WJQkiUiBtIv21fYqxtsL8XuCTFL140EJxEnXEJEoVLy5fhbM9tyGhatbyAMr7CU8ovy9XPaTE1xLj18lswMaRP4iXAQfQj-hgKK1qTQrmWpaTOsaUIHuuBUf3EW132xUjRqg0eW4loTh_We91VnfiBQtb3-_7CkrNu1Pd0bqWHHeJyPcEt_5L3YE1AAAAAAFENM4JAA")
