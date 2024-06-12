def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the leading dollar sign ('$') using string slicing
    # Convert the remaining string to a float
    return float(d[1:])

def percent_to_float(p):
    # Remove the trailing percentage sign ('%') using string slicing
    # Convert the remaining string to a float and divide by 100 to get the percentage in decimal form
    return float(p[:-1]) / 100

main()

