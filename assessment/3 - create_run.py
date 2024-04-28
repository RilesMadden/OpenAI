from config_file import api_key
from openai import OpenAI

client = OpenAI(api_key=api_key)

run = client.beta.threads.runs.create(
  # run 1
  assistant_id='asst_vcHBcrAKptN9w3KZDECJZ0Tr', # taken from output of '1 - create_assistant.py'
  thread_id='thread_aH2MuYpVDP3UCMjysowJEYYz', # taken from output of '2 - create_thread.py'

  # run 2 - add instructions
  instructions="Given the following dataset of individuals and their favorite cities along with reasons. Explain why each person favors their respective city. Take into account other columns in the dataset that may influence why it's their favorite, including their profession and what opportunities they might have.",
  
  model="gpt-4-turbo",
  tools=[{"type": "code_interpreter"}, {"type": "file_search"}]
)


print(run)

# run 1 - run_O3gtETnOXah8f9bdegmaeOPr
# run 2 - run_afBUmC6t7qkuYgoR1ZEkD84z


