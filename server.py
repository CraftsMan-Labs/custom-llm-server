import os
from flask import Flask, request, jsonify, Response, stream_with_context
from pyngrok import ngrok
from dotenv import load_dotenv
import ollama
import asyncio

# Load environment variables from .env file
load_dotenv()

# Ensure the Ollama server is running on localhost
OLLAMA_ENDPOINT = "http://localhost:11434"

# Function to interact with the Ollama model
async def query_ollama(model, prompt, stream=False):
    response = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        stream=stream
    )
    return response

# Set up LiteLLM to handle requests
def lite_llm_server():
    app = Flask(__name__)

    @app.route('/generate', methods=['POST'])
    async def generate():
        data = request.json
        model = data.get('model', 'llama3')
        prompt = data.get('prompt', '')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        try:
            response = await query_ollama(model, prompt)
            return jsonify({'response': response['message']['content']})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app

if __name__ == "__main__":
    # Start the Flask app
    app = lite_llm_server()
    
    # Get the ngrok authtoken from the environment variable
    ngrok_authtoken = os.getenv("NGROK_AUTHTOKEN")
    
    # Set up ngrok tunnel
    if ngrok_authtoken:
        ngrok.set_auth_token(ngrok_authtoken)
        public_url = ngrok.connect(8000)
        print(f" * ngrok tunnel available at {public_url}")
    else:
        print(" * No ngrok authtoken found. Please set it in the .env file.")
    
    app.run(host='0.0.0.0', port=8000)