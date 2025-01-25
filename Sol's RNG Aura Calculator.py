import tkinter as tk
from tkinter import ttk

# Comprehensive aura data with biome-specific probabilities
auras = {
    "Common": {"base": 1 / 2},
    "Uncommon": {"base": 1 / 4},
    "Good": {"base": 1 / 5},
    "Natural": {"base": 1 / 8},
    "Rare": {"base": 1 / 16},
    "Divinus": {"base": 1 / 32},
    "Crystallized": {"base": 1 / 64},
    "Rage": {"base": 1 / 128},
    "Topaz": {"base": 1 / 150},
    "Ruby": {"base": 1 / 350},
    "Forbidden": {"base": 1 / 404},
    "Emerald": {"base": 1 / 500},
    "Gilded": {"base": 1 / 512, "Sandstorm": 1 / 128, "Glitched": 1 / 128},
    "Ink": {"base": 1 / 700},
    "Jackpot": {"base": 1 / 777, "Sandstorm": 1 / 194, "Glitched": 1 / 194},
    "Sapphire": {"base": 1 / 800},
    "Aquamarine": {"base": 1 / 900},
    "Wind": {"base": 1 / 900, "Windy": 1 / 300, "Glitched": 1 / 300},
    "Diaboli": {"base": 1 / 1004},
    "Precious": {"base": 1 / 1024},
    "Glock": {"base": 1 / 1700},
    "Magnetic": {"base": 1 / 2048},
    "Ash": {"base": 1 / 2300},
    "Glacier": {"base": 1 / 2304, "Snowy": 1 / 768, "Glitched": 1 / 768},
    "Player": {"base": 1 / 3000},
    "Fault": {"base": 0 / 1, "Glitched": 1 / 3000},
    "Sidereum": {"base": 1 / 4096},
    "Bleeding": {"base": 1 / 4444},
    "Solar": {"base": 1 / 50000, "Day": 1 / 5000, "Glitched": 1 / 5000},
    "Lunar": {"base": 1 / 50000, "Night": 1 / 5000, "Glitched": 1 / 5000},
    "Starlight": {"base": 1 / 50000, "Starfall": 1 / 5000, "Glitched": 1 / 5000},
    "Star Rider": {"base": 1 / 50000, "Starfall": 1 / 5000, "Glitched": 1 / 5000},
    "Flushed": {"base": 1 / 6900},
    "Hazard": {"base": 1 / 7000, "Corruption": 1 / 1400, "Glitched": 1 / 1400},
    "Quartz": {"base": 1 / 8192},
    "Lost Soul": {"base": 1 / 9200},
    "Undead": {"base": 1 / 12000, "Hell": 1 / 2000, "Glitched": 1 / 2000},
    "Corrosive": {"base": 1 / 12000, "Corruption": 2400, "Glitched": 1 / 2400},
    "Rage : Heated": {"base": 1 / 12800},
    "Leak": {"base": 1 / 14000},
    "Powered": {"base": 1 / 16384},
    "Aquatic": {"base": 1 / 40000},
    "Flushed : Lobotomy": {"base": 1 / 69000},
    "Hazard : Rays": {"base": 1 / 70000, "Corruption": 1 / 14000, "Glitched": 1 / 14000},
    "Nautilus": {"base": 1 / 70000},
    "Permafrost": {"base": 1 / 73500, "Snowy": 1 / 24500, "Glitched": 1 / 24500},
    "Stormal": {"base": 1 / 90000, "Windy": 1 / 30000, "Glitched": 1 / 30000},
    "Exotic": {"base": 1 / 99999},
    "Diaboli : Void": {"base": 1 / 100400},
    "Undead : Devil": {"base": 1 / 120000, "Hell": 1 / 20000, "Glitched": 1 / 20000},
    "Comet": {"base": 1 / 120000, "Starfall": 1 / 12000, "Glitched": 1 / 12000},
    "Jade": {"base": 1 / 125000},
    "Aether": {"base": 1 / 180000},
    "Bounded": {"base": 1 / 200000},
    "Celestial": {"base": 1 / 350000},
    "Kyawthuite": {"base": 1 / 850000},
    "Arcane": {"base": 1 / 1000000},
    "Magnetic : Reverse Polarity": {"base": 1 / 1024000},
    "Rage : Brawler": {"base": 1 / 1280000},
    "Undefined": {"base": 1 / 1111000, "Null": 1 / 1111, "Glitched": 1 / 1111},
    "Astral": {"base": 1 / 1336000, "Corruption": 1 / 267200, "Glitched": 1 / 267200},
    "Gravitational": {"base": 1 / 2000000},
    "Unbound": {"base": 1 / 2000000},
    "Virtual": {"base": 1 / 2500000},
    "Savior": {"base": 1 / 3200000},
    "Aquatic : Flame": {"base": 1 / 4000000},
    "Poseidon": {"base": 1 / 4000000, "Rainy": 1 / 1000000, "Glitched": 1 / 1000000},
    "Zeus": {"base": 1 / 4500000},
    "Solar : Solstice": {"base": 1 / 5000000, "Day": 1 / 500000, "Glitched": 1 / 500000},
    "Galaxy": {"base": 1 / 5000000, "Starfall": 1 / 500000, "Glitched": 1 / 500000},
    "Lunar : Full Moon": {"base": 1 / 5000000, "Night": 1 / 500000, "Glitched": 1 / 500000},
    "Twilight": {"base": 1 / 6000000, "Night": 1 / 600000, "Glitched": 1 / 600000},
    "Origin": {"base": 1 / 6500000},
    "Hades": {"base": 1 / 6666666, "Hell": 1 / 1111111, "Glitched": 1 / 1111111},
    "Celestial Divine": {"base": 1 / 7000000},
    "Hyper-Volt": {"base": 1 / 7500000},
    "Nihility": {"base": 1 / 9000000, "Null": 1 / 9000, "Glitched": 1 / 9000},
    "Starscourge": {"base": 1 / 10000000, "Starfall": 1 / 1000000, "Glitched": 1 / 1000000},
    "Sailor": {"base": 1 / 12000000, "Rainy": 1 / 3000000, "Glitched": 1 / 3000000},
    "Glitch": {"base": 0 / 1, "Glitched": 1 / 12210110},
    "Stormal : Hurricane": {"base": 1 / 13500000, "Windy": 1 / 4500000, "Glitched": 1 / 4500000},
    "Sirius": {"base": 1 / 14000000, "Starfall": 1 / 1400000, "Glitched": 1 / 1400000},
    "Arcane : Legacy": {"base": 1 / 15000000},
    "Chromatic": {"base": 1 / 20000000},
    "Aviator": {"base": 1 / 24000000},
    "Arcane : Dark": {"base": 1 / 30000000},
    "Ethereal": {"base": 1 / 35000000},
    "Overseer": {"base": 1 / 45000000},
    "Exotic : Apex": {"base": 1 / 49999500},
    "Matrix": {"base": 1 / 50000000},
    "Twilight : Iridescent Memory": {"base": 1 / 60000000, "Night": 1 / 6000000, "Glitched": 1 / 6000000},
    "Sailor : Flying Dutchman": {"base": 1 / 80000000, "Rainy": 1 / 20000000, "Glitched": 1 / 20000000},
    "CHROMATIC : GENESIS": {"base": 1 / 99999999},
    "STARSCOURGE : RADIANT": {"base": 1 / 100000000, "Starfall": 1 / 10000000, "Glitched": 1 / 10000000},
    "OVERTURE": {"base": 1 / 150000000},
    "SYMPHONY": {"base": 1 / 175000000},
    "IMPEACHED": {"base": 1 / 200000000},
    "OPPRESSION": {"base": 0 / 1, "Glitched": 1 / 220000000},
    "ARCHANGEL": {"base": 1 / 250000000},
    "OVERTURE : HISTORY": {"base": 1 / 300000000},
    "BLOODLUST": {"base": 1 / 300000000, "Hell": 1 / 50000000, "Glitched": 1 / 50000000},
    "ATLAS": {"base": 1 / 360000000, "Sandstorm": 1 / 90000000, "Glitched": 1 / 90000000},
    "ABYSSAL HUNTER": {"base": 1 / 400000000, "Rainy": 1 / 100000000, "Glitched": 1 / 100000000},
    "GARGANTUA": {"base": 1 / 430000000, "Starfall": 1 / 43000000, "Glitched": 1 / 43000000},
    "APOSTOLOS": {"base": 1 / 444000000},
    "RUINS": {"base": 1 / 500000000},
    "MATRIX : OVERDRIVE": {"base": 1 / 503000000},
    "SOVEREIGN": {"base": 1 / 750000000},
    "AEGIS": {"base": 1 / 825000000},
    "LUMINOSITY": {"base": 1 / 1200000000},
    "[Limited] PUMP": {"base": 0 / 1, "Pumpkin Moon": 1 / 200000, "Glitched": 1 / 200000},
    "[Limited] LUNAR : NIGHTFALL": {"base": 0 / 1, "Graveyard": 1 / 3000000, "Glitched": 1 / 3000000},
    "[Limited] VITAL": {"base": 0 / 1, "Pumpkin Moon": 1 / 6000000, "Glitched": 1 / 6000000},
    "[Limited] MOONFLOWER": {"base": 0 / 1, "Pumpkin Moon": 1 / 10000000, "Glitched": 1 / 10000000},
    "[Limited] CRYPTFIRE": {"base": 0 / 1, "Graveyard": 1 / 21000000, "Glitched": 1 / 21000000},
    "[Limited] SOUL HUNTER": {"base": 0 / 1, "Graveyard": 1 / 40000000, "Glitched": 1 / 40000000},
    "[Limited] DULLAHAN": {"base": 0 / 1, "Graveyard": 1 / 72000000, "Glitched": 1 / 72000000},
    "[Limited] NIGHTMARE SKY": {"base": 0 / 1, "Pumpkin Moon": 1 / 190000000, "Glitched": 1 / 190000000},
    "[Limited] HARVESTER": {"base": 0 / 1, "Graveyard": 1 / 666000000, "Glitched": 1 / 666000000},
    "[Limited] APOSTOLOS : VEIL": {"base": 0 / 1, "Pumpkin Moon": 1 / 800000000, "Graveyard": 1 / 800000000, "Glitched": 1 / 800000000},
    # Add more auras...
}

