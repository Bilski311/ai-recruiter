import logging
import sys
from langchain.chat_models import ChatOpenAI
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, ResponseSynthesizer
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.node_parser import SimpleNodeParser
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.retrievers import VectorIndexRetriever

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


class QueryEngine:

    def __init__(self):
        self.chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

        documents = SimpleDirectoryReader('data', recursive=True).load_data()
        parser = SimpleNodeParser()
        nodes = parser.get_nodes_from_documents(documents)

        llm_predictor = LLMPredictor(self.chat)
        service_context = ServiceContext.from_defaults(
            llm_predictor=llm_predictor)

        index = GPTVectorStoreIndex(nodes, service_context=service_context)
        retriever = VectorIndexRetriever(index=index, similarity_top_k=10)

        response_synthesizer = ResponseSynthesizer.from_args(
            node_postprocessors=[
                SimilarityPostprocessor(similarity_cutoff=0.71)
            ]
        )

        self.query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
        )

        self.llm_predictor = llm_predictor

    def query(self, prompt):
        answer_from_query_engine = str(self.query_engine.query(
            self._get_prompt_as_string(prompt)))
        if answer_from_query_engine != 'None':
            print('Is not none')
            return answer_from_query_engine
        else:
            print('Is none')
            return self.chat(prompt).content

    def get_last_token_usage(self):
        return self.llm_predictor.last_token_usage

    def _get_prompt_as_string(self, prompt):
        return '\n'.join(
            [message.content for message in prompt])
