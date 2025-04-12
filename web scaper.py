import requests
from bs4 import BeautifulSoup
import csv
import json
import logging

# Setup logging
logging.basicConfig(filename="scraper_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def scrape_website(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Scrape headlines and links (customize per website)
        data = []
        for headline in soup.find_all(['h1', 'h2', 'h3']):
            text = headline.get_text(strip=True)
            link = headline.find('a')['href'] if headline.find('a') else 'N/A'
            data.append({'headline': text, 'link': link})

        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        print(f"❌ Failed to scrape website: {e}")
        return []

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['headline', 'link'])
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def main():
    print("🕸️  Web Scraper Console")
    url = input("Enter the website URL to scrape: ")

    scraped_data = scrape_website(url)
    if scraped_data:
        print(f"✅ Scraped {len(scraped_data)} items.")

        choice = input("Save as CSV or JSON? [csv/json]: ").strip().lower()
        filename = input("Enter output filename (without extension): ").strip()

        if choice == 'csv':
            save_to_csv(scraped_data, filename + '.csv')
            print(f"📄 Data saved to {filename}.csv")
        elif choice == 'json':
            save_to_json(scraped_data, filename + '.json')
            print(f"📄 Data saved to {filename}.json")
        else:
            print("❌ Invalid format selected.")

        logging.info(f"Scraped {len(scraped_data)} items from {url} and saved as {choice.upper()}.")
    else:
        print("⚠️ No data found or error occurred.")

if __name__ == "__main__":
    main()