# List of biomes
biomes = ["Normal", "Sandstorm", "Starfall", "Hell", "Corruption", "Null", "Glitched", "Snowy", "Rainy", "Windy", "Day", "Night", "Graveyard", "Pumpkin Moon"]

def calculate_probability():
    aura = aura_var.get()
    biome = biome_var.get()
    luck_multiplier = float(luck_var.get())

    if aura in auras:
        base_prob = auras[aura].get(biome, auras[aura]["base"])
        adjusted_prob = base_prob * luck_multiplier
        if adjusted_prob == 0:
            result_var.set("Wrong Biome or Aura selected.")
        else:
            chance_interval = 1 / adjusted_prob
            final_percentage = adjusted_prob * 100
            result_var.set(f"1 in {int(chance_interval):,}\nChance: {final_percentage:.10f}%")
    else:
        result_var.set("Invalid aura selected.")

def reset_fields():
    aura_var.set('')
    biome_var.set('Normal')
    luck_var.set('1.0')
    result_var.set('')

# GUI setup
root = tk.Tk()
root.title("Sol's RNG Aura Calculator")
root.geometry("368x360")  # Exact size without extra bars
root.resizable(False, False)

# Themed styling
style = ttk.Style()
style.theme_use('clam')  # Use a clean and modern theme
style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=5)
style.configure('TLabel', font=('Helvetica', 10), padding=5)

