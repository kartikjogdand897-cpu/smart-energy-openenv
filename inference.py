import os
import json
from openai import OpenAI
from env import SmartEnergyEnv

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN")
)

MODEL_NAME = os.getenv("MODEL_NAME")

env = SmartEnergyEnv("medium")

state = env.reset()

done = False

print("Starting inference...")

while not done:

    prompt = f"""
    You are an AI managing energy allocation.

    Current state:
    demand = {state['energy_demand']}
    solar available = {state['solar_available']}
    battery level = {state['battery_level']}

    Respond ONLY in JSON format:

    {{
        "solar": number,
        "battery": number,
        "grid": number
    }}
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content

    try:
        action = json.loads(output)
    except:
        action = {
            "solar": 20,
            "battery": 10,
            "grid": 20
        }

    state, reward, done, _ = env.step(action)

    print("STATE:", state)
    print("REWARD:", reward)

print("Completed successfully")
