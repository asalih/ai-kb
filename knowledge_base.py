import os
import openai
import csv
import json
from dotenv import load_dotenv
from openai.embeddings_utils import cosine_similarity

load_dotenv()

openai.api_key = os.getenv('API_KEY')

print("Welcome to the Binalyze AI Knowledge Base.")

while True:
    user_input = input("Ask me anything about Binalyze > ")
    if user_input == "exit":
        print("exiting...")
        break

    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=user_input,
    )

    question_embedding = response.data[0].embedding

    similarity_array = []

    with open("embeddings.csv", "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            text_embedding = json.loads(row["embedding"])
            cs = cosine_similarity(question_embedding, text_embedding)
            similarity_array.append(cs)

    index_of_max = similarity_array.index(max(similarity_array))
    original_text = ""

    with open("embeddings.csv", "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for i, row in enumerate(reader):
            if i == index_of_max:
                original_text = row["text"]

    prompt = f'''You are an AI assistant. You work for Binalyze which is a Modern Digital Forensics and Incident Response tool.
    You will be asked questions from a customer and will answer in a helpful and friendly manner.
    You will be provided company information from Binalyze under the [Article] section. The customer question
    will be provided under the [Question] section. You will answer the customers questions based on the article.
    If the user's question is not answered by the article you will respond with "I'm sorry I don't know."
    [Article]
    {original_text}
    [Question]
    {user_input}
    '''

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.2,
        max_tokens=500,
    )

    print(response.choices[0].text.lstrip())
    print("\n")