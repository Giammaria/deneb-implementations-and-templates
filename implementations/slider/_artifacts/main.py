import csv
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Define the number of listings to generate
num_listings = 1000

# Open a CSV file to write the data
with open('real_estate_listings.csv', 'w', newline='') as csvfile:
    fieldnames = ['Property ID', 'Listing Agent ID', 'Listing Date', 'Property Type',
                  'Address', 'City', 'State', 'ZIP Code', 'Country', 'Price',
                  'Number of Bedrooms', 'Number of Bathrooms', 'Square Footage',
                  'Lot Size', 'Year Built', 'Amenities', 'Description', 'Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Generate fake data for each listing
    for i in range(num_listings):
        property_id = i + 1
        listing_agent_id = fake.random_int(min=1000, max=9999)
        listing_date = fake.date_between(start_date='-1y', end_date='today')
        property_type = fake.random_element(elements=('Single Family Home', 'Condo', 'Apartment'))
        address = fake.street_address()
        city = fake.city()
        state = fake.state_abbr()
        zip_code = fake.zipcode()
        country = 'USA'
        price = fake.random_int(min=100000, max=3000000)
        bedrooms = fake.random_int(min=1, max=10)
        if price <= 1000000:
            bathrooms = fake.random_int(min=1, max=3)
        else:
            bathrooms = fake.random_int(min=2, max=5)
        square_footage = fake.random_int(min=500, max=10000) if price <= 1000000 else fake.random_int(min=2000, max=15000)
        lot_size = fake.random_int(min=5000, max=50000)
        year_built = fake.random_int(min=1950, max=2022)
        amenities = fake.random_elements(elements=('Swimming Pool', 'Fireplace', 'Garden', 'Garage', 'Gym'), unique=True)
        amenities_str = ', '.join(amenities)
        description = fake.text(max_nb_chars=200)
        status = fake.random_element(elements=('Active', 'Pending', 'Sold'))

        writer.writerow({
            'Property ID': property_id,
            'Listing Agent ID': listing_agent_id,
            'Listing Date': listing_date,
            'Property Type': property_type,
            'Address': address,
            'City': city,
            'State': state,
            'ZIP Code': zip_code,
            'Country': country,
            'Price': price,
            'Number of Bedrooms': bedrooms,
            'Number of Bathrooms': bathrooms,
            'Square Footage': square_footage,
            'Lot Size': lot_size,
            'Year Built': year_built,
            'Amenities': amenities_str,
            'Description': description,
            'Status': status
        })

print("Dataset generation complete. CSV file saved as 'real_estate_listings.csv'")
