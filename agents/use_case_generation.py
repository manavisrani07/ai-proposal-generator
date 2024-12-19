class UseCaseGenerationAgent:
    def __init__(self, llm):
        self.llm = llm
        self.prompt_template = """
You are an AI assistant specialized in the {industry_info} industry. Based on the company's information: {company_info}, analyze industry trends related to AI, ML, and automation. Propose relevant use cases where the company can leverage Generative AI, LLMs, and ML technologies to improve processes, enhance customer satisfaction, and boost operational efficiency. Provide detailed explanations for each use case.
"""

    def generate_use_cases(self, industry_info, company_info):
        prompt = self.prompt_template.format(
            industry_info=industry_info,
            company_info=company_info
        )
        return self.llm(prompt)