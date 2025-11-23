# gui.py
import tkinter as tk
from tkinter import scrolledtext
import threading
import rngFunctions

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
        rngFunctions.generate_random_number(1, 100, 0.1, log_callback=write_log)

        # Optional: append final result to GUI log
        log.insert(tk.END, "Mining finished!\n")
        log.see(tk.END)

    def start_miner():
        threading.Thread(target=mine_task, daemon=True).start()

    start_button = tk.Button(app, text="Start Mining", command=start_miner)
    start_button.pack(pady=5)

    app.mainloop()
