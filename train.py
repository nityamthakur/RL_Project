from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

from env.UpdatedEnv import PuzzlePieceEnv

# =========================
# CONFIG
# =========================

PUZZLE_SIZE = 9
TIMESTEPS = 100000

MODEL_NAME = f"./models/ppo_puzzle_agent_{PUZZLE_SIZE}"

# =========================
# CREATE ENVIRONMENT
# =========================

env = PuzzlePieceEnv(
    puzzle_size=PUZZLE_SIZE
)

env = Monitor(env, "./logs")

# =========================
# CREATE MODEL
# =========================

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=0.0003,
    n_steps=2048,
    batch_size=64,
    gamma=0.99,
)

# =========================
# TRAIN
# =========================

model.learn(total_timesteps=TIMESTEPS)

# =========================
# SAVE MODEL
# =========================

model.save(MODEL_NAME)

print(f"Training complete for puzzle size {PUZZLE_SIZE}")