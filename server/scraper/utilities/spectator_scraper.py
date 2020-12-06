from scraper.utilities.base_scraper import BaseScraper

class SpectatorScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(url)
    
    def get_latest_blogs(self, count=5):
        blogs_list = []
        blogs_div = self.bs_obj.find(id="content")
        post_div = blogs_div.find("div", class_="post-list")
        h2_div = post_div.find_all("h2")
        for h in h2_div[0:count]:
            if h.a is not None:
                title = h.a.get("title")
                link = h.a.get("href")
                blogs_list.append({
                    "title": title,
                    "link": link
                })
        return blogs_list

if __name__ == "__main__":
    m_s = SpectatorScraper("http://blog.shakirm.com/")
    res = m_s.get_latest_blogs()
    print(res)