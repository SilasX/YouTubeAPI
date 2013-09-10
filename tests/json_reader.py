from json import JSONDecoder, dumps

with open("example_pretty.json", "r") as f:
    z = JSONDecoder().decode(f.read())

#for k, v in z.iteritems():
#    print k, "::", v
results = z['feed']['entry']
for result in results:
    print result['title']['$t'].encode('utf8')
