from elasticsearch import Elasticsearch,helpers
from pymongo import MongoClient
import pandas as pd

es = Elasticsearch()

server = MongoClient('') # client details MongoDB

serverdb = server[''] # Collection Name

# data = serverdb.Version9.find()<------20_5
data = serverdb.Loc.find().limit(500)  # Search 


use_these_keys = ['LAT','LNG','ADDRESS','Length']

def filterKeys(document):
    return {key: document[key] for key in use_these_keys }


def doc_generator(data_):
    df = pd.DataFrame(list(data_))    
    df.drop(columns = ['_id'],inplace=True)
    df_iter = df.iterrows()
    for index,doc in df_iter:
        print(filterKeys(doc))
        yield{
            "_index": "master", # Elastic Search Index
            "_type":"_doc",
            "_source": filterKeys(doc)
        }
    # raise StopIteration

helpers.bulk(es,doc_generator(data),chunk_size=100,request_timeout=20000)

# doc_generator(data)
