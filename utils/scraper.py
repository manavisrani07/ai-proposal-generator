import requests
from bs4 import BeautifulSoup

def fetch_company_info(company_name):
    try:
        search_query = f"{company_name} company overview"
        search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        info = ''
        for span in soup.find_all('span'):
            info += span.text + ' '
        # Limit the info to a reasonable length
        info = info[:1000]
        return info.strip()
    except Exception as e:
        print(f"Error fetching company info: {e}")
        return f"Could not retrieve information about {company_name}."

def fetch_industry_info(industry):
    try:
        search_query = f"{industry} industry trends"
        search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        info = ''
        for span in soup.find_all('span'):
            info += span.text + ' '
        # Limit the info to a reasonable length
        info = info[:1000]
        return info.strip()
    except Exception as e:
        print(f"Error fetching industry info: {e}")
        return f"Could not retrieve information about {industry} industry."