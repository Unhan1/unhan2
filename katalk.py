import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = 'c7151035e2f8c15d29dba61390d12bc4'
redirect_uri = 'https://example.com/oauth'
code = 'WogO37ndo6KhFvWLftRlVPZKV23c27kWfYXDzofaHtidygRbvBsyfWqph4UKKclfAAABi1dLAZgh5oEAb4_jFQ'

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)
