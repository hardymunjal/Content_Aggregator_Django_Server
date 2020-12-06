from scraper.utilities.base_scraper import BaseScraper
from bs4 import NavigableString, Tag

class MicrosoftScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(url)
    
    def get_latest_blogs(self, count=5):
        blogs_list = []
        blogs_div = self.bs_obj.find(id="main")
        h3_div = blogs_div.find_all("h3")
        for h in h3_div[0:count]:
            if h.get("id") is not None:
                title_raw = h.get("id")
                title = " ".join(title_raw.split("-")).title()
                link = h.find("a").get("href")
                blogs_list.append({
                    "title": title,
                    "link": "https://docs.microsoft.com/en-us/archive/blogs/"+link[3:]
                })
        return blogs_list

if __name__ == "__main__":
    m_s = MicrosoftScraper("https://docs.microsoft.com/en-us/archive/blogs/machinelearning/")
    m_s.get_latest_blogs()