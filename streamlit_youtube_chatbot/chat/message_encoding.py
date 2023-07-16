import qdrant_client
import streamlit as st
import tiktoken
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant


def embedding_search(query, k, api_token):
    embeddings = OpenAIEmbeddings(
        openai_api_key=api_token,
    )
    client = qdrant_client.QdrantClient(
        url=st.secrets["qdrant_url"], api_key=st.secrets["qdrant_api_key"]
    )
    db = Qdrant(client=client, embeddings=embeddings, collection_name="documents")
    return db.similarity_search(query, k=k)


def query_message_prompt(query: str, api_token: str):
    docs = embedding_search(query, k=2, api_token=api_token)
    docs = [doc.page_content for doc in docs]
    context_1 = docs[0]
    context_2 = docs[1]
    query_message = f"""Die Frage, die du beantworten sollst, lautet: "{query}"
Verwende für die Beantwortung dieser Frage ausschließlich den folgenden Kontext:
Kontext 1:
---
{context_1}
---
Kontext 2:
---
{context_2}
---"""
    return query_message


def get_encoding_length(text: str) -> int:
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
    encoding_length = len(encoding.encode(text))
    return encoding_length
