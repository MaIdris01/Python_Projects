import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scraping data here.......
def scrape_school_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract school names and locations
        school_names = []
        school_locations = []
        
        schools = soup.find_all('div', class_='school-item')
        
        for school in schools:
            name = school.find('h2', class_='school-name').text.strip()
            location = school.find('p', class_='school-location').text.strip()
            
            school_names.append(name)
            school_locations.append(location)
        
        # Create a DataFrame to store the data
        data = pd.DataFrame({
            'School Name': school_names,
            'Location': school_locations
        })
        
        return data
    
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

url = '' 
school_data = scrape_school_data(url)

if school_data is not None:
    print("School data collected successfully:")
    print(school_data.head())
else:
    print("Failed to collect school data.")
