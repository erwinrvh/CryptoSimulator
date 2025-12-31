# gui.py
import tkinter as tk
from tkinter import scrolledtext
import threading
import random

from rng import rng_coinflip, rng_guess

# RNG module list/dictionary
RNG_MODULES = {
    "Coin Flip": rng_coinflip,
    "Number Guess": rng_guess,
}

def start_gui():
    app = tk.Tk()
    app.title("CryptoSimulator")
    app.geometry("500x350")

    log = scrolledtext.ScrolledText(app, width=60, height=15)
    log.pack(pady=10)

    def write_log(message):
        log.insert(tk.END, message)
        log.see(tk.END)

    def mine_task():
        # This prints to the TERMINAL
        # You can redirect it later into the GUI if you want.
        # Randomly pick RNG module from dictionary
        name, rng = random.choice(list(RNG_MODULES.items()))
        write_log(f"Starting mining with {name} RNG module...\n")
        
        rng.run(write_log)

        write_log(f"{name} RNG module finished mining.\n")

        # Optional: append final result to GUI log
        log.insert(tk.END, "Mining finished!\n")
        log.see(tk.END)

    def start_miner():
        threading.Thread(target=mine_task, daemon=True).start()

    start_button = tk.Button(app, text="Start Mining", command=start_miner)
    start_button.pack(pady=5)

    app.mainloop()
