from bs4 import BeautifulSoup
import requests


class Announcement:
    def __init__(self, url):
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
        
