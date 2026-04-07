from fastapi import FastAPI
from environment import EmailEnv

app = FastAPI()

env = EmailEnv()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    state = env.reset()
    return {"observation": state, "done": False}

@app.post("/step")
def step(action: dict):
    act = action.get("action")

    state, reward = env.step(act)

    return {
        "observation": state,
        "reward": reward,
        "done": False,
        "info": {}
    }

@app.get("/state")
def get_state():
    return env.state()