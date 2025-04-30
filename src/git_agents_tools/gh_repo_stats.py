import os
import requests
from typing import List
from agents import function_tool
from repository_assets import GitRepository


@function_tool
async def get_repos_statistics(
    repositories: List[GitRepository],
) -> List[dict]:
    """Uses the REST API from github to get the statistics from each repository in a list.
    The list contains repositories and one dictionary for each repository

    Args:
        list: the list of full name repositories to get the statistics.
        The full_name is a string that is the full name of the repository (i.e. `owner/repo`).

    Returns:
        list: the updated list of the repositories with the statistics information
    """
    token = os.getenv("GITHUB_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    stats_return = []
    for repo in repositories:

        owner, repo_name = repo.full_name.split("/")


        stats_url = (
            f"https://api.github.com/repos/{owner}/{repo_name}/stats/participation"
        )

        try:
            response = requests.get(stats_url, headers=headers)


            if response.status_code == 202:
                print(f"Stats being calculated for {repo.full_name}, waiting...")
                response = requests.get(stats_url, headers=headers)

            if response.status_code == 200:
                stats = response.json()

                details_url = f"https://api.github.com/repos/{owner}/{repo_name}"
                details_response = requests.get(details_url, headers=headers)
                details = details_response.json()

                stats_return.append({
                    "full_name": details_url,
                    "commits_last_year": sum(
                        stats.get("all", [])
                    ),
                    "open_issues": details.get("open_issues_count", 0),
                    "forks": details.get("forks_count", 0),
                    "watchers": details.get("watchers_count", 0),
                    "network_count": details.get("network_count", 0),
                    "subscribers_count": details.get("subscribers_count", 0),
                    "last_update": details.get("updated_at", ""),
                    "language": details.get("language", ""),
                })
            else:
                print(
                    f"Failed to get stats for {repo['full_name']}: {response.status_code}"
                )
                repo["stats"] = None

        except Exception as e:
            print(f"Error processing {repo['full_name']}: {str(e)}")
            repo["stats"] = None

    return stats_return
