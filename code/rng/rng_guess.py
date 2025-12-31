import random, time

def run(log_callback, **kwargs):
    """Generate a random number between start and end (inclusive)."""

    # Extract parameters from kwargs or use defaults
    start = kwargs.get("start", 1)
    end = kwargs.get("end", 100)
    delay = kwargs.get("delay", 0.1)

    numberToFind = random.randint(start, end)
    attempts = 0

    if log_callback:
        log_callback(f"Searching between {start} and {end}\n")
    print(f"Searching between {start} and {end}")
    while True:
        
        search = random.randint(start, end)
        attempts = attempts + 1
        
        if log_callback:
            log_callback(f"Guessing number: {search}\n")
        print(f"Guessing number: {search}")
        
        time.sleep(delay)

        if search == numberToFind:
            
            if log_callback:
                log_callback(f"Found the number: {search}. Took {attempts} attempts.\n")
            print(f"Found the number: {search}. Took {attempts} attempts.")
            break

    return search, attempts

