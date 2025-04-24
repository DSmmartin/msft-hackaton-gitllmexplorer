import os
from agents import Agent, handoff
from git_agents.agent_repo_setup import agent_repo_setup
from git_agents.agent_git_commands import agent_git_commands_executor
from git_agents.agent_generate_response import agent_generate_response
from git_agents.agent_git_report import agent_git_report
from repository_assets import GitRepositoryLocation

GIT_ASSISTANT_SYSTEM_PROMPT = """
You are a helpful assistant that provides information in order to understand a repository for the user that is the first time they interact with it.
"""
GIT_ASSISTANT_MODEL = os.getenv("GIT_ASSISTANT_MODEL", "gpt-4o-mini")


agent_git_assistant = Agent[GitRepositoryLocation](name="GitAssistant",
                     model=GIT_ASSISTANT_MODEL,
                     instructions=GIT_ASSISTANT_SYSTEM_PROMPT,
                     tools=[
                         agent_repo_setup.as_tool(
                             tool_name="setup_git_repo",
                             tool_description="Setup git repository if a url or local path is provided, use this tool when it is required to explore the repository.",
                         ),
                         agent_git_commands_executor.as_tool(
                             tool_name="git_explorer",
                             tool_description="Use this is an Agent to make tasks in the repository interactively."
                         ),
                         agent_generate_response.as_tool(
                             tool_name="generate_response",
                             tool_description="Use always at the end to respond to the user. This tool generates a structured and guided response when the user asks for information about the repository elements: branches, commits, tags."
                         )
                     ],
                     handoffs=[handoff(agent_git_report, tool_description_override="Use this tool when the user asks for a report of the repository")]
                     )
