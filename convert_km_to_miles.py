# Simple Unit Converter: Kilometers to Miles

def convert_km_to_miles():
    try:
        # Ask the user to input a distance in kilometers
        km = input("Enter the distance in kilometers: ")
        
        # Convert the input to a float
        km = float(km)
        
        # Convert kilometers to miles (1 mile = 1.60934 km)
        miles = km / 1.60934
        
        # Print the result in a user-friendly format
        print(f"{km} kilometers is approximately {miles:.2f} miles.")
    
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a numeric value for kilometers.")

# Run the function
convert_km_to_miles()
