from openai import OpenAI
import time
import config

client = OpenAI()

def optimize_prompt(old_prompt, metrics, iteration):
    time.sleep(config.SLEEP_SECONDS)

    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0,
        max_tokens=config.MAX_TOKENS_PROMPT,
        messages=[
            {"role": "system", "content": "Rewrite prompts only. One sentence. No code."},
            {"role": "user", "content": f"Prompt: {old_prompt}"},
            {"role": "user", "content": f"Metrics: {metrics}"},
            {"role": "user", "content": "Rewrite the prompt to improve scalability and reduce synchronization."}
        ]
    )

    return response.choices[0].message.content.strip()
