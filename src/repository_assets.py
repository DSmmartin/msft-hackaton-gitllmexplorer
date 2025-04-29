from pydantic import BaseModel

class GitRepository(BaseModel):
    """Class to represent the output of the Git repository setup agent."""
    local_path: str | None = None
    git_url: str | None = None
    full_name: str | None = None
    description: str | None = None

class ListOfRepositories(BaseModel):
    """Class to represent the output of the repositories list from search tool."""
    repositories: list[GitRepository] | None = None
