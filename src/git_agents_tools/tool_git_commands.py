from agents import function_tool, RunContextWrapper
from repository_assets import GitRepositoryLocation
import subprocess
import os



@function_tool
async def git_commands(
    context: RunContextWrapper[GitRepositoryLocation],
    bash_code_to_execute: str) -> str:
    """Execute Bash Git commands in the context of a local Git repository.

       The Bash CLI has installed Git library, use the git commands to explore the repository.`

    Args:
        bash_code_to_execute: The Bash commands to execute.

    Returns:
        str: The output of the executed Bash commands.
    """

    try:
        current_dir = os.getcwd()
        os.chdir(context.context.local_path)

        process = subprocess.run(
            bash_code_to_execute,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )

        os.chdir(current_dir)

        if process.returncode == 0:
            return process.stdout
        else:
            return f"Error (code {process.returncode}): {process.stderr}"

    except Exception as e:
        return f"Exception occurred: {str(e)}"
