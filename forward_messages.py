from telethon import TelegramClient, events
import asyncio

# Конфігурація
api_id = 123456  # Отримати на my.telegram.org
api_hash = "YOUR_API_HASH"  # Отримати на my.telegram.org
source_chat = -1001234567890  # ID чату-джерела або @username
target_chat = -1001234567890  # ID чату-призначення або @username

# Створення клієнта
client = TelegramClient("session_forward", api_id, api_hash)

@client.on(events.NewMessage(chats=source_chat))
async def forward_handler(event):
    try:
        # Пересилання повідомлення з усім контентом (текст, медіа, файли)
        await client.send_message(
            entity=target_chat,
            message=event.message,
            link_preview=False  # Вимкнути попередній перегляд посилань
        )
        print(f"✓ Переслано повідомлення: {event.message.id}")
    except Exception as e:
        print(f"✗ Помилка пересилання: {e}")

async def main():
    await client.start()
    print("🤖 Бот запущено!")
    print(f"📥 Джерело: {source_chat}")
    print(f"📤 Призначення: {target_chat}")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
