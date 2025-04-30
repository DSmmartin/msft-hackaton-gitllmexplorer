from agents import function_tool, RunContextWrapper
from repository_assets import GitRepository
import os



@function_tool
async def read_file(
    context: RunContextWrapper[GitRepository],
    file_path: str) -> str:
    """Read the contents of a file in the context of a local Git repository.

       The Bash CLI has installed Git library, use the git commands to explore the repository.

    Args:
        file_path: The path to the file to read, relative to the local repository directory.

    Returns:
        str: The contents of the specified file.
    """

    try:
        full_path = os.path.join(context.context.local_path, file_path)

        if not os.path.isfile(full_path):
            return f"File not found: {full_path}"

        with open(full_path, 'r') as file:
            content = file.read()

        return content
    except Exception as e:
        return f"Exception occurred: {str(e)}"
