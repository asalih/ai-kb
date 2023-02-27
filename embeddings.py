import os
import openai
import csv

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('API_KEY')

text_array = []
embedding_array = []

for file in os.listdir("training-data"):
    if file.endswith(".txt"):
        with open(os.path.join("training-data", file), "r", encoding="utf8") as f:
            text = f.read()
            text_array.append(text)

for text in text_array:
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text,
    )
    embedding = response.data[0].embedding

    embedding_hash = {"embedding": embedding, "text": text}
    embedding_array.append(embedding_hash)

with open("embeddings.csv", "w", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["embedding", "text"])
    for obj in embedding_array:
        writer.writerow([obj["embedding"], obj["text"]])
