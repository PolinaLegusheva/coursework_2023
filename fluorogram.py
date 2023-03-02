import asyncio
import telegram


async def main():
    bot = telegram.Bot(token='6073178391:AAHAbkwD9HJnkafy0wKOZTNINMBp2e7PpkY')
    async with bot:
        await bot.send_message(text='Hi, Od1n!', chat_id=353607352)


if __name__ == '__main__':
    asyncio.run(main())
