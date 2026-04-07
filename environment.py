import random

class EmailEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.state_data = {
            "user_active": random.choice([True, False]),
            "last_email_days": random.randint(0, 7),
            "engagement_score": random.random()
        }
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        reward = 0

        if action == "send_promo":
            reward = 0.9 if self.state_data["user_active"] else 0.1

        elif action == "send_reminder":
            reward = 0.6

        elif action == "no_email":
            reward = 0.7 if not self.state_data["user_active"] else 0.2

        if self.state_data["last_email_days"] < 2:
            reward -= 0.3  # spam penalty

        self.state_data["last_email_days"] += 1

        return self.state(), max(0, min(1, reward))