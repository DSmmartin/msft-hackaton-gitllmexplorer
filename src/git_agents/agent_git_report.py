import os
from agents import Agent
from git_agents.agent_repo_setup import agent_repo_setup
from git_agents.agent_git_commands import agent_git_commands_executor
from git_agents.agent_generate_response import agent_generate_response
from repository_assets import GitRepositoryLocation

TIME_HORIZON_MONTHS = 6

GIT_REPORT_SYSTEM_PROMPT = F"""
You are an specialized Agent that generates a git report given a git repository. You have to generate a report providing the following information:
1. **Branch Workflow**: Describe the branch workflow used in the repository (Git Flow, GitHub Flow, GitLabFlow, One Flow...). Include information about the main branch, development branches, feature branches, and any other relevant branches.

The horizon of the report is 6 months, so you have to provide the information of the last {TIME_HORIZON_MONTHS} months. The report should be structured and easy to read. Use markdown format to generate the report. The report should be in English. You can use the tools provided to you to explore the repository and generate the report.
"""


GIT_REPORT_MODEL = os.getenv("GIT_REPORT_MODEL", "gpt-4o-mini")


agent_git_report = Agent[GitRepositoryLocation](name="GitReport",
                     model=GIT_REPORT_MODEL,
                     instructions=GIT_REPORT_SYSTEM_PROMPT,
                     tools=[
                         agent_repo_setup.as_tool(
                             tool_name="setup_git_repo",
                             tool_description="Setup git repository if a url or local path is provided, use this tool when it is required to explore the repository.",
                         ),
                         agent_git_commands_executor.as_tool(
                             tool_name="git_explorer",
                             tool_description="Use this is an Agent to make tasks in the repository interactively."
                         )
                     ]
                     )
