import json
import os
from elasticsearch import Elasticsearch, helpers

# Define constants
DATA_FOLDER = "Data_Sets"
ES_HOST = "https://localhost:9200"
INDEX_NAME = "tweets_index"
ES_USER = "elastic"
ES_PASSWORD = "JiLYT-lqyqLW+V7lfuAQ"

# Connect to Elasticsearch
es = Elasticsearch(
    ES_HOST,
    basic_auth=(ES_USER, ES_PASSWORD),
    verify_certs=False  # Ignore SSL verification warnings
)

# Load preprocessed data
#with open(os.path.join(DATA_FOLDER, "twcs.json"), "r", encoding="utf-8") as file:
with open(os.path.join(DATA_FOLDER, "twcs_cleaned.json"), "r", encoding="utf-8") as file:
    data = [json.loads(line) for line in file]

# Bulk indexing function
def bulk_index_data(es, index_name, data):
    actions = [
        {
            "_index": index_name,
            "_id": doc["tweet_id"],
            "_source": doc
        }
        for doc in data
    ]
    helpers.bulk(es, actions)

# Check if index exists, else create
if not es.indices.exists(index=INDEX_NAME):
    es.indices.create(index=INDEX_NAME)

# Index data
bulk_index_data(es, INDEX_NAME, data)
print(f"✅ Data indexed successfully into `{INDEX_NAME}`!")
