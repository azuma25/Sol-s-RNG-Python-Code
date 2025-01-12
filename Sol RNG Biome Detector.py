import tkinter as tk
from tkinter import ttk
import time
import pyperclip
import webbrowser
import tkinter.font as tkfont
import os
import requests
import configparser

# Dictionary mapping biomes to their specific messages
biome_messages = {
    "SNOWY": "-# Native Auras : Glacier, Permafrost",
    "RAINY": "-# Native Auras : Poseidon, Sailor, Sailor : Flying Dutchman, ABYSSAL HUNTER",
    "WINDY": "-# Native Auras : Wind, Stormal, Stormal : Hurricane",
    "PUMPKIN MOON": "-# Limited Auras : Pump, Vital, Moonflower, NIGHTMARE SKY, APOSTOLOS : VEIL",
    "GRAVEYARD": "-# Limited Auras : Lunar Nightfall, Cryptfire, SOUL HUNTER, DULLAHAN, HARVESTER, APOSTOLOS : VEIL",
    "SAND STORM": "-# Native Auras : Gilded, Jackpot, ATLAS",
    "HELL": "-# Native Auras : Undead, Undead : Devil, Hades, BLOODLUST",
    "STARFALL": "-# Native Auras : Starlight, Star Rider, Comet, Galaxy, Starscourge, Sirius, STARSCOURGE : RADIANT, GARGANTUA",
    "CORRUPTION": "-# Native Auras : Hazard, Corrosive, Hazard : Rays, Astral, IMPEACHED",
    "NULL": "-# Native Auras : Undefined, Nihility",
    "GLITCHED": "-# Native Auras : Fault, Glitch, OPPRESSION",
}

last_biome = None

# Function to read the current biome from Roblox logs
def get_current_biome():
    log_dir_path = os.path.expanduser("~/AppData/Local/Roblox/logs/")
    latest_log_file = None
    latest_log_time = 0

    # Find the latest log file based on the last modified time
    for filename in os.listdir(log_dir_path):
        file_path = os.path.join(log_dir_path, filename)
        file_time = os.path.getmtime(file_path)
        if file_time > latest_log_time:
            latest_log_time = file_time
            latest_log_file = file_path

    if not latest_log_file:
        return None

    try:
        with open(latest_log_file, 'r') as log_file:
            logs = log_file.readlines()
            for line in reversed(logs):
                if '"largeImage":{"hoverText":' in line:
                    biome = line.split('"largeImage":{"hoverText":')[1].split('"')[1].strip()
                    return biome
    except FileNotFoundError:
        return None

# Function to generate the message based on the current biome
def generate_message():
    global discord_timestamp, discord_timestamp_2
    server_link = link_entry.get()
    biome = get_current_biome()
    if not biome:
        output_label.config(text="Could not detect the current biome.")
        return None, None
    
    timestamp = int(time.time())  # Current Unix timestamp
    discord_timestamp = f"<t:{timestamp}:R>"  # Discord-compatible formatted timestamp
    biome_message = biome_messages.get(biome, "No specific message")  # Get the specific message for the biome
    
    if biome == "NORMAL":
        message = (f"> Ended : ***{discord_timestamp}***\n> *Thanks for the visit!*")
    else:
        message = (f"> Biome : ***{biome}***\n> Started : ***{discord_timestamp}***\n<{server_link}>\n{biome_message}")
    
    output_label.config(text=f"Current Biome : {biome}")
    return message, biome

# Function to copy the generated message to clipboard
def copy_to_clipboard():
    message, _ = generate_message()
    if message:
        pyperclip.copy(message)
        output_label.config(text="Message copied to clipboard!")

def send_to_webhook(message, biome, discord_timestamp, server_link):
    webhook_url = webhook_entry.get()
    if webhook_url:
        embed_map = {
            # Embed map content here...
        }

        embed = embed_map.get(biome, {"content": None, "embeds": [{"title": "Biome Detected", "description": message, "color": 0x00FF00}], "attachments": []})

        response = requests.post(webhook_url, json=embed)
        if response.status_code == 204:
            output_label.config(text="Message sent to Discord webhook!")
        else:
            output_label.config(text="Failed to send message to Discord webhook.")

# Function to periodically check the biome and update the message
def check_biome_periodically():
    global last_biome
    message, biome = generate_message()
    if biome and biome != last_biome:
        last_biome = biome
        send_to_webhook(message, biome, discord_timestamp, link_entry.get())
    root.after(2000, check_biome_periodically)  # Schedule the function to run again after 2 seconds

# Function to save the configuration
def save_config():
    config = configparser.ConfigParser()
    config['Settings'] = {
        'PrivateServerLink': link_entry.get(),
        'DiscordWebhookURL': webhook_entry.get()
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    output_label.config(text="Configuration saved!")

# Function to load the configuration
def load_config():
    config = configparser.ConfigParser()
    if os.path.exists('config.ini'):
        config.read('config.ini')
        link_entry.insert(0, config.get('Settings', 'PrivateServerLink', fallback=''))
        webhook_entry.insert(0, config.get('Settings', 'DiscordWebhookURL', fallback=''))

# GUI Setup
root = tk.Tk()
root.title("Biome Message Generator")
root.geometry("440x240")
root.resizable(False, False)

# Themed styling
style = ttk.Style()
style.theme_use('clam')  # Use a clean and modern theme
style.configure('TButton', font=('Sarpanch Bold', 10, 'bold'), padding=5, background='white')
style.configure('TLabel', font=('Helvetica', 10), padding=5)

# Set the default font to Sarpanch
default_font = tkfont.Font(family="Sarpanch Bold", size=10)
root.option_add("*Font", default_font)

# Private Server Link
tk.Label(root, text="Private Server Link").grid(row=0, column=0, padx=5, pady=5, sticky="w")
link_entry = tk.Entry(root, width=29)
link_entry.grid(row=0, column=1, padx=7, pady=5)
link_entry.config(fg="black")

# Discord Webhook URL
tk.Label(root, text="Discord Webhook URL").grid(row=1, column=0, padx=5, pady=5, sticky="w")
webhook_entry = tk.Entry(root, width=29)
webhook_entry.grid(row=1, column=1, padx=7, pady=5)
webhook_entry.config(fg="black")

# Output Label
output_label = tk.Label(root, text="", fg="black")
output_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Copy Button
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, pady=5)

# Save Button
save_button = ttk.Button(root, text="Save Configuration", command=save_config)
save_button.grid(row=4, column=0, columnspan=2, pady=5)

# Footer for credits
footer_label = tk.Label(root, text="made with love @ reedzylx", fg="blue", font=("Verdana", 8), cursor="hand2")
footer_label.grid(row=5, column=0, columnspan=2, pady=0)
def open_reedzylx():
    webbrowser.open_new("https://guns.lol/reedzylx")

def open_solsrng():
    webbrowser.open_new("https://discord.com/invite/solsrng")

footer_label.bind("<Button-1>", lambda _: open_reedzylx())
footer_label = tk.Label(root, text="https://discord.gg/solsrng", fg="blue", font=("Verdana", 8), cursor="hand2")
footer_label.grid(row=6, column=0, columnspan=2, pady=0)
footer_label.bind("<Button-1>", lambda _: open_solsrng())

# Load the configuration on startup
load_config()

# Start the periodic biome check
check_biome_periodically()

root.mainloop()
