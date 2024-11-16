import requests

API_URL = "https://api-inference.huggingface.co/models/saul-ai/SaulLM-7B"
headers = {"Authorization": f"Bearer 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"}

def query(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    return response.json()

# Example usage
legal_text = "Your complex legal text goes here."
simplified_text = query(legal_text)
print(simplified_text)
