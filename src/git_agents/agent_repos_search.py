import os
from agents import Agent
from git_agents_tools.gh_repos_search import get_best_repositories
from git_agents_tools.gh_repo_stats import get_repos_statistics

REPOS_SEARCH_SYSTEM_PROMPT = """
You are an Agent that generates a list of top repositories for a given topic and according to a gvien popularity metric.
Given the topic and the metric you need to search the top 10 repositories and you need to add the repository statistics
information to each repository of the list.
"""
REPOS_SEARCH_MODEL = os.getenv("REPOS_SEARCH_MODEL", "gpt-4o-mini")

agent_repos_search = Agent(name="GithubRepositoriesSearch",
                     model=REPOS_SEARCH_MODEL,
                     instructions=REPOS_SEARCH_SYSTEM_PROMPT,
                     tools=[get_best_repositories, get_repos_statistics],
                     output_type=list
)