# Puzzle Paradise RL Tester

A Reinforcement Learning proof-of-concept for automated game testing in a VR puzzle environment inspired by Meta Horizon Worlds.

This project explores how RL agents can:
- interact with game systems,
- learn gameplay mechanics,
- discover exploits,
- optimize actions,
- and simulate autonomous QA/testing behavior.

The current implementation uses a simplified puzzle-placement environment built with Gymnasium and trained using PPO (Proximal Policy Optimization).

---

# Project Goal

The long-term goal is to investigate AI-driven automated testing for games, especially:
- VR games
- puzzle games
- interaction-heavy experiences
- Meta Horizon Worlds–style gameplay

The current environment serves as a sandbox for experimenting with:
- reward engineering
- emergent AI behavior
- autonomous interaction systems
- gameplay testing agents

---

# Current Features

## Environment Features

- Puzzle board simulation
- Piece selection system
- Piece placement mechanics
- Reset system
- Tidy mechanic
- Progress tracking
- Reward shaping
- Invalid action tracking

---

# Reinforcement Learning Features

- PPO agent using Stable-Baselines3
- Custom Gymnasium environment
- Reward-based learning
- Exploration tuning
- Emergent exploit detection
- Local optimum analysis

---

# Project Structure

```text
project/
│
├── puzzle_env.py          # Custom Gymnasium environment
├── train.py               # PPO training script
├── test_agent.py          # Agent evaluation/testing
├── requirements.txt
└── README.md
```


**Dependencies**

Install Python 3.10+ recommended.

Required Packages

pip install gymnasium
pip install stable-baselines3
pip install numpy
pip install torch


**Environment Overview**

The environment simulates a puzzle board where:

* pieces must be selected,
* placed into correct slots,
* and assembled progressively.

The RL agent interacts using discrete actions.

**Observation Space**

The state includes:

* board slot occupancy
* placed piece status
* selected piece
* completion count
* reset/tidy usage
* invalid action count

**Action Space**

The action space currently includes:

Piece Selection

Select puzzle pieces.

Placement Actions

Place selected piece into board slots.

Utility Actions

* Tidy
* Reset

⸻

**Reward System**

Current reward logic includes:

Action: Reward
Correct placement: Positive
Invalid action: Negative
Reset usage: Strong negative
Puzzle completion: Large positive

Reward scaling is used to encourage long-term progress rather than repetitive farming behavior.

**Current Findings**

The PPO agent successfully learned:

* puzzle interaction mechanics,
* valid placement behavior,
* and reward optimization.

The agent also discovered exploit loops, demonstrating:

* emergent behavior,
* local optimum exploitation,
* and reward hacking.
