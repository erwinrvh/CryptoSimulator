# rng_coinflip.py
import random
import time

def amount_of_flips(min, max):
    random_flips = random.randint(min, max)
    return random_flips


def run(log_callback, **kwargs):
    log_callback("Coin Flip RNG starting...\n")

    # Extract parameters from kwargs or use defaults
    min_flips = kwargs.get("min_flips", 10)
    max_flips = kwargs.get("max_flips", 100)
    flips = kwargs.get("flips", amount_of_flips(min_flips, max_flips))
    delay = kwargs.get("delay", 0.1)

    time.sleep(delay)

    heads = 0
    tails = 0

    for i in range(flips):
        flip = random.choice(["Heads", "Tails"])
        if flip == "Heads":
            heads += 1
        else:
            tails += 1

        
        log_callback(f"Flip {i+1}: {flip}\n")
        time.sleep(delay)

    ratio = (heads / (heads + tails)) * 100
    
    log_callback(f"Heads/Tails Ratio: {ratio:.2f}%\n")
    log_callback(f"Final count → Heads: {heads}, Tails: {tails}\n")
