# Email Trigger RL Environment

## Problem Statement
Design an intelligent system that decides when and what type of email to send to users to maximize engagement while avoiding spam.

## Real-World Use Case
Used in marketing automation platforms to optimize email campaigns and improve user engagement.

## State Space
- user_type: new / regular / inactive
- last_email_days: days since last email
- engagement_score: user engagement probability
- preferred_time: morning / evening

## Action Space
- send_promo
- send_reminder
- send_personalized
- no_email

## Reward Logic
- High reward for correct targeting (e.g., personalized emails to regular users)
- Penalty for spamming users
- Bonus for sending emails at preferred times
- Rewards scaled between 0 and 1

## Tasks
- Easy: Basic correct email targeting
- Medium: Optimize engagement
- Hard: Avoid spam + personalization + timing optimization

## How to Run
```bash
python inference.py