import os
import requests
from agents import function_tool


def add_repository_stats(repositories: list):
    """
    Add statistics for each repository in the list.

    Args:
        repositories: List of dictionaries containing repository information

    Returns:
        List of repositories with added statistics
    """
    # TODO set the env variable with the gh token
    token = os.getenv("GITHUB_TOKEN")

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    for repo in repositories:
        # Extract owner and repo name from full_name (format: "owner/repo")
        owner, repo_name = repo["full_name"].split("/")

        # Get statistics endpoint
        stats_url = (
            f"https://api.github.com/repos/{owner}/{repo_name}/stats/participation"
        )

        try:
            response = requests.get(stats_url, headers=headers)

            # GitHub might respond with 202 if stats are being calculated
            if response.status_code == 202:
                print(f"Stats being calculated for {repo['full_name']}, waiting...")
                sleep(2)  # Wait and try again
                response = requests.get(stats_url, headers=headers)

            if response.status_code == 200:
                stats = response.json()

                # Get additional repository details
                details_url = f"https://api.github.com/repos/{owner}/{repo_name}"
                details_response = requests.get(details_url, headers=headers)
                details = details_response.json()

                # Add statistics to repository dictionary
                repo["stats"] = {
                    "commits_last_year": sum(
                        stats.get("all", [])
                    ),  # Total commits in the last year
                    "open_issues": details.get("open_issues_count", 0),
                    "forks": details.get("forks_count", 0),
                    "watchers": details.get("watchers_count", 0),
                    "network_count": details.get("network_count", 0),
                    "subscribers_count": details.get("subscribers_count", 0),
                    "last_update": details.get("updated_at", ""),
                    "language": details.get("language", ""),
                    "license": details.get("license", {}).get("name", "No license"),
                }
            else:
                print(
                    f"Failed to get stats for {repo['full_name']}: {response.status_code}"
                )
                repo["stats"] = None

        except Exception as e:
            print(f"Error processing {repo['full_name']}: {str(e)}")
            repo["stats"] = None

    return repositories


@function_tool
async def get_repos_statistics(repositories: list) -> list:
    """Uses the REST API from github to get the statistics from each repository in a list.
    The list contains 10 repositories and one dictionary for each repository

    Args:
        repositories: list with the 10 repositories to add the statistics

    Returns:
        list: the updated list of the 10 repositories with the statistics information
    """
    return add_repository_stats(repositories=repositories)
