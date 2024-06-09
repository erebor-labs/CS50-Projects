import time

# Inform the user about the program's functionality
print("This program slows down the speed of the printed text.")

# Prompt the user to enter their text
print("Please enter your text:")

# Capture the user's input
inputted_text = input()

# Number of periods for effect
num_periods = 3

# Iterate through each character in the inputted text
for char in inputted_text:
    if char == ' ':  
        # Replace spaces with three periods
        for i in range(0, 3):
            print('.', end='', flush=True)  # Print a period without a newline and flush the output
            time.sleep(0.2)  # Pause for 0.2 seconds between each period
    else:
        # Print non-space characters
        print(char, end='', flush=True)  # Print the character without a newline and flush the output
        time.sleep(0.2)  # Pause for 0.2 seconds between each character

# Ensure the terminal cursor is on a new line after all characters are printed
print()
