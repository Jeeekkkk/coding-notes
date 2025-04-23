# Run the bot with 'python Bolt_Send_Message.py'
# from cd '.\Documents\Personal-private-repo\Python Files\Slack Bot\'

# Kill the bot with CTRL + C

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
APP_TOKEN = os.getenv("APP_TOKEN")

app = App(token=BOT_TOKEN)

@app.message("Hello")
def handle_hello(message,say):
    say("Hey there! I'm alive!")


if __name__ == "__main__":
    socket_handler = SocketModeHandler(app,APP_TOKEN)
    socket_handler.start()

