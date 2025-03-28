import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Disable SSL warnings (safe for localhost testing)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Elasticsearch credentials
ELASTIC_USER = "elastic"
ELASTIC_PASS = "JiLYT-lqyqLW+V7lfuAQ"
ELASTIC_URL = "https://localhost:9200"

# Document update URL
doc_id = "2"
index_name = "test_index"
update_url = f"{ELASTIC_URL}/{index_name}/_update/{doc_id}"

# JSON data to update the document
update_data = {
    "doc": {
        "ccity": None,  # This removes "ccity" field
        "city": "Los Angeles"
    }
}

# Send request to Elasticsearch
response = requests.post(
    update_url,
    json=update_data,
    auth=HTTPBasicAuth(ELASTIC_USER, ELASTIC_PASS),
    headers={"Content-Type": "application/json"},
    verify=False  # Ignore SSL verification
)

# Print response
print(response.json())
