import gymnasium as gym
from gymnasium import spaces
import numpy as np


class PuzzlePieceEnv(gym.Env):
    """
    Puzzle Paradise-inspired RL environment.

    This simulates VR puzzle testing:
    - selecting puzzle pieces
    - placing them on board slots
    - testing correct/incorrect placement
    - testing Tidy
    - testing Reset
    - tracking completion
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self, puzzle_size=9):
        super().__init__()

        self.puzzle_size = puzzle_size

        # Actions:
        # 0 to puzzle_size-1 = select piece
        # puzzle_size to puzzle_size*2-1 = place selected piece into board slot
        # puzzle_size*2 = tidy
        # puzzle_size*2 + 1 = reset
        self.action_space = spaces.Discrete((puzzle_size * 2) + 2)

        # Observation:
        # board state: which piece is in each slot, -1 means empty
        # piece state: 0 = loose/unplaced, 1 = locked/correctly placed
        # selected piece: -1 if none selected
        low = np.array([-1] * puzzle_size + [0] * puzzle_size + [-1])
        high = np.array([puzzle_size - 1] * puzzle_size + [1] * puzzle_size + [puzzle_size - 1])

        self.observation_space = spaces.Box(
            low=low,
            high=high,
            dtype=np.int32
        )

        self.max_steps = 300
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.board = np.full(self.puzzle_size, -1, dtype=np.int32)
        self.piece_status = np.zeros(self.puzzle_size, dtype=np.int32)

        self.selected_piece = -1
        self.steps = 0

        self.correct_placements = 0
        self.invalid_placements = 0
        self.tidy_uses = 0
        self.reset_uses = 0
        self.select_attempts = 0
        self.place_attempts = 0
        self.repeated_invalid_actions = 0

        self.last_invalid_action = None

        return self._get_obs(), self._get_info()

    def step(self, action):
        reward = -0.05
        terminated = False
        truncated = False

        self.steps += 1

        if 0 <= action < self.puzzle_size:
            reward += self._select_piece(action)

        elif self.puzzle_size <= action < self.puzzle_size * 2:
            slot = action - self.puzzle_size
            reward += self._place_piece(slot)

        elif action == self.puzzle_size * 2:
            reward += self._tidy()

        elif action == self.puzzle_size * 2 + 1:
            reward += self._reset_puzzle()

        if self.correct_placements == self.puzzle_size:
            reward += 25
            terminated = True
        elif self.correct_placements >= 3:
            reward += 2

        elif self.correct_placements >= 6:
            reward += 5

        if self.steps >= self.max_steps:
            truncated = True

        return self._get_obs(), reward, terminated, truncated, self._get_info()

    def _select_piece(self, piece_id):
        self.select_attempts += 1
        
        # Punish repeatedly selecting same piece
        if self.selected_piece == piece_id:
            self.invalid_placements += 1
            return -1
    
        # Cannot select already locked piece
        if self.piece_status[piece_id] == 1:
            self.invalid_placements += 1
            return -2

        self.selected_piece = piece_id
        return 0

    def _place_piece(self, slot):
        self.place_attempts += 1

        if self.selected_piece == -1:
            self.invalid_placements += 1
            return -2

        piece = self.selected_piece

        # Slot already occupied
        if self.board[slot] != -1:
            self.invalid_placements += 1
            self.selected_piece = -1
            return -2

        # Correct placement
        if piece == slot:
            self.board[slot] = piece
            self.piece_status[piece] = 1
            self.correct_placements += 1
            self.selected_piece = -1
            return 10

        # Incorrect placement
        self.board[slot] = piece
        self.invalid_placements += 1
        self.selected_piece = -1
        return -1

    def _tidy(self):
        """
        Simulates the Tidy button:
        removes incorrectly placed loose pieces,
        but keeps locked/correct pieces.
        """
        self.tidy_uses += 1

        cleaned = 0

        for slot in range(self.puzzle_size):
            piece = self.board[slot]

            if piece != -1 and piece != slot:
                self.board[slot] = -1
                cleaned += 1

        if cleaned > 0:
            return 1

        return -0.5

    def _reset_puzzle(self):
        """
        Simulates Reset:
        clears all puzzle progress.
        Useful for testing reset behavior.
        """
        self.reset_uses += 1
        
        penalty = -(self.correct_placements * 5)

        self.board = np.full(self.puzzle_size, -1, dtype=np.int32)
        self.piece_status = np.zeros(self.puzzle_size, dtype=np.int32)
        self.selected_piece = -1
        self.correct_placements = 0

        return penalty

    def _get_obs(self):
        return np.concatenate([
            self.board,
            self.piece_status,
            np.array([self.selected_piece], dtype=np.int32)
        ]).astype(np.int32)

    def _get_info(self):
        completion_percentage = (self.correct_placements / self.puzzle_size) * 100

        return {
            "correct_placements": self.correct_placements,
            "invalid_placements": self.invalid_placements,
            "completion_percentage": completion_percentage,
            "tidy_uses": self.tidy_uses,
            "reset_uses": self.reset_uses,
            "select_attempts": self.select_attempts,
            "place_attempts": self.place_attempts,
            "steps": self.steps,
        }

    def render(self):
        print("\n========== PUZZLE TEST ENV ==========")
        print(f"Board Slots:     {self.board}")
        print(f"Piece Status:    {self.piece_status}")
        print(f"Selected Piece:  {self.selected_piece}")
        print(f"Completed:       {self.correct_placements}/{self.puzzle_size}")
        print(f"Invalid Actions: {self.invalid_placements}")
        print(f"Tidy Uses:       {self.tidy_uses}")
        print(f"Reset Uses:      {self.reset_uses}")
        print("=====================================\n")