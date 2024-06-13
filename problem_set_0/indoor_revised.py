import time

# Messages
welcome_message = "This program converts all text to lowercase."
response_message = "Your text converted to lowercase is"
num_periods = 5  # Number of periods to print after the response message

# Print welcome message
print(welcome_message)  # Display the welcome message
time.sleep(0.5)  # Pause for 0.5 seconds to simulate a delay
print()  # Print a blank line for better readability

# Get input from the user
inputted_text = input("Please enter your text: ")  # Prompt the user to enter text
inputted_lower = inputted_text.lower()  # Convert the entered text to lowercase
print()  # Print a blank line for better readability

# Print response message with a delay for each period
print(response_message, end='', flush=True)  # Display the response message without a newline
for _ in range(num_periods):  # Loop to print periods one by one
    print('.', end='', flush=True)  # Print a period without a newline and flush the output immediately
    time.sleep(0.5)  # Pause for 0.5 seconds between each period

# New line after the dots
print()  # Move to a new line after the periods are printed
print()  # Print another blank line for better readability
time.sleep(0.5)  # Pause for 0.5 seconds

# Print the lowercase text with a delay between each character
for char in inputted_lower:  # Loop through each character in the lowercase text
    print(char, end='', flush=True)  # Print each character without a newline and flush the output immediately
    time.sleep(0.2)  # Pause for 0.2 seconds between each character

# Ensure the terminal cursor is on a new line
print()  # Move to a new line after all characters are printed
print()  # Print another blank line to ensure the cursor is correctly positioned for the next command
