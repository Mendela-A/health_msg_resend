from telethon import TelegramClient, events

api_id = 123456
api_hash = "API_HASH_HERE"

source_chat = "https://t.me/source_group"
target_chat = "https://t.me/target_group"

client = TelegramClient("session_forward", api_id, api_hash)

@client.on(events.NewMessage(chats=source_chat))
async def handler(event):
    await client.send_message(
        entity=target_chat,
        message=event.message
    )

client.start()
print("Пересилання запущено...")
client.run_until_disconnected()
