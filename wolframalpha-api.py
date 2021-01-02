# implementing wolframalpha API:

import wolframalpha

question = input('Q:')
app_id = 'Your App ID'
client = wolframalpha.Client(app_id)
result = client.query(question)
answer = next(result.results).text
print(answer)