from env.UpdatedEnv import PuzzlePieceEnv

PUZZLE_SIZES = [9, 16, 25]

for size in PUZZLE_SIZES:

    print("\n" + "=" * 60)
    print(f"STARTING DEMO FOR PUZZLE SIZE: {size}")
    print("=" * 60)

    env = PuzzlePieceEnv(
        puzzle_size=size,
        render_mode="human"
    )

    obs, info = env.reset()

    for piece in range(size):

        # Select piece
        env.step(piece)

        # Place piece
        obs, reward, terminated, truncated, info = env.step(piece + size)

        env.render()

        if terminated:
            print(f"Puzzle size {size} solved.")
            break


PUZZLE_SIZES = [9, 16, 25]

for size in PUZZLE_SIZES:

    print("\n" + "=" * 60)
    print(f"STARTING DEMO FOR PUZZLE SIZE: {size}")
    print("=" * 60)

    env = PuzzlePieceEnv(
        puzzle_size=size,
        render_mode="human"
    )

    obs, info = env.reset()

    for piece in range(size):

        # Select piece
        env.step(piece)

        # Place piece
        obs, reward, terminated, truncated, info = env.step(piece + size)

        env.render()

        if terminated:
            print(f"Puzzle size {size} solved.")
            break