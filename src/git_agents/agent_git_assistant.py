import os
from agents import Agent
from git_agents.agent_repo_setup import agent_repo_setup
from git_agents.agent_git_commands import agent_git_commands_executor

GIT_ASSISTANT_SYSTEM_PROMPT = """
You are a helpful assistant that answers questions about Git Tool.
"""
GIT_ASSISTANT_MODEL = os.getenv("GIT_ASSISTANT_MODEL", "gpt-4o-mini")


agent_git_assistant = Agent(name="GitAssistant",
                     model=GIT_ASSISTANT_MODEL,
                     instructions=GIT_ASSISTANT_SYSTEM_PROMPT,
                     tools=[
                         agent_repo_setup.as_tool(
                             tool_name="setup_git_repo",
                             tool_description="Setup git repository such as clone and sync in a secure manner."
                         ),
                         agent_git_commands_executor.as_tool(
                             tool_name="git_commands_executor",
                             tool_description="Execute git commands in a local repository. You can use this tool to explore the repository and get information about it."
                         )
                     ]
                     )
