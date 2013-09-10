from json import JSONDecoder

class Result(object):

    def __init__(self, json_string):
        self.dict_obj = JSONDecoder().decode(json_string)
        self.rendered = None

    def render(self):
        if self.rendered is None:
            results = self.dict_obj['feed']['entry']
            self.rendered = "\n".join([x['title']['$t'] for x in results]).encode('utf8')
        return self.rendered
