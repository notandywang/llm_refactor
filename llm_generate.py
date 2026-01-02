from openai import OpenAI
import pathlib
import time
import config

client = OpenAI()
BASELINE = pathlib.Path("baseline.cpp").read_text()
CACHE = pathlib.Path("cache")
CACHE.mkdir(exist_ok=True)

def generate_code(prompt, iteration):
    out = CACHE / f"gen_{iteration}.cpp"
    if out.exists():
        return out.read_text()

    time.sleep(config.SLEEP_SECONDS)

    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0,
        max_tokens=config.MAX_TOKENS_CODE,
        messages=[
            {"role": "system", "content": "Output ONLY valid C++ code. No explanation."},
            {"role": "user", "content": BASELINE},
            {"role": "user", "content": prompt}
        ]
    )

    code = response.choices[0].message.content
    out.write_text(code)
    return code
