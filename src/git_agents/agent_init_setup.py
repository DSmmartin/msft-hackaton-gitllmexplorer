import os

from agents import Agent
from git_agents_tools import clone_repository


GIT_INIT_SETUP_SYSTEM_PROMPT = """
You are an Agent that helps to prepare and initialize the git project such as git clone and sync.
"""
GIT_INIT_SETUP_MODEL = os.getenv("GIT_INIT_SETUP_MODEL", "gpt-4o-mini")

GitInitSetup = Agent(name="GitInitSetup",
                     model=GIT_INIT_SETUP_MODEL,
                     instructions=GIT_INIT_SETUP_SYSTEM_PROMPT,
                     tools=[clone_repository])
