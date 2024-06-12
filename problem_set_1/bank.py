if __name__ == "__main__":
    greeting = input("Greeting: ").lstrip()

    if greeting.lower() == "hello":
        print("$0")
    elif greeting[0].lower() == "h":
        print("$20")
    else:
        print("$100")