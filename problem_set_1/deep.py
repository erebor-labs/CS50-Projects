def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    convert_answer = answer.lower().strip()

    if convert_answer == "42" or convert_answer == "forty-two" or convert_answer == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()


    






