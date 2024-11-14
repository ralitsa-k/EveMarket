import requests
import base64
import json
import random
import string

# Step 1: Get the Authorization Code
client_id = '6efe90e7510940bfb16854dc28b02aec'
client_secret = 'hzu0VWVHIeGmpYr3wI5XtJjRhpVoFBhBj2R0tkvJ'
redirect_uri = 'eveauth-app://Ronayada/'
scopes = 'esi-assets.read_assets.v1'
state = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
auth_url = (
    f"https://login.eveonline.com/v2/oauth/authorize/"
    f"?response_type=code&redirect_uri={redirect_uri}&client_id={client_id}&scope={scopes}&state={state}"
)

print(f"Go to the following URL to authorize the application: {auth_url}")

# User should be redirected back to your callback URL with a code parameter
authorization_code = input("Enter the authorization code: ")

# Step 2: Exchange Authorization Code for Access Token
token_url = "https://login.eveonline.com/v2/oauth/token"
auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

headers = {
    'Authorization': f'Basic {auth_header}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
}

response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
    tokens = response.json()
    access_token = tokens['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token: {response.status_code} - {response.text}")

# Step 3: Use Access Token to Make Authenticated Requests
# Example: Get Character Wallet Balance
character_id = '2120194109'
wallet_url = f"https://esi.evetech.net/latest/characters/{character_id}/wallet/"

auth_headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(wallet_url, headers=auth_headers)

if response.status_code == 200:
    wallet_balance = response.json()
    print(f"Wallet Balance: {wallet_balance}")
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")

