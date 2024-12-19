class FinalProposalAgent:
    def __init__(self):
        pass

    def compile_report(self, use_cases, genai_solutions, resource_links):
        """
        Compile a structured markdown report with improved formatting and a Table of Contents.
        """
        # Start the report with a title and table of contents
        report = (
            "# Final Proposal\n\n"
            "## Table of Contents\n"
            "1. [Top Use Cases](#top-use-cases)\n"
            "2. [GenAI Solutions](#genai-solutions)\n"
            "3. [Resource Links](#resource-links)\n\n"
        )

        # Add use cases section
        report += "## Top Use Cases\n\n"
        if use_cases.strip():
            report += use_cases.strip() + "\n\n"
        else:
            report += "No use cases were generated.\n\n"

        # Add GenAI solutions section
        report += "## GenAI Solutions\n\n"
        if genai_solutions.strip():
            report += genai_solutions.strip() + "\n\n"
        else:
            report += "No GenAI solutions were proposed.\n\n"

        # Add resource links section
        report += "## Resource Links\n\n"
        if resource_links:
            for link in resource_links:
                report += f"- [{link}]({link})\n"
        else:
            report += "No resource links were found.\n"

        return report

    def save_report(self, report, filename="final_proposal.md"):
        """
        Save the compiled report to a markdown file.
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)