from  app.utils.hashing_password import pwd_context
import requests, base64, json

import os

api_key = os.getenv("API_KEY")  
client_secret = os.getenv("CLIENT_SECRET")

auth_str = f'{api_key}:{client_secret}'
auth_b64 = base64.b64encode(auth_str.encode()).decode()

    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def create_user_wallet(user_info):    
    
    headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/json',  
    }

    body_params = {
        "walletReference": f"{user_info['wallet_id']}",
        "walletName": f"PlanexTech-{user_info['wallet_id']}",
        "customerName": f"{user_info["first_name"]} {user_info["last_name"]}",
        "bvnDetails": {
            "bvn": f"{user_info["bvn"]}",
            "bvnDateOfBirth": f"{user_info["bvn_dob"]}"
        },
        "customerEmail": f"{user_info["email"]}"
    }
    
    body_json = json.dumps(body_params)
        
    base_url = 'https://sandbox.monnify.com' 
    endpoint = '/api/v1/disbursements/wallet'
    url = f'{base_url}{endpoint}'

    response = requests.post(url, headers=headers, data=body_json)
    res_json = response.json()    
    if res_json["requestSuccessful"]:
        res_body = res_json["responseBody"]
        return res_body


async def initiate_transfer(transfer_info):

    headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/json',  
    }

    body_params = {
        "amount": transfer_info.amount,
        "reference": f"{transfer_info.reference}",
        "narration": f"{transfer_info.narration}",
        "destinationBankCode": f"{transfer_info.destinationBankCode}",
        "destinationAccountNumber": f"{transfer_info.destinationAccountNumber}",
        "currency": f"{transfer_info.currency}",
        "sourceAccountNumber": f"{transfer_info.sourceAccountNumber}"
    }

    body_json = json.dumps(body_params)

    base_url = 'https://sandbox.monnify.com' 
    endpoint = '/api/v2/disbursements/single'
    url = f'{base_url}{endpoint}'

    response = requests.post(url, headers=headers, data=body_json)
    res_json = response.json()    

    if res_json["requestSuccessful"]:
        res_body = res_json["responseBody"]
        return res_body



async def verify_OTP(transfer_info):
    headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/json',  
    }

    body_params = {
        "reference": f"{transfer_info.reference}",
        "authorizationCode":f"{transfer_info.authorizationCode}"
    }

    body_json = json.dumps(body_params)

    base_url = 'https://sandbox.monnify.com' 
    endpoint = '/api/v2/disbursements/single/validate-otp'
    url = f'{base_url}{endpoint}'

    response = requests.post(url, headers=headers, data=body_json)
    res_json = response.json()    

    if res_json["requestSuccessful"]:
        res_body = res_json["responseBody"]
        return res_body
