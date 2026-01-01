import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "32044382
"))
    API_HASH = os.environ.get("API_HASH", "d42a7af177c70dea013749dd63def67c
")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8542615122:AAFJ4BoRN9IGCD5xyW8u4NR81Y6v_7BTIWY")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "team_phantom_Bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
