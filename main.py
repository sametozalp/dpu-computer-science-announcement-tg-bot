import requests
from bs4 import BeautifulSoup
from announcement_scraper import AnnouncementScraper
from model.announcement import Announcement

if __name__ == "__main__":
    url = "https://bilgisayar.dpu.edu.tr/tr/index/duyurular"
    scraper = AnnouncementScraper(url)
    announcement_list = scraper.scrape_announcements()

    for announcement in announcement_list:
        print(f"Title: {announcement.title}")
        print(f"Date: {announcement.date}")
        print(f"Link: {announcement.link}")
        print(f"Body: {announcement.body}")
        print("\n")
