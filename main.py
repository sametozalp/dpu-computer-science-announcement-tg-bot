import requests
from bs4 import BeautifulSoup
from announcement_scraper import AnnouncementScraper
from model.announcement import Announcement
import telebot

if __name__ == "__main__":
    url = "https://bilgisayar.dpu.edu.tr/tr/index/duyurular"
    TOKEN = ""
    chat_id = 0
    
    
    scraper = AnnouncementScraper(url)
    announcement_list = scraper.scrape_announcements()

    bot = telebot.TeleBot(TOKEN)
    message = announcement_list[1].title + "\n\n" + announcement_list[0].body + "\t\n\n" + announcement_list[0].date
    bot.send_message(chat_id, message)

    print("Duyuru gönderildi..")
    #bot.polling(none_stop=True)

    



