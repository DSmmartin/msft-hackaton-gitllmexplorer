import os
from agents import Agent
from git_agents_tools import git_commands, list_directory, read_file
from repository_assets import GitRepositoryLocation


GIT_COMMANDS_SYSTEM_PROMPT = """
You are Git commands executor given a local path git repository make git commands to explore.
"""
GIT_COMMANDS_MODEL = os.getenv("GIT_COMMANDS_MODEL", "gpt-4.1-mini")


agent_git_explorer = Agent[GitRepositoryLocation](name="RepositoryExplorer",
                     model=GIT_COMMANDS_MODEL,
                     instructions=GIT_COMMANDS_SYSTEM_PROMPT,
                     tools=[git_commands, list_directory, read_file],
                     )
