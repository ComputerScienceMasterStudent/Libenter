# Libenter
Conversational LLM prompter

A simple Python CLI tool to send prompts to multiple LLM providers (OpenAI, Anthropic) with **language support** for English, Hebrew, Arabic, and Farsi.

---

## Features

* Supports multiple LLM providers via environment variables.
* Run prompts across all configured LLMs.
* Specify response language using a command-line flag:

  * English (`en`) – default
  * Hebrew (`he`)
  * Arabic (`ar`)
  * Farsi (`fa`)
* Easy to extend with new LLMs or languages.

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Install dependencies (if any). Currently, no extra dependencies are required for placeholders. For real API calls, install the provider SDKs:

```bash
pip install openai anthropic
```

---

## Environment Variables

Set your API keys and providers:

```bash
export LLM_PROVIDERS=openai,anthropic
export OPENAI_API_KEY=your_openai_api_key
export ANTHROPIC_API_KEY=your_anthropic_api_key
```

> `LLM_PROVIDERS` must be a comma-separated list of supported providers (`openai`, `anthropic`).

---

## Usage

Run the CLI:

```bash
python app.py --lang en
```

You will be prompted to enter prompts (comma-separated):

```
Enter prompts (comma-separated): Hello, How are you?
```

### Command-line Options

| Flag         | Description       | Choices                | Default |
| ------------ | ----------------- | ---------------------- | ------- |
| `-l, --lang` | Response language | `en`, `he`, `ar`, `fa` | `en`    |

---

## Example

```bash
python app.py --lang he
```

**Input:**

```
Enter prompts (comma-separated): Hello, How are you?
```

**Output:**

```
Prompt: Hello
[OpenAI][he] Response to: ענה בעברית.
Hello
[Anthropic][he] Response to: ענה בעברית.
Hello

Prompt: How are you?
[OpenAI][he] Response to: ענה בעברית.
How are you?
[Anthropic][he] Response to: ענה בעברית.
How are you?
```

> The `[OpenAI][he]` / `[Anthropic][he]` indicates the LLM provider and language.

---

## Adding More Languages

Add your language instruction to `BaseLLM.LANGUAGE_INSTRUCTIONS`:

```python
LANGUAGE_INSTRUCTIONS = {
    "en": "Answer in English.",
    "he": "ענה בעברית.",
    "ar": "أجب باللغة العربية.",
    "fa": "به زبان فارسی پاسخ بده.",
    "es": "Responde en español."  # example new language
}
```

---

## Adding More LLM Providers

1. Subclass `BaseLLM`.
2. Define `ENV_VAR` for the API key.
3. Implement the `generate()` method.
4. Add the class to `LLM_REGISTRY`.

---

## License

GNU License 
