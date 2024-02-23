# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "28421635"))
	API_HASH = os.environ.get("a4856de5fec0b9b3601ff06425f3f58e")
	BOT_TOKEN = os.environ.get("6947074831:AAHfx5XvS6p0BXjamh3mdIKtjaC6MMgM4x0")
	BOT_USERNAME = os.environ.get("AnimePediaFile_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001970343871"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1534632634"))
	DATABASE_URL = os.environ.get("mongodb+srv://Cluster01: Cluster01@cluster0.byawv04.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001991806323")
	LOG_CHANNEL = os.environ.get("-1002093375923")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS",").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

🧑🏻‍💻 **Developer:** @RohitxPedia

👥 **Support Group:** [Linux Repositories](https://t.me/animepediaextra)

📢 **Updates Channel:** [Discovery Projects](https://t.me/TeamAnimePedia)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @RohitxPedia



	HOME_TEXT = """
Ram Ram Bhagat 🚩 - [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

You Want To Join Our Channel For Files.

Please subscribe to our channel on Taping below button and then tap on try again to get files.

