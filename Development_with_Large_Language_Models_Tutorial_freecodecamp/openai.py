import openai
import json #to get the api key from the json file

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