# Main Frame
main_frame = ttk.Frame(root, padding=10)
main_frame.grid(column=0, row=0, sticky="NSEW")

# Aura selection
ttk.Label(main_frame, text="Select Aura:").grid(column=0, row=0, padx=10, pady=5, sticky="W")
aura_var = tk.StringVar()
aura_menu = ttk.Combobox(main_frame, textvariable=aura_var, state="readonly", width=30)
aura_menu['values'] = list(auras.keys())
aura_menu.grid(column=1, row=0, padx=10, pady=5)

# Biome selection
ttk.Label(main_frame, text="Select Biome:").grid(column=0, row=1, padx=10, pady=5, sticky="W")
biome_var = tk.StringVar(value="Normal")
biome_menu = ttk.Combobox(main_frame, textvariable=biome_var, state="readonly", width=30)
biome_menu['values'] = biomes
biome_menu.grid(column=1, row=1, padx=10, pady=5)

# Luck multiplier
ttk.Label(main_frame, text="Luck Multiplier:").grid(column=0, row=2, padx=10, pady=5, sticky="W")
luck_var = tk.StringVar(value="1.0")
luck_entry = ttk.Entry(main_frame, textvariable=luck_var, width=33)
luck_entry.grid(column=1, row=2, padx=10, pady=5)

# Calculate button
calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate_probability)
calculate_button.grid(column=0, row=3, columnspan=2, pady=10)

# Reset button
reset_button = ttk.Button(main_frame, text="Reset", command=reset_fields)
reset_button.grid(column=0, row=4, columnspan=2, pady=5)

# Result display
result_var = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result_var, relief="groove", anchor="center", font=("Helvetica", 12, "bold"), background="#f0f0f0")
result_label.grid(column=0, row=5, columnspan=2, pady=10, sticky="EW")

# Footer for credits
footer_label = tk.Label(root, text="made with love @ reedzylx on discord\ndon't forget to visit https://discord.gg/solsrng", fg="gray", font=("Arial", 8))
footer_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
