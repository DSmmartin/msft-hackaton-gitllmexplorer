import os
from agents import Agent, OpenAIChatCompletionsModel
from model_client import get_model_client

GENERATE_RESPONSE_SYSTEM_PROMPT = """
You are an Agent that your Role is to generate a response for the user based on the information collected.

Guidelines:
- You should not provide any information that is not related to the question.
- Always include where is located the Repository (e.g. local path, remote url).
- You dont need to provide the information the commands that you used to get the information.
- You have to provide the information in a clear and concise manner.
- In your conclussion, you have to provide the confidente level of the information that you provided.

"""
GENERATE_RESPONSE_MODEL = os.getenv("GIT_ASSISTANT_MODEL", "gpt-4.1-mini")


agent_generate_response = Agent(
    name="GenerateResponse",
    model=OpenAIChatCompletionsModel(
        model=GENERATE_RESPONSE_MODEL, openai_client=get_model_client()
    ),
    instructions=GENERATE_RESPONSE_SYSTEM_PROMPT,
)
