


import os
import google.generativeai as genai
import requests
import time
from openpyxl import Workbook
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API credentials from environment variables
API_KEY = os.getenv('GODADDY_API_KEY')
API_SECRET = os.getenv('GODADDY_API_SECRET')
API_KEY_GENIE = os.getenv('GEMINI_API_KEY')

# OTE API base URL
BASE_URL = "https://api.ote-godaddy.com"

# Excel file setup
workbook = Workbook()
sheet = workbook.active
sheet.title = "Domain Availability"
sheet.append(["name", "availability", "Price"])

# Domain availability check function
def check_domain_availability(domain_name):
    url = f"{BASE_URL}/v1/domains/available?domain={domain_name}.com"
    
    headers = {
        "Authorization": f"sso-key {API_KEY}:{API_SECRET}",
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            availability = response.json().get('available')
            return availability
        except ValueError:
            print("Failed to decode JSON response.")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Set your Gemini API key
genai.configure(api_key=API_KEY_GENIE)

# Generate app names using the Gemini API
def generate_app_name(prompt):
    response = genai.generate_text(prompt=prompt)
    result = response.result
    
    # Split the result into lines and clean up each line
    names = result.split('\n')
    clean_names = []
    
    for name in names:
        # Strip unwanted characters and check if there is a dot
        if '.' in name:
            # Split and clean the name
            cleaned_name = name.split('.')[1].strip().replace('*', '')
            if cleaned_name:  # Make sure the cleaned name is not empty
                clean_names.append(cleaned_name)
    
    return clean_names

# Main loop to continuously generate names and check their availability
try:
    while True:
        # Prompt for generating nam


        with open('helper_functions/prompt.txt', 'r') as file:
            prompt = file.read()
        
        web_app_names = generate_app_name(prompt)
        
        for web_app_name in web_app_names:
            print(web_app_name)
            if web_app_name:
                is_available = check_domain_availability(web_app_name)
                if is_available is not None:
                    availability_status = "Available" if is_available else "Not Available"
                    print(f"Domain {web_app_name}.com is {availability_status}")
                    
                    # Write to Excel sheet
                    sheet.append([web_app_name, availability_status, 'n/a'])
                    workbook.save('output.csv')
        
        # Pause for a short time to avoid API rate limits
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Script terminated by user.")

finally:
    workbook.save('output.csv')
    print("Results saved to 'output.csv'")
