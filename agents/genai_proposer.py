class GenAISolutionsProposerAgent:
    def __init__(self, llm):
        self.llm = llm
        self.prompt_template = """
You are an AI assistant specialized in the {industry_info} industry. Based on the company's information: {company_info}, do the following:

1. Analyze current industry trends related to AI, ML, and automation.
2. Propose 5 relevant use cases where the company can leverage Generative AI, LLMs, and ML technologies.
3. For each use case, provide:
   - A title
   - A detailed explanation
   - Potential benefits

Format your response as a numbered list.
"""

    def propose_solutions(self, industry_info, company_info):
        prompt = self.prompt_template.format(
            industry_info=industry_info,
            company_info=company_info
        )
        return self.llm(prompt)