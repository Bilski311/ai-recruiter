from langchain.chat_models import ChatOpenAI
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, ResponseSynthesizer
from llama_index.node_parser import SimpleNodeParser
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from dotenv import load_dotenv
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

load_dotenv()
chat = ChatOpenAI(temperature=0, model_name="gpt-4")

documents = SimpleDirectoryReader('data', recursive=True).load_data()
print(documents)
parser = SimpleNodeParser()
nodes = parser.get_nodes_from_documents(documents)
print(len(nodes))

# llm_predictor = LLMPredictor(chat)
# service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# index = GPTVectorStoreIndex(
#     nodes, service_context=service_context)
# retriever = VectorIndexRetriever(
#     index=index,
#     similarity_top_k=2,
# )

# response_synthesizer = ResponseSynthesizer.from_args(
#     node_postprocessors=[
#         SimilarityPostprocessor(similarity_cutoff=0.75)
#     ]
# )

# query_engine = RetrieverQueryEngine(
#     retriever=retriever,
#     response_synthesizer=response_synthesizer,
# )

# print(
#     f'Query engine output: {query_engine.query("Do you know what static initialization blocks are in javascript? Give a brief answer.")}')
# print(f'Token usage: {llm_predictor.last_token_usage}')
