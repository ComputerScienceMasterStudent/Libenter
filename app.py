import os

# -------------------------
# LLM client abstractions
# -------------------------

class BaseLLM:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class OpenAILLM(BaseLLM):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Missing OPENAI_API_KEY")

    def generate(self, prompt: str) -> str:
        # Placeholder for real OpenAI call
        return f"[OpenAI] Response to: {prompt}"


class AnthropicLLM(BaseLLM):
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Missing ANTHROPIC_API_KEY")

    def generate(self, prompt: str) -> str:
        # Placeholder for real Anthropic call
        return f"[Anthropic] Response to: {prompt}"


# -------------------------
# LLM factory
# -------------------------

def load_llms():
    providers = os.getenv("LLM_PROVIDERS", "")
    llms = []

    for provider in providers.split(","):
        provider = provider.strip().lower()

        if provider == "openai":
            llms.append(OpenAILLM())
        elif provider == "anthropic":
            llms.append(AnthropicLLM())
        elif provider:
            raise ValueError(f"Unknown LLM provider: {provider}")

    if not llms:
        raise ValueError("No LLM providers configured")

    return llms


# -------------------------
# Main logic
# -------------------------

def main():
    llms = load_llms()

    user_input = input(
        "Enter prompts (comma-separated): "
    )

    prompts = [p.strip() for p in user_input.split(",") if p.strip()]

    if not prompts:
        print("No prompts provided.")
        return

    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        for llm in llms:
            response = llm.generate(prompt)
            print(response)


if __name__ == "__main__":
    main()
