import os
from agents import Agent, OpenAIChatCompletionsModel
from repository_assets import GitRepository
from git_agents_tools import git_commands, list_directory, read_file
from model_client import get_model_client


GIT_COMMANDS_SYSTEM_PROMPT = """
You are Git commands executor given a local path git repository make git commands to explore.
"""
GIT_COMMANDS_MODEL = os.getenv("GIT_COMMANDS_MODEL", "gpt-4.1-mini")


agent_git_explorer = Agent[GitRepository](
    name="RepositoryExplorer",
    model=OpenAIChatCompletionsModel(
        model=GIT_COMMANDS_MODEL, openai_client=get_model_client()
    ),
    instructions=GIT_COMMANDS_SYSTEM_PROMPT,
    tools=[git_commands, list_directory, read_file],
)
