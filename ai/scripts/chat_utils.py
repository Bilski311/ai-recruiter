from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from config import CHAT_TEMPERATURE


chat = ChatOpenAI(temperature=CHAT_TEMPERATURE)


def generate_chat_output(system_template, human_template, **kwargs):
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt])
    formatted_prompt = chat_prompt.format_prompt(**kwargs).to_messages()

    return chat(formatted_prompt).content
