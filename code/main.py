# This file is specifically for "front-end" code that is not part of any module.
# It is intended to be run directly.
# It should not contain any business logic or module-specific code.
# It should only handle high-level application flow, user interaction, and orchestration of modules.

# Import necessary modules/files

import rngFunctions




def main():
    print("Welcome to the Application!")
    # Here you would typically initialize modules and start the application flow.
    # For example:
    # module_a.initialize()
    # module_b.start()
    print("Application is running...")

    #print(f"{rngFunctions.generate_random_number(1, 100, 0.1)}")

    rngFunctions.generate_random_number(1, 100, 0.1)

if __name__ == "__main__":
    main()