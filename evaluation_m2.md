# 🧾 Evaluation – Milestone 2 (Translation)

**Evaluation week:** 4

## Criteria and status

| Criterion | Target | Status |
|---|---|---|
| Azure OpenAI translation integrated | Working API call | ✅ Done (`translatemodel.py`) |
| Multiple target languages | 12+ languages | 🔄 Any language the GPT model supports; a tested list is still to be recorded |
| Translation latency | < 2 s per request | 🔄 Printed per request in the pipeline; no formal benchmark yet |
| Translation accuracy | BLEU ≥ 0.8 | ⏳ Not yet measured |

## Sample result
```
Input  : "Welcome to the live cricket match!"
Output : "¡Bienvenidos al partido de cricket en vivo!"   (Spanish)
```

## Deliverables
1. Translation script: `src/translatemodel.py`
2. Dependencies: `src/requirements.txt`

## Next step
Test 12 languages on a small set of sentences, record latency and, if reference translations are available, compute BLEU.
