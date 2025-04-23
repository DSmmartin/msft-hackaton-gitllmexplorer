from agents import Runner
from git_agents.agent_git_assistant import agent_git_assistant

EXAMPLE_QUESTIONS = [
    "Could you clone this repository? -> https://github.com/huggingface/smolagents.git and list all the branches?",
]


def main():

    for question in EXAMPLE_QUESTIONS:
        result = Runner.run_sync(agent_git_assistant, question)
        print("\n" + "=" * 50)
        print(f"QUESTION: {question}")
        print("-" * 50)
        print(f"ANSWER:\n{result.final_output}")
        print("=" * 50)


if __name__ == "__main__":
    main()
