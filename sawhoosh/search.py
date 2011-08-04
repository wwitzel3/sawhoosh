from whoosh.fields import SchemaClass
from whoosh.fields import TEXT
from whoosh.fields import ID

import os.path

try:
    import cPickle as pickle
except ImportError, e:
    import pickle

from whoosh.index import create_in
from whoosh.index import open_dir

class SawhooshSchema(SchemaClass):
    value = TEXT
    id = ID(stored=True, unique=True)
    cls = ID(stored=True)

INDEX_NAME = 'sawhoosh_index'
if not os.path.exists(INDEX_NAME):
    os.mkdir(INDEX_NAME)
    WIX = create_in(INDEX_NAME, SawhooshSchema)
else:
    WIX = open_dir(INDEX_NAME)
        
def results_to_instances(session, results):
    instances = []
    for r in results:
        cls = pickle.loads('{0}'.format(r.get('cls')))
        id = r.get('id')
        instances.append(session.query(cls).get(id))
    return instances

__all__ = ['SawhooshSchema', 'WIX', 'INDEX_NAME', 'results_to_instances']