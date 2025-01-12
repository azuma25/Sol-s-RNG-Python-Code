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
        "SNOWY": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***It's kinda cold out here, because it's snowy right now!***\n***Snowy started {discord_timestamp}.***",
            "url": server_link,
            "color": 8766195,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Glacier, Permafrost"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328020569001820282/image.png"
                  }
             }
                  ],
            "attachments": []
                 },
        "RAINY": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***Prepare your umbrella, because it's pouring rain!***\n***Rainy started {discord_timestamp}.***",
            "url": server_link,
            "color": 869229,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Poseidon, Sailor, Sailor : Flying Dutchman, ABYSSAL HUNTER"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328025763533815869/image.png"
                  }
             }
                  ],
            "attachments": []
                 },
        "WINDY": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***Stay at home, it's Windy outside!***\n***Windy started {discord_timestamp}.***",
            "url": server_link,
            "color": 9619397,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Wind, Stormal, Stormal : Hurricane"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328025570981843029/image.png"
                  }
             }
            ],
            "attachments": []
        },
        "PUMPKIN MOON": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***The Pumpkin Moon shall rise again!***\n***Pumpkin Moon started {discord_timestamp}.***",
            "url": server_link,
            "color": 13400093,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Pump, Vital, Moonflower, NIGHTMARE SKY, APOSTOLOS : VEIL"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328042939401900074/image.png?ex=678543de&is=6783f25e&hm=b90e7572af7c13aee4d319e2d26072899ec16fd0f4822e4956853fc809ff3592&"
                  }
             }
            ],
            "attachments": []
        },
        "GRAVEYARD": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***Watch your steps, there are Tombstones everywhere!***\n***Graveyard started {discord_timestamp}.***",
            "url": server_link,
            "color": 5592405,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Lunar Nightfall, Cryptfire, SOUL HUNTER, DULLAHAN, HARVESTER, APOSTOLOS : VEIL"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328041915886735412/image.png?ex=678542ea&is=6783f16a&hm=495ea66289a001eb0fdb873cad9277fe02b74a563ca13918d2f81aaeb2eb4751&"
                  }
             }
            ],
            "attachments": []
        },
        "SAND STORM": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***Watch your six, Sand Storm is coming!***\n***Sand Storm started {discord_timestamp}.***",
            "url": server_link,
            "color": 14730147,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Gilded, Jackpot, ATLAS"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328035490464796672/image.png?ex=67853cee&is=6783eb6e&hm=f770f68c704c4af8046d369f6baa1e1a04e4431a54fd7c56b88669276ef83134&"
                  }
             }
            ],
            "attachments": []
        },
        "HELL": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***It's so hot out here, it feels like Hell!***\n***Hell started {discord_timestamp}.***",
            "url": server_link,
            "color": 6556941,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Undead, Undead : Devil, Hades, BLOODLUST"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328035931240009818/image.png?ex=67853d57&is=6783ebd7&hm=80e0d38d4767ba9d1a6eecef7a1fdb385abfab615095ff96eb276135947e3efc&"
                  }
             }
            ],
            "attachments": []
        },
        "STARFALL": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***Stars are falling from the sky, make a wish!***\n***Starfall started {discord_timestamp}.***",
            "url": server_link,
            "color": 2632855,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Starlight, Star Rider, Comet, Galaxy, Starscourge, Sirius, STARSCOURGE : RADIANT, GARGANTUA"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328036704178667624/image.png?ex=67853e10&is=6783ec90&hm=ea5547a37097239e7bbe45824ba7d12d997821eac2ed9333815614edf10c668c&"
                  }
             }
            ],
            "attachments": []
        },
        "CORRUPTION": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***I can't deal with these amounts of spreading Corruptions!***\n***Corruption started {discord_timestamp}.***",
            "url": server_link,
            "color": 9771471,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Hazard, Corrosive, Hazard : Rays, Astral, IMPEACHED"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328036907913056348/image.png?ex=67853e40&is=6783ecc0&hm=57c53a9021fb94dce774fbf553db69fe3ec3ae20d4f01d692d49a3890f196354&"
                  }
             }
            ],
            "attachments": []
        },
        "NULL": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***It's too dark out here, what happened?***\n***Null started {discord_timestamp}.***",
            "url": server_link,
            "color": 2105376,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Native Auras : Undefined, Nihility"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328039614908207286/image.png?ex=678540c5&is=6783ef45&hm=7d978431f96a3d7e3dad9cee7cba3f71386ea5f919257fda6ad1bc961daacf76&"
                  }
             }
            ],
            "attachments": []
        },
        "GLITCHED": {
            "content": None,
            "embeds": [
             {
            "title": "e99a18c428cb38d5f260853678922e03",
            "description": f"***5d41402abc4b2a76b9719d911017c592***\n***Glitched 983cd24fb0d69 {discord_timestamp}.***",
            "url": server_link,
            "color": 16777215,
            "author": {
                "name": "45c48cce2e2d7fbdea1afc51c7c6ad26",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"16891f84e7b : Fault, Glitch, OPPRESSION"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328039908803346544/image.png?ex=6785410c&is=6783ef8c&hm=6645cb34e951034fe39c76b59154c06cb8aea9f3c2ecb988959499b82dbd5258&"
                  }
             }
            ],
            "attachments": []
        },
        "NORMAL": {
            "content": None,
            "embeds": [
             {
            "title": "Click this to join the private server!",
            "description": f"***Seems like everything is back to Normal.***\n***Previous biome just ended {discord_timestamp}.***",
            "url": server_link,
            "color": 16773052,
            "author": {
                "name": "Reedzylx - Sol's RNG Biome Announcer",
                "url": "https://guns.lol/reedzylx",
                "icon_url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328070150850744382/reed_alter.png?ex=67855d36&is=67840bb6&hm=518c6902adbe2233c82d63abeed980a91072bba1a471c5039ce33eaaf4fa1dfe&"
                  },
            "footer": {
            "text": f"Thanks for the visit!"
                  },
            "image": {
            "url": "https://cdn.discordapp.com/attachments/1312380078545702962/1328041335822749746/image.png?ex=67854260&is=6783f0e0&hm=6a9c00872e138b82d46c4dd1582874ef19006b923eed7ecf3e75a5f7f2d7e3a2&"
                  }
             }
            ],
            "attachments": []
        }
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
