import tkinter as tk

def coin_flip_params(parent):
    """Return a frame and variables for Coin Flip RNG."""
    frame = tk.Frame(parent)

    tk.Label(frame, text="Min Flips").grid(row=0, column=0)
    min_flips_var = tk.IntVar(value=10)
    tk.Entry(frame, textvariable=min_flips_var, width=5).grid(row=0, column=1)

    tk.Label(frame, text="Max Flips").grid(row=0, column=2)
    max_flips_var = tk.IntVar(value=100)
    tk.Entry(frame, textvariable=max_flips_var, width=5).grid(row=0, column=3)

    tk.Label(frame, text="Delay (s)").grid(row=0, column=4)
    delay_var = tk.DoubleVar(value=0.1)
    tk.Entry(frame, textvariable=delay_var, width=5).grid(row=0, column=5)

    vars_dict = {
        "min_flips": min_flips_var,
        "max_flips": max_flips_var,
        "delay": delay_var
    }

    return frame, vars_dict


def number_guess_params(parent):
    """Return a frame and variables for Number Guess RNG."""
    frame = tk.Frame(parent)

    tk.Label(frame, text="Start").grid(row=0, column=0)
    start_var = tk.IntVar(value=1)
    tk.Entry(frame, textvariable=start_var, width=5).grid(row=0, column=1)

    tk.Label(frame, text="End").grid(row=0, column=2)
    end_var = tk.IntVar(value=100)
    tk.Entry(frame, textvariable=end_var, width=5).grid(row=0, column=3)

    tk.Label(frame, text="Delay (s)").grid(row=0, column=4)
    delay_var = tk.DoubleVar(value=0.1)
    tk.Entry(frame, textvariable=delay_var, width=5).grid(row=0, column=5)

    vars_dict = {
        "start": start_var,
        "end": end_var,
        "delay": delay_var
    }

    return frame, vars_dict
