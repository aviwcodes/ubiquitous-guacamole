import requests
import pandas as pd

access_token = "<YOUR_ACCESS_TOKEN>"
headers = {'Authorization':"Token "+access_token}
#private to get private repo, public to get public repositories
payload={"visibility":"private"}
url = "https://api.github.com/user/repos"
res= requests.get(url,headers=headers,params=payload)
#print("res.status_code: {}".format(res.status_code))
if res.status_code == 200:
  data=res.json()
  df = pd.json_normalize(data)
  print(df[['name','url','private']])
