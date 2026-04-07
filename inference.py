from environment import EmailEnv

env = EmailEnv()

print("[START]")

state = env.reset()

for step in range(5):
    if state["user_active"]:
        action = "send_promo"
    else:
        action = "no_email"

    state, reward = env.step(action)

    print(f"[STEP] Action={action}, Reward={reward}")

print("[END]")