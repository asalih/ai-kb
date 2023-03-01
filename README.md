# AI Knowledge Base
Acquire information with asking questions using gpt, answers will be based on the embedded knowledge base.

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

![alt example](https://github.com/asalih/ai-kb/blob/main/img/example.png?raw=true)
