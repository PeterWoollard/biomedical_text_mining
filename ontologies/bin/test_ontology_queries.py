from doctest import DocFileSuite
import urllib.parse
import urllib.request
from icecream import ic
import json
import ontology_queries

#prepare html out to
#cat out.html  | grep "b'" | sed 's/^ic| data: (//' | sed "s/b'//;s/'$//;s/^[ \t]*//;s/\n//" | tr --delete '\n'
#curl -L 'http://www.ebi.ac.uk/ols/api/search?q={liver}&queryFields={label}&ontology={uberon}&exact=true' -i -H 'Accept: application/json' 




def test_exactMatch():
    ontology='uberon'
    term='liver'
    hits = ontology_queries.exactMatch(ontology,term)
    assert len(hits) == 1


def test_anyMatch():
    ontology='uberon'
    term='liver'
    hits = ontology_queries.anyMatch(ontology,term)
    assert len(hits) >= 1

