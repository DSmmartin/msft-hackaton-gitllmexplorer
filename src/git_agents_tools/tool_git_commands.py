from agents import function_tool
import subprocess
import os



@function_tool
async def git_commands(bash_code_to_execute: str, local_repository_path: str) -> str:
    """Execute Bash Git commands in the context of a local Git repository.

       The Bash CLI has installed Git library, use the git commands to explore the repository.`

    Args:
        bash_code_to_execute: The Bash commands to execute.
        local_repository_path: The local path where is the git repository.

    Returns:
        str: The output of the executed Bash commands.
    """

    try:
        # Change directory to the repository path
        current_dir = os.getcwd()
        os.chdir(local_repository_path)

        # Execute the bash command and capture output
        process = subprocess.run(
            bash_code_to_execute,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )

        # Return to original directory
        os.chdir(current_dir)

        # Return stdout, or stderr if there was an error
        if process.returncode == 0:
            return process.stdout
        else:
            return f"Error (code {process.returncode}): {process.stderr}"

    except Exception as e:
        return f"Exception occurred: {str(e)}"
