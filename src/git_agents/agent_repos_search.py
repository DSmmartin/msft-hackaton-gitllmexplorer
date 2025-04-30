import os
from agents import Agent, OpenAIChatCompletionsModel
from git_agents_tools.gh_repos_search import get_best_repositories
from git_agents_tools.gh_repo_stats import get_repos_statistics
from model_client import get_model_client


REPOS_SEARCH_SYSTEM_PROMPT = """
You are an Agent that generates a list of top repositories for a given topic and according to a given popularity metric.
Given the topic and the metric you need to search the top 10 repositories and you need to add the repository statistics
information to each repository of the list.
"""
REPOS_SEARCH_MODEL = os.getenv("REPOS_SEARCH_MODEL", "gpt-4.1-mini")

agent_repos_search = Agent(
    name="GithubRepositoriesSearch",
    model=OpenAIChatCompletionsModel(
        model=REPOS_SEARCH_MODEL, openai_client=get_model_client()
    ),
    instructions=REPOS_SEARCH_SYSTEM_PROMPT,
    tools=[get_best_repositories, get_repos_statistics],
)
