def convert(text):
    # Check if ":)" is in the input text
    if ":)" in text:
        # If found, replace ":)" with "🙂"
        text = text.replace(":)", "🙂")
        return text  # Return the modified text
    # Check if ":(" is in the input text
    elif ":(" in text:
        # If found, replace ":(" with "🙁"
        text = text.replace(":(", "🙁")
        return text  # Return the modified text
    else:
        # If neither emoticon is found, print a message
        print("You did not include a :) or :(")
        return False  # Indicate failure to convert

def main():
    # Continuously prompt the user for input until valid emoticons are included
    while True:
        # Prompt the user to enter text
        user_input = input("Please enter text: ")
        # Call the convert function to convert the input text
        converted_text = convert(user_input)
        # Check if conversion was successful (i.e., not False)
        if converted_text is not False:
            # If successful, print the converted text
            print(converted_text)
            # Exit the loop
            break
    
if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
