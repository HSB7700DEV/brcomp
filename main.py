import telebot
from pytube import YouTube

# Replace with your Telegram Bot Token
BOT_TOKEN = "7697105902:AAHf9cqxbhpOiWTZqdyPKHjY8aNZwYkktMo"
bot = telebot.TeleBot(BOT_TOKEN)

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the YouTube Downloader Bot! 🎥\nSend me a YouTube link, and I'll download the video for you.")

# Handle YouTube URLs
@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text

    # Check if it's a valid YouTube URL
    if "youtube.com" in url or "youtu.be" in url:
        try:
            bot.reply_to(message, "Downloading the video... Please wait a moment! ⏳")

            # Use pytube to download the video
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()  # Get the best quality stream
            file_path = stream.download()  # Download the video to the current directory

            # Send the video file to the user
            with open(file_path, "rb") as video:
                bot.send_video(message.chat.id, video, caption=f"Here's your video: {yt.title} 🎉")

        except Exception as e:
            bot.reply_to(message, f"❌ Oops! Something went wrong:\n{str(e)}")
    else:
        bot.reply_to(message, "❌ Please send a valid YouTube link.")

# Start the bot
print("Bot is running...")
bot.infinity_polling()
