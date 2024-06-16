def get_coin_value():
    # Function to get a valid coin value from the user
    while True:  # Infinite loop to repeatedly prompt the user until a valid input is given
        try:
            coin = int(input("Insert Coin: "))  # Prompt the user to input a coin value and convert it to an integer
            if coin == 5 or coin == 10 or coin == 25:  # Check if the entered coin is one of the valid values (5, 10, or 25)
                return coin  # If valid, return the coin value
            else:
                break  # If the coin value is not valid, break out of the loop
        except ValueError:  # Handle the case where the input is not an integer
            print("Invalid input. Please enter an integer.")  # Inform the user of the invalid input

def main():
    # Main function to simulate the vending machine coin input process
    price = 50  # The price of the item is 50 cents
    amount_paid = 0  # Initialize the amount paid by the user to 0
    
    # Loop until the total amount paid is at least equal to the price
    while amount_paid < price:
        print(f"Amount Due: {price - amount_paid}")  # Display the remaining amount due
        coin = get_coin_value()  # Get a valid coin value from the user
        if coin in [5, 10, 25]:  # Check again if the coin is valid (this is redundant and can be removed)
            amount_paid += coin  # Add the coin value to the total amount paid
    
    # Calculate and display the change owed to the user
    change = amount_paid - price  # Calculate the change by subtracting the price from the amount paid
    print(f"Change Owed: {change}")  # Print the change owed to the user

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function
