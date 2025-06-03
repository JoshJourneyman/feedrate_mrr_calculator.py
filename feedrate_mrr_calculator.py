# Helper function to safely get a float input within a valid range
def get_float(prompt, min=None, max=None):
    while True:
        try:
            value = float(input(prompt))
            if (min is not None and value < min) or (max is not None and value > max):
                print(f"Please enter a value between {min} and {max}.")
                continue
            return value
        except ValueError:
            print("Invalid input: Please enter a number (e.g., 1200 or 0.012).")

# Helper function to safely get an integer input within a valid range
def get_int(prompt, min=None, max=None):
    while True:
        try:
            value = int(input(prompt))
            if (min is not None and value < min) or (max is not None and value > max):
                print(f"Please enter a whole number between {min} and {max}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 2, 4, 6).")

# Main calculator loop
while True:
    print('\n--- CNC Feedrate and MRR Calculator ---')

    rpm = get_int('Enter spindle speed (RPM): ', min=100, max=12000)
    fpt = get_float('Enter feed per tooth (in): ', min=0.001, max=0.05)
    flutes = get_int('Enter number of flutes: ', min=1, max=10)
    width = get_float('Enter width of cut (in): ', min=0.01, max=5.0)
    depth = get_float('Enter depth of cut (in): ', min=0.01, max=1.0)

    feedrate = rpm * fpt * flutes
    mrr = width * depth * feedrate

    print('\n--- Machining Summary ---')
    print('Feedrate: ' + str(round(feedrate, 2)) + ' IPM')
    print('Material Removal Rate: ' + str(round(mrr, 2)) + ' in³/min')

    again = input('\nWould you like to calculate another? (yes/no): ').lower()
    if again != 'yes':
        print('Exiting program. See you next cycle!')
        break
