import requests
from bs4 import BeautifulSoup
import csv
import json

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

def scrape_elements(html, tag, class_name=None):
    soup = BeautifulSoup(html, 'html.parser')
    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)
    return elements

def save_to_csv(data, filename='scraped_data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Text', 'Link'])
        for item in data:
            writer.writerow([item.get('text', ''), item.get('link', '')])
    print(f"Data saved to {filename}")

def save_to_json(data, filename='scraped_data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def main():
    print("📄 Web Scraper")
    url = input("Enter the URL to scrape: ")
    tag = input("Enter the HTML tag to extract (e.g., h1, a, div): ")
    class_name = input("Enter the class name (optional): ").strip() or None
    output_format = input("Save as CSV or JSON? (csv/json): ").strip().lower()

    html = fetch_html(url)
    if not html:
        return

    elements = scrape_elements(html, tag, class_name)

    scraped_data = []
    for el in elements:
        text = el.get_text(strip=True)
        link = el.get('href', '') if el.name == 'a' else ''
        scraped_data.append({'text': text, 'link': link})

    if output_format == 'csv':
        save_to_csv(scraped_data)
    elif output_format == 'json':
        save_to_json(scraped_data)
    else:
        print("Invalid format. Choose csv or json.")

if __name__ == "__main__":
    main()
