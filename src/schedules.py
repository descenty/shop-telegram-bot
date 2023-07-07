import logging
import aioschedule
import asyncio
import os, shutil
from datetime import datetime
from s3backup import upload_objects
import constants


async def scheduler(func: callable) -> None:
    aioschedule.every(6).hours.do(func)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def backup() -> None:
    logging.info("Backup started at", datetime.now())

    # backup_dir = f"backup/{datetime.now().strftime('%Y-%m-%d')}"
    # if not os.path.exists("backup"):
    #     os.makedirs("backup")
    # else:
    #     logging.info("Backup folder already exists.\nSkipping...")
    #     return
    # if not os.path.exists(backup_dir):
    #     os.makedirs(backup_dir)

    # shutil.copy("config.json", backup_dir)
    # shutil.copy("database.db", backup_dir)

    upload_objects(["config.json", "database.db"])
    logging.info("Backup finished at", datetime.now())


async def on_startup(_) -> None:
    await constants.bot.set_webhook(
        os.getenv("WEBHOOK_HOST", "") + os.getenv("WEBHOOK_PATH", "")
    )
    # asyncio.create_task(scheduler(backup))
