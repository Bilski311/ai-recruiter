import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = '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'


def load_data(folder):
    documents = SimpleDirectoryReader('data/' + folder).load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    return index


def generate_question(folder, topic):
    index = load_data(folder)
    response = index.query('Generate random question with answer about ' + folder + ' ' + topic + '. Result in '
                                                                                                  'json as array '
                                                                                                  'of questions')
    print(response)


# Usage
generate_question('javascript', 'typed arrays')
generate_question('http', 'cookies')
generate_question('html', 'cors')
