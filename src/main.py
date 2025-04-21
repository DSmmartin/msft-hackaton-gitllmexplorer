from agents import Runner
from git_agents.agent_git_assistant import GitAssistant

EXAMPLE_QUESTIONS = [
    "What is Git?",
    "Could you clone this repository? -> https://github.com/huggingface/smolagents.git",
]


def main():

    for question in EXAMPLE_QUESTIONS:
        result = Runner.run_sync(GitAssistant, question)
        print("\n" + "=" * 50)
        print(f"QUESTION: {question}")
        print("-" * 50)
        print(f"ANSWER:\n{result.final_output}")
        print("=" * 50)


if __name__ == "__main__":
    main()
