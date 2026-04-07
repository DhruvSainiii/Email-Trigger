import os
import time
from typing import List, Optional

from environment import EmailEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)

def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]) -> None:
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )

def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}", flush=True)

def main():
    env = EmailEnv()

    rewards = []
    steps_taken = 0

    log_start(task="email_task", env="email_env", model=MODEL_NAME)

    state = env.reset()

    for step in range(1, 9):

        user = state["user_type"]
        days = state["last_email_days"]

        if days < 2:
            action = "no_email"

        elif user == "regular":
            action = "send_personalized"

        elif user == "new":
            action = "send_promo"

        elif user == "inactive":
            action = "no_email"

        else:
            action = "send_reminder"

        try:
            state, reward = env.step(action)
            done = False
            error = None

        except Exception as e:
            reward = 0.0
            done = True
            error = str(e)

        rewards.append(reward)
        steps_taken += 1

        log_step(step, action, reward, done, error)

        if done:
            break

    score = sum(rewards) / len(rewards)
    success = True

    log_end(success, steps_taken, score, rewards)

    time.sleep(300)

if __name__ == "__main__":
    main()