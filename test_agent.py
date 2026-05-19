import time

from stable_baselines3 import PPO
from env.UpdatedEnv import PuzzlePieceEnv

# =========================
# CONFIG
# =========================

PUZZLE_SIZE = 9

MODEL_PATH = f"./models/ppo_puzzle_agent_{PUZZLE_SIZE}"

# =========================
# CREATE ENV
# =========================

env = PuzzlePieceEnv(
    puzzle_size=PUZZLE_SIZE,
    render_mode="human"
)

# =========================
# LOAD MODEL
# =========================

model = PPO.load(MODEL_PATH)

# =========================
# RESET ENV
# =========================

obs, info = env.reset()

# =========================
# RUN AGENT
# =========================

for step in range(500):

    action, _ = model.predict(obs, deterministic=True)

    obs, reward, terminated, truncated, info = env.step(action)

    print(f"\nStep: {step}")
    print(f"Action Taken: {action}")
    print(f"Reward: {reward}")
    print(f"Info: {info}")

    env.render()

    time.sleep(0.2)

    if terminated:
        print("\nPuzzle completed successfully.")
        break

    if truncated:
        print("\nEpisode ended due to max steps.")
        break