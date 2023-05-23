import requests
import pandas as pd
import numpy as np
# Load Data
df = pd.read_csv('asos.csv')

num = np.random.randint(len(df))
choice_text = np.random.choice(list(df['lemmatize_text']))
choice_url = np.random.choice(list(df['url']))
choice_url = "http://"+choice_url
text_data = {'text': choice_text,'url': choice_url}

resp = requests.post('http://127.0.0.1:5000/',data=text_data)
print('Input Product: ')
print()
print(text_data)
print()
print()
print('Similar Products: ')
print()
print(resp.json())

