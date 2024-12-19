import os
from agents.industry_research import IndustryResearchAgent
from agents.use_case_generation import UseCaseGenerationAgent
from agents.resource_collection import ResourceAssetCollectionAgent
from agents.genai_proposer import GenAISolutionsProposerAgent
from agents.final_proposal import FinalProposalAgent
from llms.groq_api import GroqAPI

def main():
    # User inputs
    company_name = input("Enter the company name: ").strip()
    industry = input("Enter the industry: ").strip()

    # Paste your Groq API key here
    API_KEY = "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"  

    # Choose the model you want to use
    model_name = "llama3-8b-8192"
    # Other options: "llama3-groq-70b", "llama-3.1-70b", "llama3-groq-8b", "gemma-7b-it"

    # Initialize the GroqAPI LLM
    llm = GroqAPI(api_key=API_KEY, model_name=model_name)

    # Initialize agents
    industry_agent = IndustryResearchAgent()
    use_case_agent = UseCaseGenerationAgent(llm)
    resource_agent = ResourceAssetCollectionAgent()
    genai_agent = GenAISolutionsProposerAgent(llm)
    final_agent = FinalProposalAgent()

    # Agent 1: Industry Research
    print("\nGathering company and industry information...")
    company_info = industry_agent.search_company_info(company_name)
    industry_info = industry_agent.get_industry_info(industry)

    # Agent 2: Use Case Generation
    print("\nGenerating use cases...")
    use_cases = use_case_agent.generate_use_cases(industry_info, company_info)

    # Agent 3: Resource Asset Collection
    print("\nCollecting resource links...")
    keywords = [company_name, industry] + use_cases.split()
    resource_links = resource_agent.search_datasets(keywords)
    resource_agent.save_resources(resource_links)

    # Agent 4: GenAI Solutions Proposer
    print("\nProposing GenAI solutions...")
    genai_solutions = genai_agent.propose_solutions(industry_info, company_info)

    # Agent 5: Final Proposal
    print("\nCompiling final proposal...")
    report = final_agent.compile_report(use_cases, genai_solutions, resource_links)
    final_agent.save_report(report)

    print("\nFinal proposal generated and saved to 'final_proposal.md'.")

if __name__ == "__main__":
    main()