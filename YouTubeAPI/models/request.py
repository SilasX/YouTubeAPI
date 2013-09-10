import urllib3

class Request(object):

    def __init__(self, settings):
        self.settings = settings
        self.result = None
        self.url = "http://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?alt=json"

    def most_viewed_all(self):
        urllib3.urlopen("http://example.com/foo/bar").read()
