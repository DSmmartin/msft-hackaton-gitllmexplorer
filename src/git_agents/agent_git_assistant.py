import os
from agents import Agent
from git_agents.agent_init_setup import GitInitSetup

GIT_ASSISTANT_SYSTEM_PROMPT = """
You are a helpful assistant that answers questions about Git Tool.
"""
GIT_ASSISTANT_MODEL = os.getenv("GIT_ASSISTANT_MODEL", "gpt-4o-mini")


GitAssistant = Agent(name="GitAssistant",
                     model=GIT_ASSISTANT_MODEL,
                     instructions=GIT_ASSISTANT_SYSTEM_PROMPT,
                     handoffs=[GitInitSetup],
                     )
