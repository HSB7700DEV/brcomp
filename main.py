import os
from pytube import YouTube
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import F

# Replace with your bot token
BOT_TOKEN = "7518154367:AAFlHoaWjCIzujGWHi9guFRHSIXpIAShf8k"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Command: /start
@dp.message(F.text.startswith("/start"))
async def start(message: Message):
    await message.answer("Welcome to the YouTube Downloader Bot! 🎥\nSend me a YouTube link, and I'll download the video for you.")

# Handle YouTube links
@dp.message(F.text.contains("youtube.com") | F.text.contains("youtu.be"))
async def download_video(message: Message):
    url = message.text.strip()

    try:
        await message.answer("⏳ Downloading the video... Please wait!")

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # Download the best quality
        file_path = stream.download()

        # Send the video as a document
        await bot.send_document(
            message.chat.id,
            document=open(file_path, "rb"),
            caption=f"🎥 {yt.title}\n\nEnjoy your video!"
        )

        # Clean up the file
        os.remove(file_path)

    except Exception as e:
        await message.answer(f"❌ Oops! Something went wrong:\n{str(e)}")

# Catch-all handler for invalid messages
@dp.message()
async def invalid_message(message: Message):
    await message.answer("❌ Please send a valid YouTube link.")

# Start the bot
async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
