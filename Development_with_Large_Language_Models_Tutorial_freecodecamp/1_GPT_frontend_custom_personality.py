import chainlit as cl
import openai
import os
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

openai.api_key=api_key

#the decorator will keep on checking for messages from the user. 
@cl.on_message
async def main(message: str):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[ #can be an array of dictionaries
        {"role": "assistant", "content":"respond to messages like a comedian"}, #can define the personality or command on how chatgpt needs to respond to user messages. 
        { "role": "user","content": message }
    ],
    temperature=1.3,
    max_tokens=50,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    await cl.Message(content=str(response['choices'][0]['message']['content'])).send()