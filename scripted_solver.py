import time

from env.UpdatedEnv import PuzzlePieceEnv

# =========================
# CONFIG
# =========================

PUZZLE_SIZE = 25

# =========================
# CREATE ENV
# =========================

env = PuzzlePieceEnv(
    puzzle_size=PUZZLE_SIZE,
    render_mode="human"
)

obs, info = env.reset()

# =========================
# PERFECT SOLVER
# =========================

for piece in range(PUZZLE_SIZE):

    # Select piece
    select_action = piece

    obs, reward, terminated, truncated, info = env.step(select_action)

    print(f"\nSelected Piece: {piece}")
    print(f"Reward: {reward}")

    env.render()

    time.sleep(0.1)

    # Place piece
    place_action = piece + PUZZLE_SIZE

    obs, reward, terminated, truncated, info = env.step(place_action)

    print(f"\nPlaced Piece: {piece}")
    print(f"Reward: {reward}")

    env.render()

    time.sleep(0.1)

    if terminated:
        print("\nPuzzle solved successfully.")
        break