from bs4 import BeautifulSoup
import requests

from model.announcement import Announcement

class AnnouncementScraper:
    def __init__(self, url):
        self.url = url
        self.announcement_list = []

    def scrape_announcements(self):
        response = requests.get(self.url, verify=False)
        soup = BeautifulSoup(response.content, "html.parser")
        elements = soup.find_all(class_="media")

        for element in elements:
            link = "https://bilgisayar.dpu.edu.tr/" + element.find("a")["href"]
            title = element.find("div", class_="media-body").find("h4").text
            date = element.find("div", class_="media-body").find("p").text

            announcement = Announcement(link, title, date)
            announcement.fetch_body()  # Fetch the body content

            self.announcement_list.append(announcement)
        
        return self.announcement_list
