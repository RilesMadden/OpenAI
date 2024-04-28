from config_file import api_key
from openai import OpenAI

client = OpenAI(api_key=api_key)

file = client.files.create(
  file=open("tse_takehome_dataset.csv", "rb"),
  purpose='assistants'
)
  
assistant = client.beta.assistants.create(
  name="Favorite City Explainer",
  instructions="Given the following dataset of individuals and their favorite cities along with reasons, please explain why each person favors their respective city.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4-turbo",
  tool_resources= {
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)

print(assistant)

# asst_oMgmQXkJf2ZJzTykGd5I1nLP