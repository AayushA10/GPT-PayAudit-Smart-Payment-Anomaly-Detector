from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

def explain_anomalies(anomalies: list):
    if not anomalies:
        return "No suspicious activity detected."

    prompt = f"""You are an audit assistant. The following are flagged payments:
{anomalies}

Explain what types of anomalies they might represent (e.g. duplicate, vendor fraud, spikes)."""

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content
