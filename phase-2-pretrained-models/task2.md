# Task 2

## Benefits of Using Pre-trained Models

### 1. Faster Development

A pre-trained model lets developers build AI features quickly because the model is already trained.

**Example:**  
If I want to add an AI chatbot to a study website, I can use an existing LLM through an API instead of spending months collecting data and training my own model.

### 2. Lower Cost

Training a large AI model requires powerful hardware and a lot of money. Using a pre-trained model is much more affordable for most developers.

**Example:**  
A small startup can use an existing AI model to summarize customer feedback instead of buying expensive GPUs to train its own model.

---

## Limitations of Using Pre-trained Models

### 1. Limited Customization

A pre-trained model may not fully understand the specific needs of a business without extra prompting or additional context.

**Example:**  
A company's internal support assistant may give generic answers unless it is connected to the company's own documents through RAG.

### 2. Dependence on the Provider

If the model provider changes prices, limits API usage, or has downtime, your application is also affected.

**Example:**  
If an AI writing application depends on an external API and that service becomes unavailable, users cannot generate new content until the service is restored.

---

## Two Models and Their Use Cases

### GPT vs Whisper

**GPT** is better for tasks that involve understanding and generating text, such as answering questions, writing emails, summarizing documents, or helping with coding.

**Whisper** is better for speech-to-text tasks because it converts spoken audio into written text accurately.

**Scenario Example:**  
If I want to build an AI study assistant that answers students' questions, I would choose **GPT** because it understands and generates natural language. If I want an app that converts recorded lectures into notes, I would choose **Whisper** because it is designed for speech transcription.