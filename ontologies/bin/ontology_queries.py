from doctest import DocFileSuite
import urllib.parse
import urllib.request
from icecream import ic
import json

#prepare html out to
#cat out.html  | grep "b'" | sed 's/^ic| data: (//' | sed "s/b'//;s/'$//;s/^[ \t]*//;s/\n//" | tr --delete '\n'
#curl -L 'http://www.ebi.ac.uk/ols/api/search?q={liver}&queryFields={label}&ontology={uberon}&exact=true' -i -H 'Accept: application/json' 

def get_url_data(url):
    ic("url=",url)
    with urllib.request.urlopen(url) as response:
       data = response.read()
    return(data)

#clean spurious chars from jq
def clean_jq(line):
    line = re.sub("^b",'',line)
    return(line)

#parse out the ols target line
def ols_parse_target(line):
    parsed = json.loads(line)
    response = parsed['response']
    hits = response['docs']
    #ic(json.dumps(hits, indent=4, sort_keys=True))
    target_line = hits
    return(target_line)

def jq_wrap_cbracket(term):
    term_coded = '{' + term + '}'
    return(term_coded)

"""     "response": {
        "docs": [
            {
                "id": "uberon:class:http://purl.obolibrary.org/obo/UBERON_0002107",
                "iri": "http://purl.obolibrary.org/obo/UBERON_0002107",
                "is_defining_ontology": true,
                "label": "liver",
                "obo_id": "UBERON:0002107",
                "ontology_name": "uberon",
                "ontology_prefix": "UBERON",
                "short_form": "UBERON_0002107",
                "type": "class"
            }
        ],
        "numFound": 1,
        "start": 0
    }, """
#curl -L 'http://www.ebi.ac.uk/ols/api/search?q={liver}&queryFields={label}&ontology={uberon}&exact=true' -i -H 'Accept: application/json' 

def exactMatch(ontology,term):
    matchType = 'exact'
    jq_target = findOLSMatch(ontology,term,matchType)
    return(jq_target)

def anyMatch(ontology,term):
    matchType = 'any'
    jq_target = findOLSMatch(ontology,term,matchType)
    return(jq_target)

def findOLSMatch(ontology,term,matchType):
    ic(ontology)
    ic(term)
    url = 'http://www.ebi.ac.uk/ols/api/search?q={liver}&ontology={uberon}&queryFields={label}&exact=true'
    query_term_coded = term
    ont_coded = ontology
    #q={liver}&queryFields={label}&ontology={uberon}&exact=true'
    if (matchType == 'exact'):
        params = {'q' : query_term_coded, 'ontology' :  ont_coded,  'exact' : 'on'}
    elif (matchType == 'any'):
        params = {'q' : query_term_coded, 'ontology' :  ont_coded,  'exact' : 'off'}
    else:
        print("ERROR: matchType is not found")
    ic(params)
    url_parsed = urllib.parse.urlencode(params)
    ic(url_parsed)
    #quit()
    data = get_url_data('http://www.ebi.ac.uk/ols/api/search?' + url_parsed)
    small_data = data.decode('ascii')
    jq_target = ols_parse_target(small_data)
    return(jq_target)

""" usage:
ontology='uberon'
term='liver'
matches = exactMatch(ontology,term)
ic(len(matches))
ic(json.dumps(matches, indent=4, sort_keys=True))
#ic(data)
#print(data)

matches = anyMatch(ontology,term)
ic(len(matches))
ic(json.dumps(matches, indent=4, sort_keys=True)) """