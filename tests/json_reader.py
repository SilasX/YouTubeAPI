from json import JSONDecoder, dumps

with open("example_pretty.json", "r") as f:
    z = JSONDecoder().decode(f.read())

#for k, v in z.iteritems():
#    print k, "::", v
output = []
results = z['feed']['entry']
for result in results:
    output.append({})
    z = output[-1]
    z['name'] = result['title']['$t']#.encode('utf8')
    z['URL'] = result['link'][0]['href']#.encode('utf8')
    z['category'] = result['category'][1]['label']#.encode('utf8')
    z['thumbnail'] = result["media$group"]["media$thumbnail"][0]['url']#.encode('utf8')
print dumps(output).encode('utf8')
