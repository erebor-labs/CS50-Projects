import time

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == "__main__":
    # Slow print the initial questions
    slow_print("What is the answer to the great question of Life?")
    slow_print("The Universe?")
    slow_print("Of Everything? ")

    # Get the user's input
    answer = input()

    # Convert the answer to lowercase
    convert_answer = answer.lower()

    # Check if the answer is correct
    if convert_answer == "42" or convert_answer == "forty-two" or convert_answer == "forty two":
        slow_print("Yes...", delay=0.2)
    else:
        slow_print("No...", delay=0.2)


    






