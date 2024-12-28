import phonenumbers
from phonenumbers import geocoder, carrier

# Enter the phone number
phone_number = input("Enter the phone number (e.g., +1234567890): ")

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Get the carrier name
carrier_name = carrier.name_for_number(parsed_number, "en")

# Get the geolocation
geolocation = geocoder.description_for_number(parsed_number, "en")

# Print the results
print("Carrier Name:", carrier_name)
print("Geolocation:", geolocation)