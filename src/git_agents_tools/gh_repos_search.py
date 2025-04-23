import os
import requests


def get_list_repositories(query: str):
    # TODO set the env variable with the gh token
    token = os.getenv("GITHUB_TOKEN")

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page=10"

    # Send request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Print results
        print(f"Total repositories found: {data['total_count']}")
        print(f"Top 10 repositories by stars:")
        for repo in data["items"]:
            print(f"\nRepository: {repo['full_name']}")
            print(f"Description: {repo['description']}")
            print(f"URL: {repo['html_url']}")
            print(f"Stars: {repo['stargazers_count']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    get_list_repositories(query="flask")
