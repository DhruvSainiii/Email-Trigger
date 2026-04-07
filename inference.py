from environment import EmailEnv
import time

env = EmailEnv()

print("[START]")

state = env.reset()

for step in range(8):

    user = state["user_type"]
    days = state["last_email_days"]

    # 🧠 Intelligent decision making
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

    state, reward = env.step(action)

    print(f"[STEP] step={step}, action={action}, reward={reward}, state={state}")

print("[END]")

while True:
    time.sleep(60)