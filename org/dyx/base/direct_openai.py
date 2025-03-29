import os

import openai
from openai import OpenAI
from org.dyx.env.env import OPENAI_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# 文本text模型
openai.api_key = OPENAI_API_KEY
print(f"api_key:{OPENAI_API_KEY}")

client = OpenAI()
# response_text = client.completions.create(model="gpt-3.5-turbo-instruct", temperature=0.5, max_tokens=100,
#                                    prompt="请给我的咖啡店起个名字")
# print(response_text.choices[0].text.strip())

# chat模型
response_chat = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "system", "content": "你是一个起名大师"},
                                                                 {"role": "user", "content": "请给我的咖啡店起个名字"}],
                                        temperature=0.5, max_tokens=60)
print(response_chat)
