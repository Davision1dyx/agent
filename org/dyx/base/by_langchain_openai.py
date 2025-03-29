import os

from langchain_core.messages import SystemMessage, HumanMessage

from org.dyx.env.env import OPENAI_API_KEY
from langchain_openai import OpenAI

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# 文本模型
# text = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.8, max_tokens=60)
# text.invoke("请给我的咖啡店起个名字")

# 聊天模型
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.8, max_tokens=60)

messages = [
    SystemMessage(content="你是一个很棒的起名专家"),
    HumanMessage(content="请给我的咖啡店起个名字")
]

response = chat.invoke(messages)
print(response)