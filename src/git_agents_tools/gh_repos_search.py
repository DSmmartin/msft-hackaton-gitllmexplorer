import os
import requests
from typing import List
from agents import function_tool
from repository_assets import GitRepository

@function_tool
async def get_best_repositories(
    topic: str,
    ) -> List[GitRepository]:
    """Uses the REST API from github to get the top 10 list of most popular
    repositories according to some metric.

    Args:
        topic: the topic to use in the query

    Returns:
        ListOfRepositories: the list of top 10 repositories according to the provided metric, sorted in descending order.
        The list contains dictionaries with the following keys:
            - full_name: the full name of the repository
            - description: the description of the repository
            - url: the url of the repository
    """
    headers = {
        "Authorization": f"Bearer {os.getenv("GITHUB_TOKEN")}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/search/repositories?q={topic}&sort=stars&order=desc&per_page=10"

    response = requests.get(url, headers=headers)
    results = []
    if response.status_code == 200:
        data = response.json()

        print(f"Total repositories found: {data['total_count']}")
        for repo in data["items"]:
            item = {}
            item["full_name"] = repo["full_name"]
            item["description"] = repo["description"]
            item["url"] = repo["html_url"]
            item["stargazers_count"] = repo["stargazers_count"]
            results.append(GitRepository(**item))
        return results

    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    return results
