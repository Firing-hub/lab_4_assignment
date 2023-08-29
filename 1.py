# Flight table data
flight_table = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
]

def get_flight_details(input_value, input_type):
    if input_type == "Flight ID":
        for flight in flight_table:
            if flight["Flight ID"] == input_value:
                return flight
    elif input_type == "Source":
        matching_flights = [flight for flight in flight_table if flight["From"] == input_value]
        return matching_flights
    elif input_type == "Destination":
        matching_flights = [flight for flight in flight_table if flight["To"] == input_value]
        return matching_flights
    else:
        return None

# User input
user_input_type = input("Enter input type (Flight ID / Source / Destination): ").strip()
user_input_value = input("Enter input value: ").strip()

# Retrieve and display flight details
if user_input_type in ["Flight ID", "Source", "Destination"]:
    result = get_flight_details(user_input_value, user_input_type)
    if result:
        if isinstance(result, list):
            print("Matching flights:")
            for flight in result:
                print(flight)
        else:
            print("Flight details:")
            print(result)
    else:
        print("No matching flights found.")
else:
    print("Invalid input type. Please enter 'Flight ID', 'Source', or 'Destination'.")
