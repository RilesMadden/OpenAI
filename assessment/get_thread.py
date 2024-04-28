import requests
from config_file import api_key

thread_id = 'thread_p2WCEijq1ygbZ9qweLkdVUVZ'

r = requests.get(url=f'https://api.openai.com/v1/threads/{thread_id}',
                 headers={'Authorization': f'Bearer {api_key}', 'OpenAI-Beta': 'assistants=v2'})
r_json = r.json()
print(r_json)


