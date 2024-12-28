# Llama 3.1 Chatbot Interface

The simples chat interface built with Gradio that connects to a local Llama 3.1 CPU-only model through an API.

## Features

- Clean and intuitive chat interface
- Real-time streaming responses
- Text cleaning and formatting
- Easy-to-use clear chat functionality
- Local API integration with Llama 3.1

## Prerequisites

- Python 3.10+
- Local Llama 3.1 model server running on port 11434

## Installation

1. Clone the repository:


```bash
git clone https://github.com/miguel-spn/the-simplest-chatbot.git
cd the-simplest-chatbot
```

2. Install the required packages:

```python
pip install gradio requests
```

## Usage

1. Make sure your Llama 3.1 model server is running on `localhost:11434`

2. Run the chatbot:

```python
python chatbot.py
```

3. Open your browser and navigate to:
   - Local: `http://localhost:7860`
   - Public URL will be provided in the console output

## Configuration

The chatbot is configured to:
- Run on host `0.0.0.0`
- Use port `7860`
- Generate a public share link
- Connect to Llama 3.1 CPU-only model

You can modify these settings in the `demo.launch()` parameters.

## API Integration

The chatbot connects to a local API endpoint:
- URL: `http://localhost:11434/api/generate`
- Model: `steamdj/llama3.1-cpu-only`
- Streaming: Enabled

## License

MIT License
