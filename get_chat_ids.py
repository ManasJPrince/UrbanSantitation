import requests

BOT_TOKEN = "8547426960:AAFqzeQkgt_R-jDL26pdStX_3asPMfbnR8s"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)
data = response.json()

if data.get("ok"):
    print("Updates found:")
    for result in data["result"]:
        chat = result.get("message", {}).get("chat", {})
        chat_id = chat.get("id")
        title = chat.get("title", "No Title (Private Chat)")
        type_ = chat.get("type")
        print(f"Chat ID: {chat_id} | Title: {title} | Type: {type_}")
else:
    print("Error:", data)
