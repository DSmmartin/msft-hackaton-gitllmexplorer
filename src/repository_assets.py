from pydantic import BaseModel

class GitRepositoryLocation(BaseModel):
    """Class to represent the output of the Git repository setup agent."""
    local_path: str | None = None
    git_url: str | None = None
