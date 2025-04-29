import tempfile

from agents import function_tool
from agents import RunContextWrapper
from git import Repo

from repository_assets import GitRepository


@function_tool
async def clone_repository(
    context: RunContextWrapper[GitRepository],
    git_url: str) -> str:

    """Clone a Git repository from the given URL. I.e. the git_url is a string that starts with `https://` or `git@` and ends with `.git`.
    This function creates a temporary directory to clone the repository into.

    Args:
        git_url: The URL of the Git repository to clone.

    Returns:
        str: The local path to the cloned repository.
    """
    temp_dir = tempfile.mkdtemp(prefix="git_repo_")
    _ = Repo.clone_from(git_url, temp_dir)
    context.context.local_path = temp_dir
    context.context.git_url = git_url
    return GitRepository(
        local_path=temp_dir,
        git_url=git_url
    )


@function_tool
async def sync_local_repo(
    context: RunContextWrapper[GitRepository],
    local_dir_path: str) -> str:

    """Sync the local repository with the remote. The local_dir_path is a string that is the local path of the repository (doesn't contain `https://` or `git@`).

    Args:
        local_dir_path: The local directory path of the repository to sync.

    Returns:
        str: The local path to the synced repository.
    """

    repo = Repo(local_dir_path)
    origin = repo.remotes.origin
    origin.fetch()
    context.context.local_path = local_dir_path
    context.context.git_url = origin.url
    return GitRepository(
        local_path=local_dir_path,
        git_url=origin.url
    )

