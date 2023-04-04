import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = 'here-goes-your-openai-api-token'

documents = SimpleDirectoryReader('data/javascript').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

response = index.query("Prepare 5 questions with answers about Javascript 'static member'. "
                       "Result in json array of questions")
print(response)
