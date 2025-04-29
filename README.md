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


4. Add the environment variable OPENAI_API_KEY.

5. Execute the following command to run the app:

```bash
uv run ./src/main.py
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key. This is required for the application to function properly.
- `GITHUB_TOKEN`: Your GitHub token. This is required for the application to function properly.

### Some other default environment variables

- `__SOME_AGENT_NAME__MODEL`: For each agent, you can set the model to be used each one, could use a different model. The current agents are:

1. GitAssistant. The env variable is `GIT_ASSISTANT_MODEL`, where the default is `gpt-4o-mini`.
2. GitCommands. The env variable is `GIT_COMMANDS_MODEL`, where the default is `gpt-4.1-mini`.
3. GitReport. The env variable is `GIT_REPORT_MODEL`, where the default is `gpt-4.1-mini`.
4. GitSetup. The env variable is `GIT_SETUP_MODEL`, where the default is `gpt-4.1-mini`.