
# Telegram Bot Scheduler

This project provides a Telegram bot that sends scheduled messages based on predefined dates and times. The bot uses the Telebot and Schedule libraries to manage the bot interactions and scheduling.

## Prerequisites

1. Create a Telegram bot. You can use the [BotFather](https://core.telegram.org/bots#botfather) on Telegram to create a new bot.
2. Obtain the HTTP API token for your bot from BotFather.
3. Add your bot to a Telegram group chat.

## Files

- **chirie.py**: Contains configuration variables like the bot token, message templates, and scheduled dates.
- **main2.py**: The main script that initializes the bot, sets up the command handlers, schedules the messages, and starts the bot.
- **Dockerfile**: Defines the Docker image for this application.
- **requirements.txt**: Lists the required Python libraries.

## Usage

### 1. Update Configuration

Open the `chirie.py` file and replace the following variables with appropriate values:

- `botToken`: Your Telegram bot token.
- `excelLink`: The link to your Google Spreadsheet.
- `GoogleDriveFolder`: The link to your Google Drive folder.
- `chatId`: The chat ID where the bot should send messages.
- `messageText1`, `messageText2`, `messageText3`: Message templates with placeholders for the links.
- `day1`, `day2`, `day3`: The days of the month when the bot should send the corresponding messages.

### 2. Build the Docker Image

Navigate to the directory containing the project files and run the following command:

```bash
docker build -t telegram_bot_scheduler .
```

This command builds a Docker image named "telegram_bot_scheduler" using the provided `Dockerfile`.

### 3. Run the Docker Container

Once the image is built, you can run the container:

```bash
docker run --name telegram_bot_container telegram_bot_scheduler
```

This command starts the Telegram bot with the container named "telegram_bot_container". The bot will begin polling for incoming messages and will send scheduled messages based on the configuration in `chirie.py`.

## Dependencies

- Telebot: For managing the Telegram bot.
- Schedule: For scheduling messages at specific times.

## Conclusion

With the bot running, you can now interact with it on Telegram. Use `/excel` to get the spreadsheet link and `/folder` to get the Google Drive folder link. The bot will also send scheduled messages based on the dates defined in `chirie.py`.
