# Agentic-AI-Starter

## 🧠 LangChain Agent: Capital & Weather Finder 🌍☁️

This is a simple AI Agent built using **LangChain** and **OpenAI** that takes a natural language query like:

> *"What is the capital of France, and what's the weather like there?"*

It automatically breaks the query into subtasks:

1. Finds the capital city of the specified country.
2. Retrieves the current weather for that capital.

### 🔧 Features

* **Agentic AI**: Uses LangChain's agent framework for reasoning and task execution.
* **Tool-based architecture**: Uses two tools:

  * `CapitalFinder` – Fetches capital using REST Countries API.
  * `WeatherFetcher` – Returns weather (can be extended with OpenWeatherMap).
* **OpenAI-powered reasoning**: Uses an LLM to decide how and when to use tools.
* **Chain-of-thought logic**: Explains its reasoning as it works through the task.

### 🚀 How to Run

1. Install dependencies:

   ```bash
   pip install langchain openai requests
   ```

2. Set your OpenAI API key:

   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

3. Run the agent:

   ```bash
   python main.py
   ```

### 📦 Output

The agent will reason through your query step by step and return a final answer with the capital and weather.

---

### 🤖 Example Output:

```
> What is the capital of France, and what's the weather like there?

Agent action: CapitalFinder
Observation: Paris
Agent action: WeatherFetcher
Observation: The weather in Paris is currently sunny and 25°C.

Final Answer: The capital of France is Paris, and the weather there is currently sunny and 25°C.
```

---

### 🛠 Extend Ideas

* Connect to real weather APIs
* Add memory to track past conversations
* Chain multiple tools together for deeper reasoning


