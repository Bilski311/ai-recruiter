import sys
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


def main(subject):
    chat = ChatOpenAI(temperature=0)
    template = f'You are helping to generate dataset of questions and answers for IT recruitement process related to {subject}.'
    system_prompt_message = SystemMessagePromptTemplate.from_template(template)

    human_template = "Generate a question in a JSON format."
    human_prompt_message = HumanMessagePromptTemplate.from_template(
        human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_prompt_message, human_prompt_message])
    print(chat(chat_prompt.format_prompt().to_messages()))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        subject = sys.argv[1]
        main(subject)
    else:
        print("Please provide a subject as a command line argument.")
