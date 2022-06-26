
"""
title: ontology_queries.py tests
description: test of the modules for querying ontologies. 
author: Peter Woollard 
creation_date: 26-Jun-2022
comment:
"""
from doctest import DocFileSuite
import urllib.parse
import urllib.request
from icecream import ic

import sys
sys.path.append('../')
import ontology_queries

def test_exactMatch():
    ontology='uberon'
    term='liver'
    hits = ontology_queries.exactMatch(ontology,term)
    assert len(hits) == 1


def test_exactMatches():
    ontology='uberon'
    terms= ['liver','heart']
    hits = ontology_queries.exactMatches(ontology,terms)
    total_hit_count=0
    for term in hits:
        ic(term)
        hit = hits[term]
        total_hit_count += len(hit)
    assert(total_hit_count) == 2


def test_terms_that_match_or_not():
    hits = ({'heart': [{'id': 'uberon:class:http://purl.obolibrary.org/obo/UBERON_0000948',
                         'iri': 'http://purl.obolibrary.org/obo/UBERON_0000948',
                         'is_defining_ontology': True,
                         'label': 'heart',
                         'obo_id': 'UBERON:0000948',
                         'ontology_name': 'uberon',
                         'ontology_prefix': 'UBERON',
                         'short_form': 'UBERON_0000948',
                         'type': 'class'}],
              'liver': [{'id': 'uberon:class:http://purl.obolibrary.org/obo/UBERON_0002107',
                         'iri': 'http://purl.obolibrary.org/obo/UBERON_0002107',
                         'is_defining_ontology': True,
                         'label': 'liver',
                         'obo_id': 'UBERON:0002107',
                         'ontology_name': 'uberon',
                         'ontology_prefix': 'UBERON',
                         'short_form': 'UBERON_0002107',
                         'type': 'class'}],
              'madeup': []})
    (found,missing) = ontology_queries.terms_that_match_or_not(hits)
    assert(len(missing)) == 1

