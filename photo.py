import requests as requests

# Replace YOUR_TOKEN with your actual bot token
bot_token = "6073178391:AAHAbkwD9HJnkafy0wKOZTNINMBp2e7PpkY"
# Replace MESSAGE_ID with the actual message ID of the photo
message_id = "35"
# Get the file ID for the photo
response = requests.post(
    f"https://api.telegram.org/bot{bot_token}/getMessage",
    data={"chat_id": 472405778, "message_id": message_id},
)
file_id = response.json()["result"]["photo"][-1]["file_id"]  # get the last available photo
# Get the file path for the photo
response = requests.post(
    f"https://api.telegram.org/bot{bot_token}/getFile",
    data={"file_id": file_id},
)
file_path = response.json()["result"]["file_path"]
# Download the photo
photo_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
response = requests.get(photo_url)
# Save the photo to a file
if response.status_code == 200:
    with open("photo.jpg", "wb") as f:
        f.write(response.content)
    print("Photo downloaded successfully!")
else:
    print(f"Error downloading photo: {response.text}")