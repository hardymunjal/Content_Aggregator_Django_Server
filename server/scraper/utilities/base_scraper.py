import requests
from bs4 import BeautifulSoup

class BaseScraper:
    def __init__(self, url):
        self.url = url
        res = requests.get(self.url)
        self.html = res.text
        self.bs_obj = BeautifulSoup(self.html, 'html.parser')
        print("********************************************************")
        print(f"Scraping website - '{self.bs_obj.title.text}' at {url}")
        print("********************************************************")
        print("\n")


if __name__ == "__main__":
    b_s = BaseScraper("https://webscraper.io/test-sites/tables")

