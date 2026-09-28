# 🧩 Milestone 2 – Translation Module

| | |
|---|---|
| **Duration** | Weeks 3–4 |
| **Status** | ✅ Implemented |
| **Code** | `src/translatemodel.py` |

## Objective
Translate recognised text into a target language using **Azure OpenAI** (a GPT chat model, `gpt-4o-mini` by default).

## Approach
The module uses **prompt-based translation**: no model training is involved. A system prompt instructs the model to translate the user's text into the requested language and reply with the translation only. A low temperature (`0.2`) keeps output consistent.

## Tasks
- ✅ Configured the Azure OpenAI client (endpoint, key and deployment name read from environment variables).
- ✅ Implemented `translate_text(text, target_language)` using the chat completions API.
- ✅ Added a command-line demo to translate typed text.
- ✅ Connected the translation step to the speech pipeline (see Milestone 3).

## Tools & Libraries
- `openai` (Azure OpenAI SDK)

## How to run
```bash
python src/translatemodel.py
```
```
Enter text to translate: Welcome to the live cricket match!
Enter target language code (e.g., fr, es, ta): es
Translated Text (es): ¡Bienvenidos al partido de cricket en vivo!
```

## Integration flow
1. Text arrives from speech recognition (Milestone 1) or typed input.
2. `translate_text()` sends it to Azure OpenAI with the translation prompt.
3. The translated text is returned for display or speech output.

## Limitations
- Translation quality is not yet scored with BLEU; latency is only printed per request.
- Language coverage depends on the underlying GPT model.

⬅️ [Milestone 1](milestone.md) · ➡️ [Milestone 3](milestone3.md)
