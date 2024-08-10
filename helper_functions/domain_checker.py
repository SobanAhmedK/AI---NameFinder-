"""This file will be responsible for checking the name availability on the Godaddy

Inputs: Array of Names
functionality: Send the names to goDaddy.com one by one and see the status of names given
Output: return list of responses


"""

import requests
import openpyxl
import os
from dotenv import load_dotenv

load_dotenv()


# Replace with your GoDaddy API Key and Secret
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


# Function to check domain availability and pricing
def check_domain_availability_and_pricing(domain):
    url = f'https://api.ote-godaddy.com/v1/domains/available?domain={domain}.com'

    headers = {
        'Authorization': f'sso-key {API_KEY}:{API_SECRET}',
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        available = data.get('available', False)
        pricing = data.get('price', 'N/A')  # Adjust if the pricing information is in a different field
        return available, pricing
    else:
        print(f"Error checking domain {domain}: {response.text}")
        return None, None



def name_checker(names: list):
    list_of_response = []

    for domain in names:
        available, price = check_domain_availability_and_pricing(domain)
        list_of_response.append({'domain': domain, 'available': available, 'price': price})
    print(list_of_response)
    return list_of_response



