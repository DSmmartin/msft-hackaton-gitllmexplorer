from agents import function_tool, RunContextWrapper
from repository_assets import GitRepositoryLocation
import os



@function_tool
async def list_directory(
    context: RunContextWrapper[GitRepositoryLocation],
    relative_path: str) -> str:
    """List the contents of the directory in the context of a local Git repository.

       The Bash CLI has installed Git library, use the git commands to explore the repository.

    Args:
        relative_path: The relative path from the root git directory.

    Returns:
        str: The list of files and directories in the specified directory.
    """

    try:
        repository_path = context.context.local_path
        full_path = os.path.join(repository_path, relative_path)
        contents = os.listdir(full_path)
        return "\n".join(contents)

    except FileNotFoundError:
        return "Error: The specified directory does not exist."
    except PermissionError:
        return "Error: Permission denied when accessing the directory."
    except Exception as e:
        return f"Exception occurred: {str(e)}"
