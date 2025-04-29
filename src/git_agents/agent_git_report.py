import os
from agents import Agent
from git_agents.agent_repo_setup import agent_repo_setup
from repository_assets import GitRepository
from git_agents.agent_git_commands import agent_git_explorer


TIME_HORIZON_MONTHS = 6

GIT_REPORT_SYSTEM_PROMPT = F"""
You are a specialized Agent that generates a git report given a git repository. You have to generate a report providing the following information:

1. What is about the repository.

* Purpose
* Technologies
* Maturity of the repository
* How to contribute


2. Recent Activity Highlights

* **Summary of Recent Activity**. For example, the new releases or functionalities implemented.
* **Branch Workflow**: Describe the branch workflow used in the repository (Git Flow, GitHub Flow, GitLabFlow, One Flow...). Include information about the main branch, development branches, feature branches, and any other relevant branches.
* **Commit history snapshot**. provide key insights in how has been maintained well/frequently. If follows the best practices.


The horizon of the report is 6 months, so you have to provide the information of the last {TIME_HORIZON_MONTHS} months. The report should be structured and easy to read. Use markdown format to generate the report. The report should be in English. You can use the tools provided to you to explore the repository and generate the report.

To generate the report you can follow an incremental approach, gathering information from the repository and then generating the report.
"""


GIT_REPORT_MODEL = os.getenv("GIT_REPORT_MODEL", "gpt-4.1")


agent_git_report = Agent[GitRepository](name="GitReport",
                     model=GIT_REPORT_MODEL,
                     instructions=GIT_REPORT_SYSTEM_PROMPT,
                     tools=[
                         agent_repo_setup.as_tool(
                             tool_name="setup_git_repo",
                             tool_description="Setup git repository if a url or local path is provided, use this tool when it is required to explore the repository.",
                         ),
                         agent_git_explorer.as_tool(
                             tool_name="git_explorer",
                             tool_description="Use this is an Agent to request exploratory tasks in the repository recursively. The task description is what information is expected to obtain, not how to obtain it, needs to be concise, not large and atomic in order to not overwhelm the process. Each task per point of the report is a good strategy. The agent will explore the repository and provide the information requested."
                         )
                     ],
                     )
