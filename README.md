# Email Trigger RL Environment

##  Problem Statement
Design an intelligent system that decides **when and what type of email to send** to users in order to **maximize engagement while avoiding spam**.

---

##  Real-World Use Case
This environment simulates real-world **marketing automation systems** used by companies to:
- Improve email open rates  
- Reduce user fatigue  
- Optimize campaign performance  

---

##  Environment Overview
This is a Reinforcement Learning environment where an agent learns to:
- Understand user behavior  
- Choose the right type of email  
- Decide optimal timing  

---

##  State Space
The agent observes:

- **user_type**: new / regular / inactive  
- **last_email_days**: days since last email  
- **engagement_score**: probability of user interaction  
- **preferred_time**: morning / evening  

---

##  Action Space
The agent can take one of the following actions:

- `send_promo`  
- `send_reminder`  
- `send_personalized`  
- `no_email`  

---

##  Reward Logic
- High reward for correct targeting (e.g., personalized emails to regular users)  
- Penalty for sending too many emails (spam behavior)  
- Bonus for sending emails at preferred user time  
- Rewards are normalized between **0.0 and 1.0**

 **Key Insight:**  
This environment models real-world **email fatigue and engagement trade-offs**, balancing personalization, timing, and spam avoidance.

---

##  Tasks

###  Easy
- Send relevant emails to active users  

###  Medium
- Maximize engagement using appropriate email types  

###  Hard
- Balance **personalization + timing + spam avoidance**  

---

##  Baseline Agent Behavior
The baseline agent uses **probabilistic decision-making** based on user state:
- Prioritizes personalization for regular users  
- Uses promotions for new users  
- Avoids spamming inactive users  

---

##  How to Run

```bash
python inference.py