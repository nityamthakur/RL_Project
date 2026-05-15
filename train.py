from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from env.puzzle_piece_env import PuzzlePieceEnv


def main():
    env = PuzzlePieceEnv(puzzle_size=9)

    check_env(env, warn=True)

    model = PPO(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=0.0003,
        n_steps=2048,
        batch_size=64,
        gamma=0.99
    )

    model.learn(total_timesteps=300_000)

    model.save("puzzle_paradise_testing_agent")

    print("Training complete. Model saved.")


if __name__ == "__main__":
    main()