import requests
from config_file import api_key

thread_id = 'thread_aH2MuYpVDP3UCMjysowJEYYz' # taken from output of '2 - create_thread.py'

r = requests.get(url=f'https://api.openai.com/v1/threads/{thread_id}/messages',
                 headers={'Authorization': f'Bearer {api_key}', 'OpenAI-Beta': 'assistants=v2'})
r_json = r.json()
print(r_json)

# Prompt - Explain why New York is Tina Escobar's favorite city.

# response from run 1 - New York is Tina Escobar's favorite city because it offers a vibrant arts scene, a diverse culture, and bustling city life.
# run_id = 'run_O3gtETnOXah8f9bdegmaeOPr'

# response from run 2 - Tina Escobar favors New York as her favorite city due to its vibrant arts scene, diverse culture, and the excitement of bustling city life, which she finds exhilarating and inspiring.
# run_id = 'run_afBUmC6t7qkuYgoR1ZEkD84z'