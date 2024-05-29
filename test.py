from  app.utils.hashing_password import pwd_context

import requests, base64, json



# Define your API key and client secret
api_key = 'MK_TEST_AT8WRK8Y7G'  
client_secret = 'LYD5LRCKUQFXCTQBZVS6DJ4RABU4RZJ1'

# Encode API key and client secret in base64 for Basic authentication
auth_str = f'{api_key}:{client_secret}'
auth_b64 = base64.b64encode(auth_str.encode()).decode()


# def create_user_wallet():
    
#     # Construct the Authorization header with Basic authentication
#     headers = {
#         'Authorization': f'Basic {auth_b64}',
#         'Content-Type': 'application/json',  # Specify the content type for the request body
#     }

#     # Define the request body parameters
#     body_params = {
#         "walletReference": f"ref43123332",
#         "walletName": "Staging Wallet - ref16804248425966",
#         "customerName": f"john doe",
#         "bvnDetails": {
#             "bvn": f"22421665930",
#             "bvnDateOfBirth": f"1999-05-23"
#         },
#         "customerEmail": f"user@example.com"
#     }

#     # Convert the request body to JSON format
#     body_json = json.dumps(body_params)

#     # Make the API request
#     base_url = 'https://sandbox.monnify.com'  # Replace this with your actual base URL
#     endpoint = '/api/v1/disbursements/wallet'
#     url = f'{base_url}{endpoint}'

#     response = requests.post(url, headers=headers, data=body_json)
#     res_json = response.json()
    
#     return res_json


# print(create_user_wallet())


# def initiate_transfer():
    
#     headers = {
#         'Authorization': f'Basic {auth_b64}',
#         'Content-Type': 'application/json',  
#     }

#     body_params = {
#         "amount": 200,
#         "reference": f"ref-4992",
#         "narration": f"testing",
#         "destinationBankCode": f"001",
#         "destinationAccountNumber": f"1711315986",
#         "currency": f"NGN",
#         "sourceAccountNumber": f"3689699179"
#     }
    
#     body_json = json.dumps(body_params)
        
#     base_url = 'https://sandbox.monnify.com' 
#     endpoint = '/api/v2/disbursements/single'
#     url = f'{base_url}{endpoint}'

#     response = requests.post(url, headers=headers, data=body_json)
#     res_json = response.json()    

#     # return res_json
#     if res_json["requestSuccessful"]:
#         res_body = res_json["responseBody"]
        
#         return res_body


# print(initiate_transfer())


def verify_OTP():
    headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/json',  
    }

    body_params = {
        "reference": f"ref-4992",
        "authorizationCode": "714714"
    }

    body_json = json.dumps(body_params)

    base_url = 'https://sandbox.monnify.com' 
    endpoint = '/api/v2/disbursements/single/validate-otp'
    url = f'{base_url}{endpoint}'

    response = requests.post(url, headers=headers, data=body_json)
    res_json = response.json()    

    return res_json
    # if res_json["requestSuccessful"]:
    #     res_body = res_json["responseBody"]
    #     return res_body


print(verify_OTP())


