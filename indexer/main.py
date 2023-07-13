import getpass
import os

from langchain.document_loaders import YoutubeLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from tqdm import tqdm

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")
qdrant_api_key = getpass.getpass("Qdrant API Key:")
qdrant_url = getpass.getpass("Qdrant url:")

embeddings = OpenAIEmbeddings()

urls = [
    "https://www.youtube.com/watch?v=gSPVXhL_mhM",
    "https://www.youtube.com/watch?v=DZwfmbhpIEw",
    "https://www.youtube.com/watch?v=nYhOVBeRugE",
    "https://www.youtube.com/watch?v=kpfm4WXo2aU",
    "https://www.youtube.com/watch?v=b3JsYPoTa8s",
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

documents = []
for url in tqdm(urls):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True, language=["de"])
    documents.extend(loader.load_and_split(text_splitter))

# code for loading the data the first time into the qdrant database
qdrant = Qdrant.from_documents(
    documents,
    embeddings,
    url=qdrant_url,
    api_key=qdrant_api_key,
    collection_name="documents",
)
print("upload done")
