import asyncio
from agents import Runner, Agent, TResponseInputItem, trace
from repository_assets import GitRepositoryLocation
from git_agents.agent_git_assistant import agent_git_assistant
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown


EXAMPLE_QUESTIONS = [
    # "what is your purpose?",
    # "Could you provide a summary about this repo based on the README.md?. The URL of the repository is: https://github.com/microsoft/promptflow.git",
    # "What are the current actives branches (understanding active branches as branches that have recent activity) in the following repository? -> /path/to/local_repo/promptflow.",
    # "What are the last branches (the last 5 ones) that were merged and explain the changes in the following repository? -> /path/to/local_repo/promptflow",
    # "Given the following local repository path: /path/to/local_repo/promptflow, could you tell me if follows a branching workflow strategy (git flow, github flow, gitlab flow, one flow)? based on the banches names and the commit history? provide a complete report of the git flow strategy.",
    # "Could you generate a report of the repository? The URL of the repository is: https://github.com/microsoft/promptflow.git"
]


async def main():
    console = Console()
    current_agent: Agent[GitRepositoryLocation] = agent_git_assistant
    input_items: list[TResponseInputItem] = []
    context = GitRepositoryLocation()

    # Display welcome message
    console.print(Panel.fit("🔍 [bold blue]Git Repository Explorer[/bold blue]", border_style="yellow"))
    console.print("[dim]Enter your questions about Git repositories or type 'exit' to quit[/dim]\n")

    while True:
        user_input = input("💬 ")
        if user_input.lower() == 'exit':
            console.print("[bold green]Exiting the program. Goodbye![/bold green]")
            break

        # Display user question with styling
        console.print(Panel(f"[yellow]{user_input}[/yellow]", title="👤 User Question", border_style="yellow"))

        with trace("Git Assistant"):
            console.print("[dim]Processing your request...[/dim]")
            input_items.append({"content": user_input, "role": "user"})
            result = await Runner.run(current_agent, input_items, context=context)

            input_items = result.to_input_list()
            current_agent = result.last_agent

            # Display agent response with styling and Markdown rendering
            console.print(Panel(
                Markdown(result.final_output) if result.final_output else "[italic]No response received[/italic]",
                title="🤖 Git Assistant",
                border_style="red"
            ))
            console.print("\n")


if __name__ == "__main__":
    asyncio.run(main())