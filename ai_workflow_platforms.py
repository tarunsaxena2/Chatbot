!pip install openai langchain pypdf faiss-cpu tiktoken

import os

os.environ["OPENAI_API_KEY"] = ""

from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("/content/sample.pdf")  # upload PDF to Colab first
documents = loader.load()

print(len(documents), "pages loaded")

from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(documents)

print(len(docs), "chunks created")

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(docs, embeddings)

print("Vector DB ready")

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model_name="gpt-4o-mini")

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

query = "Summarize the main idea of the document"
result = qa.run(query)

print(result)

while True:
    q = input("Ask question (or type exit): ")
    if q == "exit":
        break
    print(qa.run(q))
