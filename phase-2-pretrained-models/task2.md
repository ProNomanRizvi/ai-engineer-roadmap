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

### Claude vs Gemini

**Claude** is a better choice when working with very long documents because it has a large context window. It can understand long reports, manuals, or multiple files while keeping the conversation consistent.

**Gemini** is a better choice when a project needs to work with different types of data, such as text, images, audio, and video. It is designed for strong multimodal capabilities and also supports a very large context window.

**Scenario Example:**

If I build a company knowledge assistant that needs to read hundreds of pages of policies and answer employee questions, I would choose **Claude** because it handles long documents very well.

If I build a learning app where users upload images, ask questions about diagrams, and interact with videos and text in one place, I would choose **Gemini** because it is designed for multimodal tasks and can process different types of information together.