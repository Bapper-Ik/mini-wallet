

def users_serializer(user_info):
    return {
        "wallet_id": user_info.wallet_id,
        "first_name": user_info.first_name,
        "last_name": user_info.last_name,
        "email": user_info.email,
        "password": user_info.password,
        "phone": user_info.phone,
        "bvn": user_info.bvn,
        "bvn_dob": user_info.bvn_dob
    }
    

def wallet_serializer(wallet_info):
    return {
        "wallet_name": wallet_info["walletName"],
        "wallet_ref": wallet_info["walletReference"],
        "account_number": wallet_info["accountNumber"],
        "account_name": wallet_info["accountName"],
        "bank_name": "MONIE POINT",
        "bvn": wallet_info["bvnDetails"]["bvn"],
        "bvn_dob": wallet_info["bvnDetails"]["bvnDateOfBirth"],
        "balance": 0
    }


