import requests
from decouple import config

def get_grant_token():
    url = f'{config('BASE_URL')}/tokenized/checkout/token/grant'

    headers = {

        'Content-Type':'application/json',
        'Accept':'application/json',
        'username':config('BKASH_USERNAME'),
        'password':config('BKASH_PASSWORD')
    }

    data = {
        'app_key' : config('BKASH_APP_KEY'),
        'app_secret' : config('BKASH_APP_SECRET')
    }
    response = requests.post(url,json=data,headers=headers)
    return response.json()


def create_payment(token,amount,invoice):

    url = f'{config('BASE_URL')}/tokenized/checkout/create'
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token,
        "X-App-Key": config('BKASH_APP_KEY'),
    }
    data = {
        "mode": "0011",
        "payerReference": "01770618575",
        "callbackURL": config('BKASH_CALLBACK_URL'),
        "amount": str(amount),
        "currency": "BDT",
        "intent": "sale",
        "merchantInvoiceNumber": str(invoice)
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()


def execute_payment(token, payment_id):
    url = f"{config('BASE_URL')}/tokenized/checkout/execute"
    headers = {
        "Accept": "application/json",
        "Authorization": token,
        "X-App-Key": config('BKASH_APP_KEY'),
    }
    data = {
        "paymentID": payment_id
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()