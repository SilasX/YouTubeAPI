import urllib2
from result import Result

class Request(object):

    def __init__(self, settings=None):
        self.settings = settings
        self.result = None
        self.url = "http://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?alt=json"

    def get_most_viewed_all(self):
        self.result = Result(urllib2.urlopen(self.url).read())
