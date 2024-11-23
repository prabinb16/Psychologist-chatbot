# Llama 3.2 Chatbot

A simple chatbot interface using Llama 3.2 model through Ollama.

## Prerequisites

1. Install Ollama from [https://ollama.ai/](https://ollama.ai/)
2. Pull the Llama 3.2 model:
```bash
ollama pull llama3.2
```
3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Chatbot

1. Make sure Ollama is running
2. Start the chatbot interface:
```bash
streamlit run app.py
```
3. Open your browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Features

- Clean, modern chat interface
- Real-time responses from Llama 3.2
- Chat history preservation during session
- Error handling for API communication
- Responsive design that works on both desktop and mobile

## Troubleshooting

- If you get connection errors, make sure Ollama is running
- If the model isn't responding, verify that you've successfully pulled the Llama 3.2 model
- For other issues, check the error messages in the Streamlit interface
