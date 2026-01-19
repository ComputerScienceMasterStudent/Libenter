# Libenter
Conversational LLM prompter
Used for multi-prompts with LLMs.

An extensible Python example that demonstrates how to:

- Define a common interface for multiple LLM providers
- Load providers dynamically via environment variables
- Run the same prompts against multiple LLMs in one pass

This project uses placeholder responses instead of real API calls, making it safe for local testing and experimentation.

---

## Features

-  Pluggable LLM providers (OpenAI, Anthropic, etc.)
-  Simple factory pattern via a registry
-  Environment-variable based configuration
-  Easy to test and extend
-  Zero external dependencies

---

## Project Structure

```

.
├── main.py        # Entry point
└── README.md

````

---

## Configuration

### Environment Variables

| Variable | Description |
|--------|-------------|
| `LLM_PROVIDERS` | Comma-separated list of LLM providers to load |
| `OPENAI_API_KEY` | API key for OpenAI (required if using `openai`) |
| `ANTHROPIC_API_KEY` | API key for Anthropic (required if using `anthropic`) |

### Example

```bash
export LLM_PROVIDERS=openai,anthropic
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-...
````

---

## Usage

Run the program:

```bash
python main.py
```

You’ll be prompted to enter one or more prompts:

```text
Enter prompts (comma-separated): hello world, explain LLMs
```

Output will look like:

```text
Prompt: hello world
[OpenAI] Response to: hello world
[Anthropic] Response to: hello world
```

---

## Adding a New LLM Provider

1. Create a new subclass of `BaseLLM`
2. Define the required `ENV_VAR`
3. Implement `generate()`
4. Register it in `LLM_REGISTRY`

### Example

```python
class MyCustomLLM(BaseLLM):
    ENV_VAR = "MY_LLM_API_KEY"

    def generate(self, prompt: str) -> str:
        return f"[MyLLM] Response to: {prompt}"
```

```python
LLM_REGISTRY["myllm"] = MyCustomLLM
```

Then enable it:

```bash
export LLM_PROVIDERS=openai,myllm
```

---

## Error Handling

* Missing API keys raise a `ValueError` at startup
* Unknown providers fail fast with a clear error
* Empty prompt input is handled gracefully

---

## License

GNU


```
