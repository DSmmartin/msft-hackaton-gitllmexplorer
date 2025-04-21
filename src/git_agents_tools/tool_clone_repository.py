from typing_extensions import Any
import tempfile

from agents import function_tool
from git import Repo


@function_tool
async def clone_repository(git_url: str) -> str:

    """Clone a Git repository from the given URL.

    Args:
        git_url: The URL of the Git repository to clone.

    Returns:
        str: The path to the cloned repository.
    """
    temp_dir = tempfile.mkdtemp(prefix="git_repo_")
    _ = Repo.clone_from(git_url, temp_dir)
    return temp_dir
