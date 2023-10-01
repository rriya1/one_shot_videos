from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import chainlit as cl
import openai
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

openai.api_key=api_key

template= """Question: {question}
Answer: think 1"""

@cl.on_chat_start  #whenever an object created, a chainlit UI is initiated
def main():
    #prompttemplate is taking a template which we defined above and its input as the question
    prompt= PromptTemplate(template=template,input_variables=["question"])
    #initializing llmchian, it connects out prompt with the llm
    llm_chain= LLMChain(
        prompt=prompt, #varibale which we defined above
        llm= OpenAI(temprature=1,streaming=True),#defining the model
        verbose=True #thought process, additional text for reasoning
    ) #initializing lllm object
    cl.user_session.set("llm_chain",llm_chain) #taking this llm chian and storing it in a user session called "llm_chain" to access it in the onmessage call

@cl.on_message
async def main(message :str):
    llm_chain=cl.user_session.get("llm_chain") #retreving the user session, the one we defined in template
    #instead of calling modelnow, we will call the llm chain
    res=await llm_chain.arun(message,callbacks=[cl.AsyncLangchianCallbackHandler()]) #this makes a socket connection, could not understand its purpose correctly
    await cl.Message(content=res["text"]).send()