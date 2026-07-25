# Phase 2 — Pre-trained Models: Notes

## Pre-trained Models
- Already trained on massive datasets and used through APIs or local inference
- Benefits: faster development, lower cost, high-quality performance
- Limitations: limited customization, provider dependence, knowledge cutoff

## Popular Models
- **GPT-4o / GPT-4 Turbo (OpenAI):** 128K context, strong general-purpose model
- **Claude (Anthropic):** 200K context, excellent for reasoning and long documents
- **Gemini (Google):** 1M+ context, built for multimodal tasks (text, images, audio, and more)
- **Llama (Meta):** open-source, can be self-hosted and run locally

## Context Length & Knowledge Cutoff
- **Context length:** the maximum amount of text a model can process in a single request
- **Knowledge cutoff:** the model does not know information added after its training cutoff date, so external data (such as RAG) is needed for up-to-date answers

## Practical: Local Inference
- Ran a local model (llama3.2) using Ollama with no API cost
- Character-based token estimates are only approximations and can differ from the model's actual tokenizer count (for example, Ollama's `eval_count`)