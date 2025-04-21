from agents import Agent, Runner


def main():
    agent = Agent(name="GitAssistant", instructions="You are a helpful assistant that answers questions about Git Tool.")

    result = Runner.run_sync(agent, "What is GIT?")
    print(result.final_output)


if __name__ == "__main__":
    main()
