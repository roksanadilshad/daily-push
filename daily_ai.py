import openai 
import os
import random
from datetime import datetime
import json

# Load your API key from GitHub Secrets (env var)
openai.api_key = os.getenv("OPENAI_API_KEY")

# File types and extensions
file_types = {
    "html": ".html",
    "css": ".css",
    "javascript": ".js"
}

# Prompts per file type
prompts = {
    "html": [
        "Create an HTML page with a motivational quote and styled background.",
        "Make a simple HTML table of your top 5 favorite foods.",
        "Write HTML code for a personal portfolio landing page."
    ],
    "css": [
        "Write CSS code for a neon glowing button.",
        "Create CSS for a smooth gradient background animation.",
        "Write CSS styles for a modern card layout."
    ],
    "javascript": [
        "Write JavaScript code that displays a random fun fact in the console.",
        "Create a JavaScript function that changes background color every 5 second.",
        "Make a JavaScript countdown timer that starts from 10, and when it ends make the background change color."
    ]
}

# File to track used prompts
used_prompts_file = "used_prompts.json"

# Load used prompts or start fresh
if os.path.exists(used_prompts_file):
    with open(used_prompts_file, "r", encoding="utf-8") as f:
        used_prompts = json.load(f)
else:
    used_prompts = {ftype: [] for ftype in file_types.keys()}

def save_used_prompts():
    with open(used_prompts_file, "w", encoding="utf-8") as f:
        json.dump(used_prompts, f, indent=2)

def get_unused_prompt(ftype):
    available = [p for p in prompts[ftype] if p not in used_prompts.get(ftype, [])]
    if not available:
        # Reset if all used
        used_prompts[ftype] = []
        available = prompts[ftype]
    choice = random.choice(available)
    used_prompts[ftype].append(choice)
    save_used_prompts()
    return choice

# Pick a random file type
chosen_type = random.choice(list(file_types.keys()))
extension = file_types[chosen_type]

# Pick a prompt that hasn’t been used recently
prompt = get_unused_prompt(chosen_type)

# Generate AI code
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

code = response.choices[0].message.content

# Filename with date and type
file_name = f"{chosen_type}_file_{datetime.now().strftime('%Y_%m_%d')}{extension}"

# Save generated code to file
with open(file_name, "w", encoding="utf-8") as f:
    f.write(code)

print(f" Generated {file_name} with prompt: {prompt}")

# Update README.md log
readme_file = "README.md"
log_entry = f"- {datetime.now().strftime('%Y-%m-%d')}: Generated `{file_name}` — prompt: *{prompt}*\n"

# Append to README or create if missing
if os.path.exists(readme_file):
    with open(readme_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
else:
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write("# Daily AI Generated Files Log\n\n")
        f.write(log_entry)

print(f" Updated {readme_file}")
