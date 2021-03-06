from scraper.utilities.base_scraper import BaseScraper

class MLMasteryScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(url)
    
    def get_latest_blogs(self, count=5):
        blogs_list = []
        blogs_div = self.bs_obj.find(id="main")
        article_div = blogs_div.find_all("article")
        for ar in article_div[0:count]:
            if ar.a is not None:
                blogs_list.append({
                    "title": ar.a.get("title"),
                    "link": ar.a.get("href")
                })
        return blogs_list

if __name__ == "__main__":
    m_s = MLMasteryScraper("https://machinelearningmastery.com/blog/")
    m_s.get_latest_blogs()