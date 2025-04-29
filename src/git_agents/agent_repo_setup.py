import os
from agents import Agent
from git_agents_tools import clone_repository, sync_local_repo
from repository_assets import GitRepository


GIT_REPO_SETUP_SYSTEM_PROMPT = """
You are an Agent that helps to setup the git project such as git clone and sync.
Given a git url or local path, you have to clone or sync the repository respectively.
"""
GIT_REPO_SETUP_MODEL = os.getenv("GIT_SETUP_MODEL", "gpt-4o-mini")

agent_repo_setup = Agent[GitRepository](name="GitRepoSetup",
                     model=GIT_REPO_SETUP_MODEL,
                     instructions=GIT_REPO_SETUP_SYSTEM_PROMPT,
                     tools=[clone_repository, sync_local_repo],
                     output_type=GitRepository)
