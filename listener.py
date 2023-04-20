import telegram
import requests
import time


def request_last_message(token: str = ""):
    # Get the file ID for the photo
    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/getUpdates"
    )

    d = response.json()
    results = d["result"]

    last_message = results[-1]["message"]

    return last_message


def download_photo(token: str = "", file_id: str = "") -> int:
    # Get the file path for the photo
    response = requests.post(
        f"https://api.telegram.org/bot{token}/getFile",
        data={"file_id": file_id}
    )
    file_path = response.json()["result"]["file_path"]

    # Download the photo
    photo_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
    response = requests.get(photo_url)

    # Save the photo to a file
    stat_code = response.status_code
    print("RESPONSE STATUS CODE: ", stat_code)
    if stat_code == 200:
        with open("photo.jpg", "wb") as f:
            f.write(response.content)
    else:
        print(f"Error downloading photo: {response.text}")

    return stat_code


def send_message(token: str = "", chat_id: str = ""):
    message = "Photo in processing \U0001F63C"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # this sends the message


if __name__ == "__main__":
    # Replace YOUR_TOKEN with your actual bot token
    bot_token = "6073178391:AAHAbkwD9HJnkafy0wKOZTNINMBp2e7PpkY"

    photo_messages_ids = []
    while True:
        last_message = request_last_message(bot_token)
        if "photo" in last_message.keys():
            photo_message_id = last_message["message_id"]

            if photo_message_id not in photo_messages_ids:
                file_id = last_message["photo"][-1]["file_id"]
                stat_code = download_photo(bot_token, file_id)

                if stat_code == 200:
                    chat_id = last_message["chat"]["id"]
                    send_message(bot_token, chat_id)
                    photo_messages_ids.append(photo_message_id)

        time.sleep(1.0)
