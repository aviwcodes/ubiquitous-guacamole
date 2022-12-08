import requests
import pandas as pd

username = "aviwcodes"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
#print(user_data)
df = pd.json_normalize(user_data)
df[['login','url','public_repos']].head()
