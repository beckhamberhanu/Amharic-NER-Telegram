from telethon import TelegramClient
import pandas as pd
import os
from config import API_ID, API_HASH, PHONE_NUMBER, CHANNELS

# Initialize Telegram client
client = TelegramClient("session_name", API_ID, API_HASH)

async def fetch_messages():
    await client.start(PHONE_NUMBER)  # Start client
    all_messages = []

    for channel in CHANNELS:
        try:
            entity = await client.get_entity(channel)
            async for message in client.iter_messages(entity, limit=500):
                all_messages.append([
                    channel,
                    message.id,
                    message.date,
                    message.sender_id,
                    message.text
                ])
        except Exception as e:
            print(f"Error fetching from {channel}: {e}")

    # Convert to DataFrame
    df = pd.DataFrame(all_messages, columns=["Channel", "Message_ID", "Date", "Sender_ID", "Text"])

    # Save as CSV
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_messages.csv", index=False)
    print("✅ Data saved to data/raw_messages.csv")

# Run the script
with client:
    client.loop.run_until_complete(fetch_messages())