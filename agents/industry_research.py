from utils.scraper import fetch_company_info, fetch_industry_info

class IndustryResearchAgent:
    def __init__(self):
        pass

    def search_company_info(self, company_name):
        return fetch_company_info(company_name)

    def get_industry_info(self, industry):
        return fetch_industry_info(industry)