import streamlit as st
from agents.industry_research import IndustryResearchAgent
from agents.use_case_generation import UseCaseGenerationAgent
from agents.resource_collection import ResourceAssetCollectionAgent
from agents.genai_proposer import GenAISolutionsProposerAgent
from agents.final_proposal import FinalProposalAgent
from llms.groq_api import GroqAPI

def validate_api_key(api_key, model_name="llama3-8b-8192"):
    """Attempt a simple call to validate the API key."""
    try:
        llm = GroqAPI(api_key=api_key, model_name=model_name)
        # A simple test prompt to check validity
        test_response = llm("Test prompt for API key validation")
        if test_response:
            return True
    except Exception as e:
        st.error(f"API Key validation failed: {e}")
    return False

def run_pipeline(api_key, company_name, industry, model_name="llama3-8b-8192"):
    st.write("### Running the pipeline...")
    st.write("Gathering company and industry information...")
    industry_agent = IndustryResearchAgent()
    company_info = industry_agent.search_company_info(company_name)
    industry_info = industry_agent.get_industry_info(industry)

    st.write("Generating use cases...")
    llm = GroqAPI(api_key=api_key, model_name=model_name)
    use_case_agent = UseCaseGenerationAgent(llm)
    use_cases = use_case_agent.generate_use_cases(industry_info, company_info)

    st.write("Collecting resource links...")
    resource_agent = ResourceAssetCollectionAgent()
    keywords = [company_name, industry] + use_cases.split()
    resource_links = resource_agent.search_datasets(keywords)
    resource_agent.save_resources(resource_links)

    st.write("Proposing GenAI solutions...")
    genai_agent = GenAISolutionsProposerAgent(llm)
    genai_solutions = genai_agent.propose_solutions(industry_info, company_info)

    st.write("Compiling final proposal...")
    final_agent = FinalProposalAgent()
    report = final_agent.compile_report(use_cases, genai_solutions, resource_links)
    final_agent.save_report(report)

    st.success("Final proposal generated and saved to 'final_proposal.md'.")
    st.write("### Report Preview:")
    st.markdown(report)

def main():
    st.title("AI Proposal Generator")

    st.write("""
    This application generates an AI-based proposal for a given company and industry.
    
    **Instructions**:
    - Enter the company name and industry.
    - Click the 'Run' button.

    **This AI Proposal Generator automates the process of creating detailed business proposals by**:

    - Collecting company and industry information.
    - Generating relevant use cases based on trends and requirements.
    - Proposing AI/ML solutions tailored to the company’s needs.
    - Collecting relevant datasets and resources.
    - Compiling all the information into a structured final report.
    """)

    # If you prefer storing the API key in Streamlit secrets, you can retrieve it:
    api_key = st.secrets["general"]["GROQ_API_KEY"]
    # Otherwise, ask the user for the API key:
    #api_key = st.text_input("Enter your Groq API Key:", type="password")

    company_name = st.text_input("Enter the company name:")
    industry = st.text_input("Enter the industry:")

    if st.button("Run"):
        if not api_key:
            st.error("Please provide a valid Groq API key.")
            return
        if not company_name:
            st.error("Please provide a company name.")
            return
        if not industry:
            st.error("Please provide an industry.")
            return

        st.write("Validating API Key...")
        if validate_api_key(api_key):
            st.success("API Key is valid!")
            run_pipeline(api_key, company_name, industry)
        else:
            st.error("Invalid API Key. Please try again.")

if __name__ == "__main__":
    main()
