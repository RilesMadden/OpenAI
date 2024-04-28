import requests
from config_file import api_key

thread_id = 'thread_p2WCEijq1ygbZ9qweLkdVUVZ'
run_id = 'run_82mt46MeoEqpUObLac60lrDb'

r = requests.get(url=f'https://api.openai.com/v1/threads/{thread_id}/messages',
                 headers={'Authorization': f'Bearer {api_key}', 'OpenAI-Beta': 'assistants=v2'})
r_json = r.json()
print(r_json['data'][0]['content'][0]['text']['value'])

