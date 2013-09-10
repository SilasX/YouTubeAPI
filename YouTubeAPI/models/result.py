from json import JSONDecoder

class Result(object):

    def __init__(self, json_string):
        self.dict_obj = JSONDecoder().decode(json_string)
        self.rendered = None
        self.result_dict = None

    def key_elements(self):
        if self.result_dict is not None:
            return self.result_dict
        results = self.dict_obj['feed']['entry']
        self.result_dict = []
        for result in results:
            self.result_dict.append({})
            z = self.result_dict[-1]
            z[u'name'] = result['title']['$t']
            z[u'URL'] = result['link'][0]['href']
        return self.result_dict

    def render(self):
        if self.rendered is None:
            results = self.dict_obj['feed']['entry']
            self.rendered = "\n".join([x['title']['$t'] for x in results]).encode('utf8')
        return self.rendered
