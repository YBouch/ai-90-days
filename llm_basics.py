import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

project_description = """
A company plans to build a new asphalt mixing plant
in Baden-Württemberg with a production capacity of 240 t/h.
"""

response = client.responses.create(
    model="gpt-6-luna",
    input=f"""
Extract the following project information.

Return ONLY valid JSON, no markdown, no explanation, with exactly these fields:

plant_type (string)
location (string)
capacity (number)
unit (string)
new_installation (boolean)

Project description:
{project_description}
"""
)

raw = response.output_text.strip()
raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

data = json.loads(raw)

print(data)
print(f"Capacity: {data['capacity']} {data['unit']}")