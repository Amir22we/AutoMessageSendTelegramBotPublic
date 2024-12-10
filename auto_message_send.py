from telethon import TelegramClient
import asyncio

api_id = 
api_hash = ''  
phone_number = '' 

client = TelegramClient('session_name', api_id, api_hash)

chat_ids = [
    
]

message = ""

async def send_message(chat_id):
    try:
        await client.send_message(chat_id, message)
        print(f"Message sent to {chat_id}")
    except Exception as e:
        print(f"Failed to send message to {chat_id}: {e}")

async def send_messages_periodically():
    while True:
        await asyncio.gather(*[send_message(chat_id) for chat_id in chat_ids])
        await asyncio.sleep(20) 

async def main():
    await client.start() 
    await send_messages_periodically()

with client:
    client.loop.run_until_complete(main())
