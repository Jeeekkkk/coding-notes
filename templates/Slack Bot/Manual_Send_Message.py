import requests
import sys
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

channels_url = 'https://slack.com/api/conversations.list'
message_url = 'https://slack.com/api/chat.postMessage'
headers = {
    'Authorization': f'Bearer {BOT_TOKEN}',
    'Content-Type': 'application/json',
}

def find_channel(name):
    # Call channel names
    try:
        channel_response = requests.get(channels_url,headers=headers)
        channel_response.raise_for_status()
        channel_data = channel_response.json()
        if not channel_data.get("ok"):
            print("Slack API error:",channel_data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit()
    # Search channel names
    for ch in channel_data["channels"]:
        if ch["name"] == name:
            ch_id = ch["id"]
            if not ch_id:
                print("Error: Channel ID not found")
                sys.exit()
            return ch_id

def load_tickets(file_location):
    try:
        df = pd.read_csv(file_location)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit()
    # Filter
    df_filtered = df[df["status"]=="Open"]
    return df_filtered

def format_rows(df):
    lines = []
    for _,row in df.iterrows():
        lines.append(f"id {row['id']}: title {row['title']}")
    return "\n".join(lines)

def send_message(channel,text):
    payload = {
    'channel': channel,
    'text': text,
    }
    # Send message
    try:
        response = requests.post(message_url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data.get("ok"):
            print("Slack API error:",data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit()


# Call channels
channel_id = find_channel('slack_bot')
open_file = load_tickets(r'C:\Users\jaked\Documents\Personal-private-repo\Python Files\Slack Bot\Samples\tickets.csv')
format_text = format_rows(open_file)
send_message(channel_id,format_text)