def format_file_name(fn: str) -> str:
    """
    Strip leading/trailing whitespace and convert the filename to lowercase.

    Parameters:
    fn (str): The original filename

    Returns:
    str: The formatted filename
    """
    return fn.strip().lower()

def get_file_ext(file_name: str) -> str:
    """
    Determine the media type based on the file extension.

    Parameters:
    file_name (str): The formatted filename

    Returns:
    str: The media type corresponding to the file extension, or
         "application/octet-stream" if the extension is not recognized
    """
    # Dictionary mapping file extensions to media types
    file_ext = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    # Check if the filename ends with any of the known extensions
    for ext, media_type in file_ext.items():
        if file_name.endswith(ext):
            return media_type
    # Return the default media type if no known extension is found
    return "application/octet-stream"

def main():
    """
    Main function to execute the program logic.
    Prompts the user for a filename, formats it, determines the media type,
    and prints the media type.
    """
    # Prompt the user to enter a filename
    file_name = input("Please enter a filename: ")
    # Format the filename
    formatted_file_name = format_file_name(file_name)
    # Determine the media type based on the file extension
    media_type = get_file_ext(formatted_file_name)
    # Print the media type
    print(media_type)

# Entry point of the script
if __name__ == "__main__":
    main()
