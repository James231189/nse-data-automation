import requests
from bs4 import BeautifulSoup
import os
import time

def scrape_nse_oi_data():
    url = 'https://www.nseindia.com/option-chain'  # Replace with the correct URL
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Fetch the content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Parse the data to extract OI values (replace with actual HTML structure)
    # The IDs or classes need to be updated based on actual NSE website structure
    call_oi = soup.find('span', {'id': 'callOI'}).text.strip()  # Example ID, replace with actual
    put_oi = soup.find('span', {'id': 'putOI'}).text.strip()    # Example ID, replace with actual
    
    return call_oi, put_oi

def update_github_data():
    call_oi, put_oi = scrape_nse_oi_data()
    itm_strikes = f"{call_oi},{put_oi}"
    
    # Write the data to a file
    with open("itm_strikes.txt", "w") as file:
        file.write(itm_strikes)

if __name__ == "__main__":
    update_github_data()
    time.sleep(1)  # Wait a bit before closing
