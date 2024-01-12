import requests
import urllib.request
from bs4 import BeautifulSoup
from model.announcement import Announcement_Model

url = "https://bilgisayar.dpu.edu.tr/tr/index/duyurular"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, "html.parser")
elements = soup.find_all(class_="media")

announcement_list = []

for element in elements:
    element_a = element.find("a")["href"]
    element_h4 = element.find("div", class_="media-body").find("h4").text
    element_date = element.find("div", class_="media-body").find("p").text
    model = Announcement_Model(element_a, element_h4, element_date)

    response2 = requests.get(model.link, verify=False)
    soup2 = BeautifulSoup(response2.content, "html.parser")
    element_body = soup2.find(class_="sayfa-icerik").text
    model.body = element_body
    
    announcement_list.append(model)

for announcement in announcement_list:
    print("***************************************************************************************************")
    print(announcement.title)
    print(announcement.link)
    print(announcement.date)
    print(announcement.body)

