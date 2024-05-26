from litellm import completion

response = completion(
    model="ollama_chat/phi3", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
)
print(response.json())