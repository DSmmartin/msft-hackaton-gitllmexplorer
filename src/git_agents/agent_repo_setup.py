import os
from agents import Agent, OpenAIChatCompletionsModel
from git_agents_tools import clone_repository, sync_local_repo
from repository_assets import GitRepository
from model_client import get_model_client


GIT_REPO_SETUP_SYSTEM_PROMPT = """
You are an Agent that helps to setup the git project such as git clone and sync.
Given a git url or local path, you have to clone or sync the repository respectively.
"""
GIT_REPO_SETUP_MODEL = os.getenv("GIT_SETUP_MODEL", "gpt-4o-mini")

agent_repo_setup = Agent[GitRepository](
    name="GitRepoSetup",
    model=OpenAIChatCompletionsModel(
        model=GIT_REPO_SETUP_MODEL, openai_client=get_model_client()
    ),
    instructions=GIT_REPO_SETUP_SYSTEM_PROMPT,
    tools=[clone_repository, sync_local_repo],
    output_type=GitRepository,
)
