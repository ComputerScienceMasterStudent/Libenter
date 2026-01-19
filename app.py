import os
from typing import Dict, List, Type


# -------------------------
# LLM base abstraction
# -------------------------

class BaseLLM:
    """Abstract base class for LLM clients."""

    ENV_VAR: str  # must be defined by subclasses

    def __init__(self) -> None:
        api_key = os.getenv(self.ENV_VAR)
        if not api_key:
            raise ValueError(f"Missing {self.ENV_VAR}")
        self.api_key = api_key

    def generate(self, prompt: str) -> str:
        raise NotImplementedError


# -------------------------
# Concrete LLMs
# -------------------------

class OpenAILLM(BaseLLM):
    ENV_VAR = "OPENAI_API_KEY"

    def generate(self, prompt: str) -> str:
        # Placeholder for real OpenAI call
        return f"[OpenAI] Response to: {prompt}"


class AnthropicLLM(BaseLLM):
    ENV_VAR = "ANTHROPIC_API_KEY"

    def generate(self, prompt: str) -> str:
        # Placeholder for real Anthropic call
        return f"[Anthropic] Response to: {prompt}"


# -------------------------
# LLM registry & factory
# -------------------------

LLM_REGISTRY: Dict[str, Type[BaseLLM]] = {
    "openai": OpenAILLM,
    "anthropic": AnthropicLLM,
}


def load_llms() -> List[BaseLLM]:
    providers = os.getenv("LLM_PROVIDERS", "")
    if not providers:
        raise ValueError("No LLM providers configured")

    llms: List[BaseLLM] = []

    for name in map(str.strip, providers.split(",")):
        if not name:
            continue

        try:
            llms.append(LLM_REGISTRY[name.lower()]())
        except KeyError:
            raise ValueError(f"Unknown LLM provider: {name}")

    if not llms:
        raise ValueError("No valid LLM providers configured")

    return llms


# -------------------------
# Main logic
# -------------------------

def main() -> None:
    llms = load_llms()

    user_input = input("Enter prompts (comma-separated): ")
    prompts = [p.strip() for p in user_input.split(",") if p.strip()]

    if not prompts:
        print("No prompts provided.")
        return

    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        for llm in llms:
            print(llm.generate(prompt))


if __name__ == "__main__":
    main()
