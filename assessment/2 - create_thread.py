from config_file import api_key
from openai import OpenAI

client = OpenAI(api_key=api_key)

file = client.files.create(
  file=open("tse_takehome_dataset.csv", "rb"),
  purpose='assistants'
)

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Explain why New York is Tina Escobar's favorite city.",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
)

print(thread)

# thread_aH2MuYpVDP3UCMjysowJEYYz