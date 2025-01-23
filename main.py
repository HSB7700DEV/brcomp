import os
from pytube import YouTube
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Replace with your bot token
BOT_TOKEN = "7697105902:AAHf9cqxbhpOiWTZqdyPKHjY8aNZwYkktMo"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Command: /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Welcome to the YouTube Downloader Bot! 🎥\nSend me a YouTube link, and I'll download the video for you.")

# Handle YouTube links
@dp.message_handler(lambda message: "youtube.com" in message.text or "youtu.be" in message.text)
async def download_video(message: types.Message):
    url = message.text.strip()

    try:
        await message.reply("⏳ Downloading the video... Please wait!")

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # Download the best quality
        file_path = stream.download()

        # Send the video as a document
        await bot.send_document(
            message.chat.id,
            open(file_path, "rb"),
            caption=f"🎥 {yt.title}\n\nEnjoy your video!"
        )

        # Clean up the file
        os.remove(file_path)

    except Exception as e:
        await message.reply(f"❌ Oops! Something went wrong:\n{str(e)}")

# Catch-all handler for non-YouTube messages
@dp.message_handler()
async def invalid_message(message: types.Message):
    await message.reply("❌ Please send a valid YouTube link.")

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
