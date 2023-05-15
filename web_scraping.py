import requests
from bs4 import BeautifulSoup

# Function to scrape data from a website
def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Add code to extract specific data from the website
        # Example: Extracting the titles of news articles
        article_titles = soup.find_all('h2', class_='article-title')
        for title in article_titles:
            print(title.text)
    else:
        print("Error accessing the website.")

# Example usage
scrape_website("https://www.example.com")
