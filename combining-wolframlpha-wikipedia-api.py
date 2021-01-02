# Combining both wolframalpha and wikipedia api into one:

import wolframalpha
import wikipedia

while True:
    question = input('Q:')
    try:
        #wolframalpha code:
        app_id = 'Your App ID'
        client = wolframalpha.Client(app_id)
        result = client.query(question)
        answer = next(result.results).text
        print(answer)
    
    except:
        #wikipedia code:
        print(wikipedia.summary(question))

