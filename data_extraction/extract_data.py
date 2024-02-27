# data_extraction/extract_data.py
import sys
import os


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)



import requests
from bs4 import BeautifulSoup
from data_processing.process_data import process_information
def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website content: {e}")
        return None

def extract_information(html_content):
    # Example Web Scraping Logic: Extract text content of all <p> elements
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    extracted_info = ' '.join([paragraph.get_text() for paragraph in paragraphs])

    # Additional Web Scraping Logic:
    # You can add more logic here to extract specific information based on the HTML structure

    return extracted_info

if __name__ == "__main__":
    website_url = "https://desktop.telegram.org/?setln=en"  # Replace with the actual website URL
    content = fetch_website_content(website_url)

    if content:
        information = extract_information(content)
        processed_info = process_information(information)
        print(f"Processed Information: {processed_info}")
