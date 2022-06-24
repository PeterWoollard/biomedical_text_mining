import urllib.parse
import urllib.request
from icecream import ic


def get_url_data(url):
    print("url=",url)
    with urllib.request.urlopen(url) as response:
       data = response.read()
    return(data)

url = 'http://python.org/'  
data = get_url_data(url)
#print(data)

#https://www.ebi.ac.uk/ols/docs/api

#url = 'http://www.ebi.ac.uk/ols/api/ontologies/go/parents?id=GO:0043226'
#data = get_url_data(url)
#ic(data)

def exactMatch(ontology,term):
    ic(ontology)
    ic(term)
    url = 'http://www.ebi.ac.uk/ols/api/search?q={liver}&ontology={uberon}&queryFields={label}&exact=true'
    term_coded = '{' + term + '}'
    ont_coded = '{' + ontology + '}'
    params = {'q' : term_coded, 'ontology' :  ont_coded, 'exact' : 'true'}
    params = {'q' : term_coded}
    ic(params)
    url_parsed = urllib.parse.urlencode(params)
    ic(url_parsed)
    #quit()
    data = get_url_data('http://www.ebi.ac.uk/ols/api/search?' + url_parsed)
    return(data)

ontology='uberon'
term='liver'
data = exactMatch(ontology,term)
ic(data)