# Rename file later on

import random, time

def generate_random_number(start, end, delay):
    """Generate a random number between start and end (inclusive)."""

    numberToFind = random.randint(start, end)
    attempts = 0
    print(f"Searching between {start} and {end}")
    while True:
        
        search = random.randint(start, end)
        attempts = attempts + 1
        
        print(f"Guessing number: {search}")
        time.sleep(delay)
        if search == numberToFind:
            print(f"Found the number: {search}. Took {attempts} attempts.")
            break

    return search, attempts

