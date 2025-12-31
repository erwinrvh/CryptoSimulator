# rng_coinflip.py
import random
import time

def run(log_callback):
    log_callback("Coin Flip RNG starting...\n")
    time.sleep(0.3)

    heads = 0
    tails = 0

    for i in range(20):
        flip = random.choice(["Heads", "Tails"])
        if flip == "Heads":
            heads += 1
        else:
            tails += 1

        
        log_callback(f"Flip {i+1}: {flip}\n")
        time.sleep(0.1)

    
    log_callback(f"Final count → Heads: {heads}, Tails: {tails}\n")
    log_callback("Coin Flip RNG done!\n")
