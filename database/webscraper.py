import requests
from bs4 import BeautifulSoup
import schedule
import time

# Function to scrape traffic information
def scrape_traffic_laws():
    url = "https://law.lis.virginia.gov/vacodefull/title46.2/chapter8/"
    try:
        # Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant traffic law sections
        laws = soup.find_all('div', class_='section')
        
        # Process and store the data
        traffic_laws = []
        for law in laws:
            section_number = law.find('h3').text.strip() if law.find('h3') else "No Section Number"
            law_content = law.find('div', class_='fulltext').text.strip() if law.find('div', class_='fulltext') else "No Content"
            traffic_laws.append({
                "section": section_number,
                "content": law_content
            })

        # Save data to a file
        with open('traffic_laws.txt', 'w', encoding='utf-8') as file:
            for law in traffic_laws:
                file.write(f"Section: {law['section']}\n")
                file.write(f"Content: {law['content']}\n")
                file.write("-" * 80 + "\n")

        print("Traffic laws successfully scraped and saved.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

# Schedule the function to run every 12 hours
schedule.every(12).hours.do(scrape_traffic_laws)

print("Traffic law scraper is running. Press Ctrl+C to exit.")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
