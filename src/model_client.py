import os
from openai import AsyncAzureOpenAI, AsyncOpenAI
from openai import OpenAIError

def get_azure_openai_client() -> AsyncAzureOpenAI:
    return AsyncAzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )

def get_openai_client() -> AsyncOpenAI:
    return AsyncOpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

def get_model_client() -> AsyncOpenAI:
    try:
        azure_client = get_azure_openai_client()
        return azure_client
    except OpenAIError:
        return get_openai_client()
