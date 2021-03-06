from doctest import DocFileSuite
import urllib.parse
import urllib.request
from icecream import ic
import json
import ontology_queries

#prepare html out to
#cat out.html  | grep "b'" | sed 's/^ic| data: (//' | sed "s/b'//;s/'$//;s/^[ \t]*//;s/\n//" | tr --delete '\n'
#curl -L 'http://www.ebi.ac.uk/ols/api/search?q={liver}&queryFields={label}&ontology={uberon}&exact=true' -i -H 'Accept: application/json' 


ontology='uberon'
term='liver'
matches = ontology_queries.exactMatch(ontology,term)
ic(len(matches))
ic(json.dumps(matches, indent=4, sort_keys=True))
#ic(data)
#print(data)

matches = ontology_queries.anyMatch(ontology,term)
ic(len(matches))
ic(json.dumps(matches, indent=4, sort_keys=True))