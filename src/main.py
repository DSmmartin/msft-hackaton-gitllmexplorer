import asyncio
from agents import Runner, Agent, TResponseInputItem, trace
from repository_assets import GitRepositoryLocation
from git_agents.agent_git_assistant import agent_git_assistant


EXAMPLE_QUESTIONS = [
    # "what is your purpose?",
    # "Could you provide a summary about this repo based on the README.md?. The URL of the repository is: https://github.com/microsoft/promptflow.git",
    # "What are the current actives branches (understanding active branches as branches that have recent activity) in the following repository? -> /path/to/local_repo/promptflow.",
    # "What are the last branches (the last 5 ones) that were merged and explain the changes in the following repository? -> /path/to/local_repo/promptflow",
    # "Given the following local repository path: /path/to/local_repo/promptflow, could you tell me if follows a branching workflow strategy (git flow, github flow, gitlab flow, one flow)? based on the banches names and the commit history? provide a complete report of the git flow strategy.",
    # "Could you generate a report of the repository? The URL of the repository is: https://github.com/microsoft/promptflow.git"
]


async def main():
    current_agent: Agent[GitRepositoryLocation] = agent_git_assistant
    input_items: list[TResponseInputItem] = []
    context = GitRepositoryLocation()

    while True:
        user_input = input("Enter your question (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        with trace("Git Assistant"):
            input_items.append({"content": user_input, "role": "user"})
            result = await Runner.run(current_agent, input_items, context=context)

            input_items = result.to_input_list()
            current_agent = result.last_agent
            print("Response:\n", result.final_output)



if __name__ == "__main__":
    asyncio.run(main())