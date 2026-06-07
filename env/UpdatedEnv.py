import gymnasium as gym
from gymnasium import spaces
import numpy as np

class PuzzlePieceEnv(gym.Env):

    metadata = {"render_modes": ["human"]}

    def __init__(self, puzzle_size=9, render_mode=None):
        super().__init__()

        self.puzzle_size = puzzle_size
        self.render_mode = render_mode

        # Actions:
        # 0 to puzzle_size-1 = select piece
        # puzzle_size to puzzle_size*2-1 = place selected piece into board slot
        # puzzle_size*2 = tidy
        # Removed ex
        self.action_space = spaces.Discrete((puzzle_size * 2) + 1)

        # Observation Space Setup
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
        self.piece_status = np.zeros(self.puzzle_size, dtype=np.int32) # 0: Loose/Unplaced, 1: Locked Correctly

        self.selected_piece = -1
        self.steps = 0

        self.correct_placements = 0
        self.invalid_placements = 0
        self.tidy_uses = 0
        self.select_attempts = 0
        self.place_attempts = 0
        
        # Track milestones to prevent reward farming loopholes
        self.milestone_3_reached = False
        self.milestone_6_reached = False

        return self._get_obs(), self._get_info()

    def step(self, action):
        reward = -0.05 
        terminated = False
        truncated = False

        self.steps += 1

        # Action Decoding
        if 0 <= action < self.puzzle_size:
            reward += self._select_piece(action)

        elif self.puzzle_size <= action < self.puzzle_size * 2:
            slot = action - self.puzzle_size
            reward += self._place_piece(slot)

        elif action == self.puzzle_size * 2:
            reward += self._tidy()

        # Dynamic Milestone Reward Allocations (Triggered ONLY once per achievement)
        if self.correct_placements == self.puzzle_size:
            reward += 50
            terminated = True
        elif self.correct_placements >= 6 and not self.milestone_6_reached:
            reward += 5
            self.milestone_6_reached = True
        elif self.correct_placements >= 3 and not self.milestone_3_reached:
            reward += 2
            self.milestone_3_reached = True

        if self.steps >= self.max_steps:
            truncated = True

        if self.render_mode == "human":
            self.render()

        return self._get_obs(), reward, terminated, truncated, self._get_info()

    def _select_piece(self, piece_id):
        self.select_attempts += 1
        
        # Penalty for redundant selection
        if self.selected_piece == piece_id:
            self.invalid_placements += 1
            return -1
    
        # Penalty for selecting an already correctly locked piece
        if self.piece_status[piece_id] == 1:
            self.invalid_placements += 1
            return -2

        self.selected_piece = piece_id
        return 0.1 

    def _place_piece(self, slot):
        self.place_attempts += 1

        if self.selected_piece == -1:
            self.invalid_placements += 1
            return -2

        piece = self.selected_piece

        # Conflict: Slot already occupied
        if self.board[slot] != -1:
            self.invalid_placements += 1
            self.selected_piece = -1
            return -2

        # Evaluation Scenario A: Correct Placement
        if piece == slot:
            self.board[slot] = piece
            self.piece_status[piece] = 1
            self.correct_placements += 1
            self.selected_piece = -1
            return 10

        # Evaluation Scenario B: Incorrect Placement
        self.board[slot] = piece
        self.selected_piece = -1
        return -2 

    def _tidy(self):
        self.tidy_uses += 1
        cleaned = 0

        for slot in range(self.puzzle_size):
            piece = self.board[slot]
            if piece != -1 and piece != slot:
                self.board[slot] = -1
                cleaned += 1

        if cleaned > 0:
            return 1.0 # Reward for successful optimization execution
        #return -0.5 # Penalty for executing Tidy when the board is clean
        return -0.5 - (self.tidy_uses * 0.2)

    def _get_obs(self):
        return np.concatenate([
            self.board,
            self.piece_status,
            np.array([self.selected_piece], dtype=np.int32)
        ]).astype(np.int32)

    def _get_info(self):
        return {
            "correct_placements": self.correct_placements,
            "invalid_placements": self.invalid_placements,
            "completion_percentage": (self.correct_placements / self.puzzle_size) * 100,
            "tidy_uses": self.tidy_uses,
            "steps": self.steps,
        }

    def render(self):
        print("\n========== PUZZLE TEST ENV ==========")
        print(f"Board Slots:     {self.board}")
        print(f"Piece Status:    {self.piece_status}")
        print(f"Selected Piece:  {self.selected_piece}")
        print(f"Completed:       {self.correct_placements}/{self.puzzle_size}")
        print("=====================================\n")
