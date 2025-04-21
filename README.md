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