import sys
import asyncio
import logging
from logging import DEBUG, INFO

from pyrogram import Client, types
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied

from app.settings import settings
from app.const import LogMessages, IrisCommands, WAIT_TIME_BEFORE_SEND_CMD

logging.basicConfig(level=DEBUG if settings.debug else INFO)


class App:
    __client: Client

    def __init__(self) -> None:
        self.__client = Client(
            'account',
            settings.api_id.get_secret_value(),
            settings.api_secret.get_secret_value()
        )

    async def __send_message_to_iris_bot(self, message: str) -> types.Message:
        logging.info(LogMessages.Info.send_message_to_iris.format(message))
        return await self.__client.send_message(
            settings.iris_bot_shortname,
            message
        )

    async def __join_to_iris_channel(self) -> None:
        try:
            await self.__client.join_chat(settings.iris_channel_shortname)
        except (UsernameInvalid, UsernameNotOccupied):
            logging.error(LogMessages.Error.invalid_channel_name)
            sys.exit()

    async def __loop(self) -> None:
        while True:
            await self.__send_message_to_iris_bot(IrisCommands.farm)

            logging.info(LogMessages.Info.wait_seconds.format(WAIT_TIME_BEFORE_SEND_CMD))
            await asyncio.sleep(WAIT_TIME_BEFORE_SEND_CMD)

    async def __main(self) -> None:
        async with self.__client:
            await self.__join_to_iris_channel()
            await self.__loop()

    def start(self) -> None:
        self.__client.run(self.__main())
