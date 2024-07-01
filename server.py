import os
from flask import Flask, request, jsonify, Response, stream_with_context
from pyngrok import ngrok
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

async def query_litellm(model, prompt, 
                        stream=False, 
                        system_prompt = '', 
                        max_tokens = 1024, 
                        format_json = False,
                        temperature = 0.5,
                        top_p = 1.0,
                        ):
    response = completion(
        model="ollama/"+model,
        messages=[
            {
                "content": system_prompt,
                "role": "system"
            },
            { 
                "content": prompt, 
                "role": "user"
             }],
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
    )
    return response

def lite_llm_server():
    app = Flask(__name__)

    @app.route('/generate', methods=['POST'])
    async def generate():
        data = request.json
        model = data.get('model', 'phi3')
        prompt = data.get('prompt', '')
        system_prompt = data.get('system_prompt', '')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        try:
            response = await query_litellm(model, prompt, system_prompt)
            return jsonify(response.json())
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app

if __name__ == "__main__":
    app = lite_llm_server()

    ngrok_authtoken = os.getenv("NGROK_AUTHTOKEN")
    
    if ngrok_authtoken:
        ngrok.set_auth_token(ngrok_authtoken)
        public_url = ngrok.connect(8000)
        print(f" * ngrok tunnel available at {public_url}")
    else:
        print(" * No ngrok authtoken found. Please set it in the .env file.")
    
    app.run(host='0.0.0.0', port=8000)