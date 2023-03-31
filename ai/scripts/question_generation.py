import sys
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def main(subject):
    chat = ChatOpenAI(temperature=0)
    template = 'You are helping to generate dataset of questions for IT recruitement process related to {subject}.'
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = 'Generate a question. Write it out only in JSON format(no other text). The JSON should only have one field: "question"'
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt])

    formatted_prompt = chat_prompt.format_prompt(subject=subject).to_messages()
    print(chat(formatted_prompt).content)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        subject = sys.argv[1]
        main(subject)
    else:
        print("Please provide a subject as a command line argument.")
