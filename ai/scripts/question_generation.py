import openai
from langchain.llms import OpenAIChat

llm = OpenAIChat()
text = "Write a question for javascript interview?"
print(llm(text))