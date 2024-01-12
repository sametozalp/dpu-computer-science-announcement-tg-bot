from bs4 import BeautifulSoup
import requests


class Announcement:
    def __init__(self, link, title, date, body=None):
        self.link = link
        self.title = title
        self.date = date
        self.body = body

    def fetch_body(self):
        response = requests.get(self.link, verify=False)
        soup = BeautifulSoup(response.content, "html.parser")
        element_body = soup.find(class_="sayfa-icerik").text
        self.body = element_body
