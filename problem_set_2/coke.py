def get_coin_value():
    while True:
        try:
            coin = int(input("Insert Coin: "))
            if coin == 5 or coin == 10 or coin == 25:
                return coin
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    price = 50
    amount_paid = 0
    
    while amount_paid < price:
        print(f"Amount Due: {price - amount_paid}")
        coin = get_coin_value()
        if coin in [5, 10, 25]:
            amount_paid += coin
    
    change = amount_paid - price
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()

