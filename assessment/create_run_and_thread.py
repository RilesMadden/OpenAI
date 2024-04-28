from config_file import api_key
import requests

HEADERS = {'Authorization': f'Bearer {api_key}', 'OpenAI-Beta': 'assistants=v2'}
assistant_id = 'asst_oMgmQXkJf2ZJzTykGd5I1nLP' # obtained from create_assistant.py
thread_id = 'thread_uy5N31mzdQMxCoVrEQPjiZcA'
run_id = 'run_zo6kGFmxZFubazhH23kgalU5'

endpoint = f'https://api.openai.com/v1/threads/runs'

response = requests.post(
    url=endpoint,
    headers=HEADERS,
    json={
        'assistant_id': f'{assistant_id}',
        'thread': {
            'messages': [
                {'role': 'user',
                 'content': 'Explain why New York is Nicole Escobars favorite city'}
            ]
        }
    }
)

endpoint = f'https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}'

response = requests.get(
    url=endpoint,
    headers=HEADERS
)

print(response.json())
