def einstein_calc(mass):
    light_speed = 300_000_000
    energy = mass * light_speed ** 2
    return energy

def find_mass():
    mass = int(input("Please enter the mass of your object: "))
    return mass

def main():
    mass = find_mass()  # Call find_mass to get the mass
    energy = einstein_calc(mass)  # Call einstein_calc with the mass
    print("Energy equivalent of mass:", energy)

if __name__ == "__main__":
    main()

