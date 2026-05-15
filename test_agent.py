import time
from stable_baselines3 import PPO

from env.puzzle_piece_env import PuzzlePieceEnv


def main():
    env = PuzzlePieceEnv(puzzle_size=9)
    model = PPO.load("puzzle_paradise_testing_agent")

    obs, info = env.reset()

    for step in range(100):
        action, _ = model.predict(obs, deterministic=True)

        obs, reward, terminated, truncated, info = env.step(action)

        print(f"Step: {step}")
        print(f"Action Taken: {action}")
        print(f"Reward: {reward}")
        print(f"Info: {info}")

        env.render()

        time.sleep(0.3)

        if terminated:
            print("Puzzle completed successfully.")
            break

        if truncated:
            print("Episode ended due to max steps.")
            break


if __name__ == "__main__":
    main()