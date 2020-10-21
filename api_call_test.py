import requests
import pandas as pd
import json


url = "http://localhost:5000/personal-app/personal-balance/balance"
_json = {"date": "2020-10-20"}

resp = requests.post(url, json=_json)

resp_json_str = resp.json()

resp_json = json.loads(resp_json_str)

df = pd.DataFrame(data=resp_json)

print(df)
