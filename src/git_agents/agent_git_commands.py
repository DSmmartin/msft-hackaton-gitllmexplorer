import os
from agents import Agent
from git_agents_tools import git_commands

GIT_COMMANDS_SYSTEM_PROMPT = """
You are Git commands executor given a local path git repository make git commands to explore.
"""
GIT_COMMANDS_MODEL = os.getenv("GIT_COMMANDS_MODEL", "gpt-4o-mini")


agent_git_commands_executor = Agent(name="GitCommandsExecutor",
                     model=GIT_COMMANDS_MODEL,
                     instructions=GIT_COMMANDS_SYSTEM_PROMPT,
                     tools=[git_commands]
                     )
