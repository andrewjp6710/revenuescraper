import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import re
from random import randint
from googlesearch import search
from urllib.parse import urlparse
from fuzzywuzzy import fuzz

# Replace with your ScrapeOps API key
SCRAPEOPS_API_KEY = '3db81d31-3467-41e2-9a65-0e7b629819f9'

# User agent headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Function to get a list of user agent headers from ScrapeOps
def get_headers_list():
    response = requests.get('http://headers.scrapeops.io/v1/browser-headers?api_key=' + SCRAPEOPS_API_KEY)
    json_response = response.json()
    return json_response.get('result', [])

# Function to get a random header from the list
def get_random_header(header_list):
    random_index = randint(0, len(header_list) - 1)
    return header_list[random_index]

# Function to choose the best matching link from the top 2 results
def choose_best_matching_link(account, top_results):
    if top_results:
        best_match = None
        best_similarity = 0

        for result in top_results:
            link = result
            parsed_link = urlparse(link)
            similarity = fuzz.partial_ratio(account.lower(), parsed_link.netloc.lower())
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = link

        if best_match:
            return best_match
        else:
            # If no best match was found, return the first suggested link
            return top_results[0]
    return "Not available"

# Function to scrape revenue information for a single account
def scrape_revenue(account, region):
    search_query = f"{account} zoom info revenue {region}"
    top_results = []

    for site_url in search(search_query, tld="co.in", num=2, stop=2, pause=2):
        top_results.append(site_url)

    selected_link = choose_best_matching_link(account, top_results)

    if selected_link:
        response = requests.get(
            url='https://proxy.scrapeops.io/v1/',
            params={
                'api_key': SCRAPEOPS_API_KEY,
                'url': selected_link,
            },
            headers=HEADERS
        )

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract text from the page
        text = soup.get_text()
        
        # Use regex to find revenue information
        revenue_matches = re.findall(r'\$<?\d+(?:,\d+)*(?:\.\d+)?', text)
        
        if revenue_matches:
            match_using_text = revenue_matches[0]
        else:
            match_using_text = "Not available"
        
        return match_using_text

    return "Not available"

# Function to export data to an Excel file
def export_to_excel(data, output_path):
    workbook = xlsxwriter.Workbook(output_path)
    worksheet1 = workbook.add_worksheet()

    row = 0
    col = 0

    for name, rev in data:
        try:
            worksheet1.write(row, col, name)
            worksheet1.write(row, col+1, rev)
        except:
            pass
        row += 1

    workbook.close()

def main():
    print('Hello!')

    # Input from the user
    region = input("Please input your account region (e.g. New South Wales, New Zealand, Queensland etc): ")
    fileName = input("Please input the name of the Excel File (including '.xlsx'). Please ensure the code and the Excel file are located in the same directory/folder: ")

    base_dir = os.getcwd()
    excelFinalPath = os.path.join(base_dir, fileName)

    data = pd.read_excel(excelFinalPath)
    df = pd.DataFrame(data, columns=["account_name"])
    mylist = data['account_name'].tolist()

    listofRevenue = []

    # Loop through the list of accounts and scrape revenue information
    for account in mylist:
        revenue = scrape_revenue(account, region)
        print(f"Account: {account} Revenue: {revenue}")
        listofRevenue.append((account, revenue))

    # Export the scraped data to an Excel file
    export_to_excel(listofRevenue, excelFinalPath)

if __name__ == "__main__":
    main()
