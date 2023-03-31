import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = 'here-goes-your-openai-api-token'

documents = SimpleDirectoryReader('data/javascript/closures').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

response = index.query("What are javascript closures?")
print(response)
