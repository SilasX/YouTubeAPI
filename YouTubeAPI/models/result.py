from json import JSONDecoder

class Result(object):

    def __init__(self, json_string):
        self.dict_obj = JSONDecoder().decode(json_string)
        self.rendered = None
        self.result_dict = None
        self.KEY_ORDER = [
            u'vidname',
            u'vidURL',
            u'category',
            u'thumbnail'
        ]

    def key_elements(self):
        if self.result_dict is not None:
            return self.result_dict
        results = self.dict_obj['feed']['entry']
        self.result_dict = []
        for result in results:
            self.result_dict.append({})
            z = self.result_dict[-1]
            z[u'vidname'] = result['title']['$t']
            z[u'vidURL'] = result['link'][0]['href']
            z[u'category'] = result['category'][1]['label']
            z[u'thumbnail'] = result["media$group"]["media$thumbnail"][0]['url']
        return self.result_dict

    def render(self):
        if self.rendered is None:
            results = self.dict_obj['feed']['entry']
            self.rendered = "\n".join([x['title']['$t'] for x in results]).encode('utf8')
        return self.rendered

    def render_html(self):
        output = "<html><body><table>"
        self.key_elements()  # set up result dict
        for result in self.result_dict:
            output += "<tr>"
            for k in self.KEY_ORDER:
                output += "<td class='%s'>" % k
                if k == u'thumbnail':
                    output += "<img src='%s'/>" % result[k]
                else:
                    output += result[k]
                output += "</td>"
            output += "</tr>"
        output += "</table></body></html>"
        return output
