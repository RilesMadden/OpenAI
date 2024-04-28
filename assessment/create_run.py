from config_file import api_key
from openai import OpenAI

client = OpenAI(api_key=api_key)

# run = client.beta.threads.runs.create(
#   thread_id='thread_p2WCEijq1ygbZ9qweLkdVUVZ',
#   assistant_id='asst_oMgmQXkJf2ZJzTykGd5I1nLP'
# )
# run_2GLcVoHbck09J87EW9cpuuN7

run = client.beta.threads.runs.create(
  thread_id='thread_p2WCEijq1ygbZ9qweLkdVUVZ',
  assistant_id='asst_oMgmQXkJf2ZJzTykGd5I1nLP',
  model="gpt-4-turbo",
  # new instructions to override create instructions
  instructions="Given the following dataset of individuals and their favorite cities along with reasons. Explain why each person favors their respective city. Take into account other columns in the dataset that may influence why it's their favorite.",
  tools=[{"type": "code_interpreter"}, {"type": "file_search"}]
)
# run_82mt46MeoEqpUObLac60lrDb

print(run)


