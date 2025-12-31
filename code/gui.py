# gui.py
import tkinter as tk
from tkinter import scrolledtext
import threading
import random

from rng import rng_coinflip, rng_guess
from gui_params import *

# RNG module list/dictionary
RNG_MODULES = {
    "Coin Flip": rng_coinflip,
    "Number Guess": rng_guess,
}

# TODO: When I click start mine, the options show up, but it should wait until I set it then start mining.
# Maybe have a separate "Set Parameters" button?
# Or even have random parameters instead of me setting them...
def start_gui():
    app = tk.Tk()
    app.title("CryptoSimulator")
    app.geometry("500x350")

    # Create frame and parameter variables for each RNG module
    param_frames = {}
    param_vars = {}

    param_frames["Coin Flip"], param_vars["Coin Flip"] = coin_flip_params(app)
    param_frames["Number Guess"], param_vars["Number Guess"] = number_guess_params(app)

    # Hide all frames initially
    for frame in param_frames.values():
        frame.forget() 

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

        # Hide all frames initially
        for frame in param_frames.values():
            frame.forget() 

        # Show only the selected module's frame
        if name in param_frames:
            param_frames[name].pack(pady=5)

        # Gather kwargs dynamically
        kwargs = {k: v.get() for k, v in param_vars.get(name, {}).items()}
        rng.run(write_log, **kwargs)
        
        # rng.run(write_log)

        write_log(f"{name} RNG module finished mining.\n")

        # Optional: append final result to GUI log
        log.insert(tk.END, "Mining finished!\n")
        log.see(tk.END)

    def start_miner():
        threading.Thread(target=mine_task, daemon=True).start()

    start_button = tk.Button(app, text="Start Mining", command=start_miner)
    start_button.pack(pady=5)

    app.mainloop()
