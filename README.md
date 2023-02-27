# AI Knowledge Base
Acquire acknowledgment with asking questions based on knowledge base.

## Install
```
pip install -r requirements.txt
```

## Run
First embeddings must be prepared using embeddings.py. This will create necessary vectors.
```
API_KEY=<api key> python embeddings.py
``` 

To run knowledge_base.py you need to provide an API Key from openapi.
```
API_KEY=<api key> python knowledge_base.py
``` 