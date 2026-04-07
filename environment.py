import random

class EmailEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.state_data = {
            "user_type": random.choice(["new", "regular", "inactive"]),
            "last_email_days": random.randint(0, 7),
            "engagement_score": round(random.uniform(0.2, 0.9), 2),
            "preferred_time": random.choice(["morning", "evening"])
        }
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        reward = 0

        user = self.state_data["user_type"]
        days = self.state_data["last_email_days"]

        # 🎯 Smart reward logic
        if action == "send_personalized":
            reward = 0.9 if user == "regular" else 0.4

        elif action == "send_promo":
            reward = 0.8 if user == "new" else 0.3

        elif action == "send_reminder":
            reward = 0.6 if user != "inactive" else 0.2

        elif action == "no_email":
            reward = 0.7 if user == "inactive" else 0.2

       
        if days < 2:
            reward -= 0.5


        if action == "send_personalized" and self.state_data["preferred_time"] == "evening":
            reward += 0.1


        self.state_data["last_email_days"] += 1

        return self.state(), max(0, min(1, reward))