import openai
import json #to get the api key from the json file

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

openai.api_key=api_key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "what are you?"
    }
  ],
  temperature=1.3,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'][0]['message']['content'])
