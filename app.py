from fastapi import FastAPI
from environment import EmailEnv

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    env = EmailEnv()
    state = env.reset()

    return {
        "observation": state,
        "reward": 0.0,
        "done": False,
        "info": {}
    }


@app.post("/step")
def step(action: dict):
    env = EmailEnv()

    act = action.get("action", "no_email")

    state, reward, done, info = env.step(act)

    return {
        "observation": state,
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }

@app.get("/state")
def get_state():
    env = EmailEnv()
    return {"state": env.state()}