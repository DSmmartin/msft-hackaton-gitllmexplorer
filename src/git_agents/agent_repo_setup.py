import os

from agents import Agent
from git_agents_tools import clone_repository


GIT_REPO_SETUP_SYSTEM_PROMPT = """
You are an Agent that helps to setup the git project such as git clone and sync.
"""
GIT_REPO_SETUP_MODEL = os.getenv("GIT_SETUP_MODEL", "gpt-4o-mini")

agent_repo_setup = Agent(name="GitRepoSetup",
                     model=GIT_REPO_SETUP_MODEL,
                     instructions=GIT_REPO_SETUP_SYSTEM_PROMPT,
                     tools=[clone_repository])
