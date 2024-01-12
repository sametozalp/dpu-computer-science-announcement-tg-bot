class Announcement_Model(object):
    def __init__(self, link, title, date, body=None):
        self.link = "https://bilgisayar.dpu.edu.tr" + link
        self.title = title
        self.date = date
        self.body = body
