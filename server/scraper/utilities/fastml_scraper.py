from scraper.utilities.base_scraper import BaseScraper
from bs4 import NavigableString, Tag

class FastMLScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(url)
    
    def get_latest_blogs(self, count=5):
        blogs_list = []
        blogs_div = self.bs_obj.find(id="content")
        blog_div = blogs_div.find("div", class_="blog-index")
        article_div = blog_div.find_all("article")
        for ac in article_div[0:count]:
            if ac.header is not None:
                blog_obj = ac.header.h1
                title = blog_obj.find("a").text
                link = blog_obj.find("a").get("href")
                blogs_list.append({
                    "title": title.title(),
                    "link": "https://fastml.com/"+link[1:]
                })
        return blogs_list

if __name__ == "__main__":
    m_s = FastMLScraper("http://fastml.com/")
    print(m_s.get_latest_blogs())