import requests
from bs4 import BeautifulSoup
import os

def scrape_traffic_laws():
    url = "https://law.lis.virginia.gov/vacodefull/title46.2/chapter8/"
    try:
        print(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all <b> tags and <section> tags
        titles = soup.find_all('b')  # Extract all law titles
        bodies = soup.find_all('section', class_='body')  # Extract all law bodies

        # Ensure the number of titles matches the number of body sections
        if len(titles) != len(bodies):
            print(f"Warning: Titles ({len(titles)}) and bodies ({len(bodies)}) count mismatch.")

        # Create a directory for individual files
        folder_name = "traffic_laws"
        os.makedirs(folder_name, exist_ok=True)

        traffic_laws = {}
        for title, body in zip(titles, bodies):
            # Extract and clean the title
            law_title = title.text.strip()
            if not law_title.startswith("§"):  # Skip invalid titles
                continue
            # Extract the law number from the title
            law_number = law_title.split("§")[1].strip().split(" ")[0]  # Get everything after '§'
            law_number = law_number.replace(".", "_")  # Replace periods with underscores for filenames

            # Extract the body content
            law_content = "\n".join(p.text.strip() for p in body.find_all('p'))

            # Save law data in dictionary
            traffic_laws[law_number] = {
                "title": law_title,
                "content": law_content
            }

        # Save all laws to a single file
        with open('traffic_laws.txt', 'w', encoding='utf-8') as file:
            for law_number, law_data in traffic_laws.items():
                file.write(f"Law Number: {law_number}\n")
                file.write(f"Title: {law_data['title']}\n")
                file.write(f"Content:\n{law_data['content']}\n")
                file.write("-" * 80 + "\n")

        # Save each law to a separate file in the directory
        for law_number, law_data in traffic_laws.items():
            # Format the filename
            filename = f"{folder_name}/{law_number}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Title: {law_data['title']}\n")
                file.write(f"Content:\n{law_data['content']}\n")

        print(f"Traffic laws successfully scraped and saved. Individual files are in the '{folder_name}' folder.")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

# Run the scraper
scrape_traffic_laws()



""" import requests
from bs4 import BeautifulSoup
import os

def scrape_traffic_laws():
    url = "https://law.lis.virginia.gov/vacodefull/title46.2/chapter8/"
    try:
        print(f"Fetching data from {url}")
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all <b> tags and <section> tags
        titles = soup.find_all('b')  # Extract all law titles
        bodies = soup.find_all('section', class_='body')  # Extract all law bodies

        # Ensure the number of titles matches the number of body sections
        if len(titles) != len(bodies):
            print(f"Warning: Titles ({len(titles)}) and bodies ({len(bodies)}) count mismatch.")

        # Create a directory for individual files
        folder_name = "traffic_laws"
        os.makedirs(folder_name, exist_ok=True)

        traffic_laws = {}
        for title, body in zip(titles, bodies):
            # Extract and clean the title
            law_title = title.text.strip()
            if not law_title.startswith("§"):  # Skip invalid titles
                continue
            law_number = law_title.strip()  # Use the full law title as the unique key

            # Extract the body content
            law_content = "\n".join(p.text.strip() for p in body.find_all('p'))

            # Save law data in dictionary
            traffic_laws[law_number] = {
                "title": law_title,
                "content": law_content
            }

        # Save all laws to a single file
        with open('traffic_laws.txt', 'w', encoding='utf-8') as file:
            for law_number, law_data in traffic_laws.items():
                file.write(f"Law Number: {law_number}\n")
                file.write(f"Title: {law_data['title']}\n")
                file.write(f"Content:\n{law_data['content']}\n")
                file.write("-" * 80 + "\n")

        # Save each law to a separate file in the directory
        for law_number, law_data in traffic_laws.items():
            # Create a filename based on the law number
            filename = f"{folder_name}/{law_number.replace('§', '').replace('.', '_').strip()}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Title: {law_data['title']}\n")
                file.write(f"Content:\n{law_data['content']}\n")

        print(f"Traffic laws successfully scraped and saved. Individual files are in the '{folder_name}' folder.")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

# Run the scraper
scrape_traffic_laws() """



""" import requests
from bs4 import BeautifulSoup
import os

def scrape_traffic_laws():
    url = "https://law.lis.virginia.gov/vacodefull/title46.2/chapter8/"
    try:
        print(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all <b> tags and <section> tags
        titles = soup.find_all('b')  # Extract all law titles
        bodies = soup.find_all('section', class_='body')  # Extract all law bodies

        # Ensure the number of titles matches the number of body sections
        if len(titles) != len(bodies):
            print(f"Warning: Titles ({len(titles)}) and bodies ({len(bodies)}) count mismatch.")

        # Create a directory for individual files
        folder_name = "traffic_laws"
        os.makedirs(folder_name, exist_ok=True)

        traffic_laws = {}
        for title, body in zip(titles, bodies):
            # Extract and clean the title
            law_title = title.text.strip()
            if not law_title.startswith("§"):  # Skip invalid titles
                continue
            law_number = law_title.split(".")[0].strip()  # Extract law number

            # Extract the body content
            law_content = "\n".join(p.text.strip() for p in body.find_all('p'))

            # Save law data in dictionary
            traffic_laws[law_number] = {
                "title": law_title,
                "content": law_content
            }

        # Save all laws to a single file
        with open('traffic_laws.txt', 'w', encoding='utf-8') as file:
            for law_number, law_data in traffic_laws.items():
                file.write(f"Law Number: {law_number}\n")
                file.write(f"Title: {law_data['title']}\n")
                file.write(f"Content:\n{law_data['content']}\n")
                file.write("-" * 80 + "\n")

        # Save each law to a separate file in the directory
        for law_number, law_data in traffic_laws.items():
            filename = f"{folder_name}/{law_number.replace('§', '').replace('.', '_').strip()}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Title: {law_data['title']}\n")
                file.write(f"Content:\n{law_data['content']}\n")

        print(f"Traffic laws successfully scraped and saved. Individual files are in the '{folder_name}' folder.")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

# Run the scraper
scrape_traffic_laws() """

