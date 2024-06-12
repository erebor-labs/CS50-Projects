def energy_calc (m: int):
    """
    Calculate the energy equivalent of a given mass using E = mc^2.
    
    Parameters:
    m (int): The mass of the object in kilograms.
    
    Returns:
    int: The equivalent energy in Joules.
    """
    # Speed of light in meters per second
    c = 300_000_000
    # Calculate energy using the formula E = mc^2
    e = m * c ** 2
    # Return the calculated energy
    return e

# This block of code executes when the script is run as the main program
if __name__ == "__main__":
    # Prompt the user to input the mass of the object
    mass = int(input("What is the mass of the object (in kilograms)? "))
    # Calculate the equivalent energy using the energy_calc function
    energy = energy_calc(mass)
    # Print the result with commas for readability
    print(f"The equivalent energy is: {energy:,} joules")



