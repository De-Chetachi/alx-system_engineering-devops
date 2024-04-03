#!/usr/bin/env python3
import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('hbtp0Gef2DBqDMaH2qRqSA', '_NswMz46VY3mdjx3nqdSelThQH5J3g')
post_data = {"grant_type": "password", "username": "Cautious_Relief_6373", "password": "pwd"}
headers = {"User-Agent": "ChangeMeClient/0.1 by Cautious_Relief_6373"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())
