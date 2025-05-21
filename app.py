import subprocess
import time
import random
from datetime import datetime

# List of random commit messages
messages = [
    "Update code", "Fix bug", "Minor changes", "Refactor script", "Improve logic",
    "Optimize function", "Enhance performance", "Patch update", "Typo fix", "Stable release"
]

MIN_COUNT=0
MAX_COUNT=20

# ✅ Add a parameter here
def run_git_command(cmd):
    try:
        result=subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip(), "Success"
    except subprocess.CalledProcessError as e:
        return e.stderr.strip(), "Failed"

while MIN_COUNT<=MAX_COUNT:
    MIN_COUNT+=1
    message=random.choice(messages)
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    out_add, status_add=run_git_command(["git", "add", "."])
    out_commit, status_commit=run_git_command(["git", "commit", "-m", message])
    out_push, status_push=run_git_command(["git", "push"])

    with open("log.txt", "a") as log:
        log.write(f"Time: {timestamp}\n")
        log.write(f"Commit Message: {message}\n")
        log.write(f"Add Status: {status_add}, Commit Status: {status_commit}, Push Status: {status_push}\n")
        log.write("-" * 50 + "\n")

    time.sleep(30)  # 5 minutes
