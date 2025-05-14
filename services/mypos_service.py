import requests
from flask import current_app
import base64
import uuid

def generate_transaction_id():
    return uuid.uuid4().int >> 96 


def generate_oauth_token():
    client_id = current_app.config['MYPOS_CLIENT_ID']
    client_secret = current_app.config['MYPOS_CLIENT_SECRET']
    oauth_url=current_app.config['MYPOS_OAUTH_API_URL']

    # Encode client_id:client_secret as Base64
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # Prepare request
    response = requests.post(
        url=oauth_url,  # or production URL
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_credentials}"
        },
        data={
            "grant_type": "client_credentials"
        }
    )
    token=response.json().get('access_token')
    return token


def request_myposdeposit(quotation_id,title,amount, currency, customer_email):
    """
    Request a deposit payment via MyPOS TRANSACTION API
    """
    client_id = current_app.config['MYPOS_CLIENT_ID']
    api_url = current_app.config['MYPOS_TRANSACTION_API_URL']
    merchant_id = current_app.config['MYPOS_MERCHANT_ID']
    oauth_bearer_token = generate_oauth_token()
    
    payload = {
        "item_name": title,
        "item_price": amount,
        "pref_language": "EN",
        "currency": currency,
        "account_number": merchant_id,
        "custom_name": "Payment Link",
        "quantity": 1,
    }

    
    headers = {
        'API-Key': client_id,
        'X-Request-ID': str(quotation_id)+' '+title,
        'Authorization': f'Bearer {oauth_bearer_token}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response_data = response.json()
        
        if response.status_code == 200:
            return {
                'success': True,
                'payment_url': response_data.get('url'),
                'transaction_id':generate_transaction_id()
            }
        else:
            current_app.logger.error(f"MyPOS API error: {response_data}")
            return {
                'success': False,
                'error': response_data.get('message', 'Unknown error')
            }
    except Exception as e:
        current_app.logger.error(f"MyPOS API request error: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }