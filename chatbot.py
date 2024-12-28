import gradio as gr
import json
import requests
import re






def clean_response_text(text):
    """
    Cleans the API response text to remove unwanted characters and formatting issues.
    """
    text = text.replace("\n", "<br>")
    text = re.sub(r"[()_]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("*", "").replace("_", "").replace("`", "")
    return text

def generate_response(prompt):
    """
    Generates a response from the API in a streaming manner.
    """
    url = "http://localhost:11434/api/generate"
    
    response = requests.post(url, json={
        "model": "steamdj/llama3.1-cpu-only",
        "prompt": prompt,
        "stream": True
    }, stream=True)

    partial_response = ""
    for line in response.iter_lines():
        if line:
            json_response = json.loads(line)
            if "response" in json_response:
                partial_response += json_response["response"]
                partial_response_cleaned = clean_response_text(partial_response)
                yield partial_response_cleaned

def chat_response(message, history):
    """
    Handles the chat input and updates the chat history with cleaned responses.
    """
    history.append((message, ""))

    for partial_response in generate_response(message):
        history[-1] = (message, partial_response)
        yield history

# Basic Gradio Interface with a ChatComponent
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(label="Llama 3.1 Chatbot")
    msg = gr.Textbox(label="Type your message")
    clear = gr.Button("Clear Chat")
    
    def respond(message, chat_history):
        bot_response = []
        for response in chat_response(message, chat_history):
            bot_response = response
            yield bot_response
    
    msg.submit(respond, [msg, chatbot], chatbot)
    clear.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    demo.queue()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    )
