import os
import requests
from agents import function_tool


def get_list_repositories(
    query: str, sorting_metric: str = "stars", order: str = "desc"
):
    # TODO set the env variable with the gh token
    token = os.getenv("GITHUB_TOKEN")

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/search/repositories?q={query}&sort={sorting_metric}&order={order}&per_page=10"

    # Send request
    response = requests.get(url, headers=headers)
    results = []
    if response.status_code == 200:
        data = response.json()

        # Print results
        print(f"Total repositories found: {data['total_count']}")
        # print(f"Top 10 repositories by stars:")
        for repo in data["items"]:
            item = {}
            # print(f"\nRepository: {repo['full_name']}")
            item["full_name"] = repo["full_name"]
            # print(f"Description: {repo['description']}")
            item["description"] = repo["description"]
            # print(f"URL: {repo['html_url']}")
            item["url"] = repo["html_url"]
            if sorting_metric == "starts":
                # print(f"Stars: {repo['stargazers_count']}")
                item["stargazers_count"] = repo["stargazers_count"]
            results.append(item)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    return results


@function_tool
async def get_best_repositories(topic: str, metric: str) -> list:
    """Uses the REST API from github to get the top 10 list of most popular
    repositories according to some metric.

    Args:
        topic: the topic to use in the query
        metric: popularity metric to use in the github api

    Returns:
        list: the list of top 10 repositories according to the provided metric
    """
    return get_list_repositories(query=topic, metric="stars")


# if __name__ == "__main__":
#     get_list_repositories(query="flask")
