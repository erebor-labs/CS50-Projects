def main():
    vowels = "aeiou"
    prompt = input("Input: ")
    result = ""

    for char in prompt:
        if char.lower() not in vowels:
            result += char

    print("Output:", result)

if __name__ == "__main__":
    main()