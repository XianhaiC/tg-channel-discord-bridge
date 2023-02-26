from telethon import TelegramClient, events, sync
from dotenv import load_dotenv
import os

load_dotenv()


# Replace the placeholders with your own API ID and API hash
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

# Replace the placeholders with your own phone number and session name
phone_number = '+18589523677'
session_name = 'discord-bridge-session'

# Create a new Telegram client instance
client = TelegramClient(session_name, api_id, api_hash)

# Connect to the Telegram API
client.connect()

# Send an authentication request to the Telegram API
client.send_code_request(phone_number)

# Wait for the user to enter the authentication code received via SMS or Telegram
auth_code = input('Enter the authentication code: ')

# Complete the authorization flow using the entered authentication code
client.sign_in(phone_number, auth_code)

# Get the authorization key for the user account
auth_key = client.session.auth_key

channel_username = 'discord-bridge-test'

# Use the authorization key to authenticate your user account and make API calls
print("Got auth key:", auth_key)

print("Channels found:")
for dialog in client.iter_dialogs():
    if dialog.is_channel:
        print(dialog.title)

# Define an event handler for new messages in the channel
@client.on(events.NewMessage(chats=channel_username))
async def handle_new_message(event):
    # Print the content of the new message to the console
    print(event.message.text)

# Connect to the Telegram API and start the event loop
with client:
    print("Listening to channel", channel_username)
    client.run_until_disconnected()
