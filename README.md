# msft-hackaton-gitllmexplorer
Project for the AI Agents Microsoft Hackaton

Goal: Create a CLI Tool that allows users to understand Git Repositories using LLM's Agents.

## Contribute

### Setting up the environment with `uv`

[`uv`](https://github.com/astral-sh/uv) is a fast Python package installer and resolver that we use for dependency management.

#### Installing `uv`

1. Install `uv` using the official installer:

```bash
curl -sSf https://install.python-uv.org | sh
```

For Mac users follow instructions here:
https://docs.astral.sh/uv/getting-started/installation/

2. Verify the installation:

```bash
uv --version
```

#### Creating and activating the environment

1. Clone the repository:

```bash
git clone https://github.com/DSmmartin/msft-hackaton-gitllmexplorer.git
cd msft-hackaton-gitllmexplorer
```

2. Create a virtual environment:

```bash
uv sync && uv venv
```

3. Activate the virtual environment:

- On Linux/macOS:
```bash
source .venv/bin/activate
```


4. Prepare the environment variables with third parties
- `OPENAI_API_KEY`: Your OpenAI API key. This is required for the application to function properly.
- `GITHUB_TOKEN`: Your GitHub token. This is required for the application to function properly.

5. Prepare the environment variables for the agents
Each agent can be configured with a different model. The agent variables follow the format:
- `__AGENT_NAME__MODEL`: 'default_model'
These are the environmental variables for the implemented agents:
- `GIT_ASSISTANT_MODEL`: `gpt-4o-mini`.
- `GIT_COMMANDS_MODEL`: `gpt-4.1-mini`.
- `GIT_REPORT_MODEL`: `gpt-4.1-mini`.
- `GIT_SETUP_MODEL`: `gpt-4.1-mini`.

6. Execute the following command to run the app:

```bash
uv run ./src/main.py
```

## Some requests that you can try with the Assistant Agent:

- "Give me more information about this repository https://github.com/valory-xyz/quickstart"
- "Make a clone of this repository and initialize it https://github.com/modelcontextprotocol/servers"
- "Find me the best repositories about transformers"

## Future steps and potential new features

- Improving the Git Exploratory analisis tool which more detailed information such as:
    1. How many active branches?
    2. What is the branch strategy?
    3. What is the Git Flow?
- Packaging the tool in a cli library
- Building a TUI for the tool (the Textual library)
- Integrating some Git commands with the [Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git)
- Adding unit tests for core functionalities
- Building a RAG with the book "PRO GIT" by Scott Chacon and Ben Straub
