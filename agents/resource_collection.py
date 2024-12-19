class ResourceAssetCollectionAgent:
    def __init__(self, max_links=10):
        self.max_links = max_links  

    def search_datasets(self, keywords):
        """
        Search for datasets on Kaggle, Hugging Face, and GitHub, filtering duplicates
        and limiting the number of results.
        """
        resource_links = set()  # Using set to avoid duplicates
        platforms = ["kaggle.com", "huggingface.co", "github.com"]

        for keyword in keywords:
            for platform in platforms:
                if len(resource_links) >= self.max_links:
                    break
                link = f"https://{platform}/search?q={keyword.replace(' ', '+')}"
                resource_links.add(link)
        return list(resource_links)

    def filter_links(self, links):
        """
        Optional: Implement filtering logic for irrelevant links (if needed).
        """
        # Removing links containing specific unwanted keywords
        unwanted_keywords = ["test", "example"]
        filtered_links = [
            link for link in links if not any(kw in link for kw in unwanted_keywords)
        ]
        return filtered_links

    def save_resources(self, resource_links, filename="resource_links.md"):
        """
        Save resource links to a markdown file.
        """
        with open(filename, "w") as f:
            f.write("# Resource Links\n\n")
            for link in resource_links:
                f.write(f"- [{link}]({link})\n")
