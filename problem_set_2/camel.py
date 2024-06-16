def convert_text(camel_text):
    # Initialize an empty list to hold the characters for the snake_case version
    snake_text = []

    # Iterate over each character in the input camelCase text
    for char in camel_text:
        # If the character is uppercase
        if char.isupper():
            # Append an underscore before the lowercase version of the uppercase character
            snake_text.append("_")
            snake_text.append(char.lower())
        else:
            # If the character is not uppercase, append it as is
            snake_text.append(char)
    
    # Join the list into a single string and print it
    print("".join(snake_text))

def main():
    # Get input from the user
    get_text = input("camelCase: ")
    # Print the snake_case label without a newline
    print("snake_case: ", end="")
    # Call the convert_text function with the user's input
    convert_text(get_text)

# Check if this script is being run directly
if __name__ == "__main__":
    main()
