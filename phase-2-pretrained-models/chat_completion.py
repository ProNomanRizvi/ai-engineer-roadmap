"""
Phase 2 - Pre-trained Models
Task: Chat Completion using local Ollama API (llama3.2)
This script sends a prompt to a locally running LLM and prints
the response along with a basic token count.
"""

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2"


def chat_completion(prompt: str) -> dict:
    """
    Sends a single user prompt to the local Ollama model
    and returns the parsed JSON response.
    """
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()


def estimate_token_count(text: str) -> int:
    """
    Rough token estimate (Ollama's /api/chat doesn't always return
    token counts the same way OpenAI does, so we estimate here:
    ~4 characters per token is a common approximation).
    """
    return max(1, len(text) // 4)


def main():
    prompt = "Explain what an AI Engineer does in one short paragraph."

    print(f"Sending prompt to {MODEL_NAME}...\n")
    result = chat_completion(prompt)

    reply_text = result["message"]["content"]

    print("=== Model Response ===")
    print(reply_text)

    print("\n=== Token Info ===")
    print(f"Prompt tokens (estimated): {estimate_token_count(prompt)}")
    print(f"Response tokens (estimated): {estimate_token_count(reply_text)}")

    # Ollama also returns actual eval counts if available
    if "eval_count" in result:
        print(f"Response tokens (from Ollama, actual): {result['eval_count']}")
    if "prompt_eval_count" in result:
        print(f"Prompt tokens (from Ollama, actual): {result['prompt_eval_count']}")


if __name__ == "__main__":
    main()