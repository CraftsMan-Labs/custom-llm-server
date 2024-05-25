Here is a README file for the GitHub repository [custom-llm-server](https://github.com/magusCoder-official/custom-llm-server).

---

# Custom LLM Server

This project demonstrates how to set up a lightweight server using Flask and Ollama to run large language models (LLMs) like Llama 3 and Phi 3. By leveraging ngrok, you can expose your local server to the internet, making it accessible from anywhere. This setup is ideal for using a spare laptop as a custom server to handle AI tasks globally.

## Features

- **Flask-based server**: Lightweight and easy to set up.
- **Ollama integration**: Supports Llama 3 and Phi 3 models.
- **ngrok tunneling**: Expose your local server to the internet.
- **Asynchronous processing**: Efficient handling of requests.

## Installation

### Prerequisites

- Python 3.7+
- Pip (Python package installer)
- Ollama (Download and install from the [official website](https://ollama.com))

### Step-by-Step Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/magusCoder-official/custom-llm-server.git
   cd custom-llm-server
   ```

2. **Set Up Environment Variables**
   - Create a `.env` file in the root directory of your project with the following content:
     ```plaintext
     NGROK_AUTHTOKEN=your-ngrok-authtoken
     ```
     Get your token from here

     https://dashboard.ngrok.com/tunnels/authtokens
3. **Install Required Models**
   - Open your terminal and run the following commands to install the Llama 3 and Phi 3 models:
     ```bash
     ollama pull llama3
     ollama pull phi3
     ```

4. **Install Dependencies**
   - Create a `requirements.txt` file with the following content:
     ```plaintext
     Flask
     pyngrok
     python-dotenv
     ollama
     asyncio
     ```
   - Install the dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Server**
   - Start the server by running the script:
     ```bash
     python your_script_name.py
     ```
   - If you have set the `NGROK_AUTHTOKEN` in your `.env` file, ngrok will create a public URL for your server.

## Usage

Once the server is running, you can send POST requests to the `/generate` endpoint with a JSON payload containing the model and prompt.

### Example Request
```json
{
  "model": "llama3",
  "prompt": "Why is the sky blue?"
}
```

### Example Response
```json
{
  "response": "The sky is blue because of the way Earth's atmosphere scatters light from the sun."
}
```

## Sample `.env` File
```plaintext
NGROK_AUTHTOKEN=your-ngrok-authtoken
```

## Future Projects

Stay tuned for more projects showcasing the capabilities of this setup. We will explore various custom opensource based swarm ai agents and enhancements to make the most out of your custom AI server which will all run locally on your device.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize and expand this project to suit your needs. Happy coding!

---

This README file provides a comprehensive guide to setting up and using the custom LLM server, ensuring that users can easily follow along and get the server running on their own machines.

Citations:
[1] https://github.com/magusCoder-official/custom-llm-server