import json
from config import output_types
from chat_utils import generate_chat_output
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from config import CHAT_TEMPERATURE

class ContentGenerator:
    def __init__(self):    
        self.chat = ChatOpenAI(temperature=CHAT_TEMPERATURE)
    def generate(self, output_type, **kwargs):
        output_type_config = output_types[output_type]
        system_template = output_type_config['system_template']
        human_template = output_type_config['human_template']
        
        output = self._generate_chat_output(system_template, human_template, **kwargs)
        return json.loads(output)

    def _generate_chat_output(self, system_template, human_template, **kwargs):
        system_message_prompt = SystemMessagePromptTemplate.from_template(
            system_template)
        human_message_prompt = HumanMessagePromptTemplate.from_template(
            human_template)
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt])
        formatted_prompt = chat_prompt.format_prompt(**kwargs).to_messages()

        return self.chat(formatted_prompt).content