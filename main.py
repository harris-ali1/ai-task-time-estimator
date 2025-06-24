from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def get_estimate(prompt: str, temperature=0.4, max_tokens=300) -> str:
    response = client.chat.completions.create(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content
