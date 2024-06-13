def convert(text):
    """
    This function accepts a string as input and returns the same input with any :)
    converted to 🙂 and any :( converted to 🙁. All other text is returned unchanged.
    """
    # Replace ":)" with "🙂"
    text = text.replace(":)", "🙂")
    # Replace ":(" with "🙁"
    text = text.replace(":(", "🙁")
    return text

def main():
    """
    This function prompts the user for input, calls the convert function on that input,
    and prints the result.
    """
    # Prompt the user to enter text
    user_input = input("Please enter text: ")
    # Call the convert function to convert the input text
    converted_text = convert(user_input)
    # Print the converted text
    print(converted_text)

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()