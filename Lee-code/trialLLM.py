# from ollama import chat
# stream = chat(
#     model="llama3.2",
#     messages=[{"role": "user", "content": "为什么天空是蓝色的？"}],
#     stream=True
# )
# for chunk in stream:
#     print(chunk["message"]["content"], end="", flush=True)

import requests

url = "http://localhost:11434/api/generate"
data = {"model": "llama3.2:latest", "prompt": "Solve 23*57 step by step"}

with requests.post(url, json=data, stream=True) as r:
    for line in r.iter_lines():
        if line:
            part = line.decode('utf-8')
            # Example: apply math or filtering logic here
            print("Chunk:", part)
