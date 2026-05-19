# RL-Based Automated Puzzle Testing Agent

## Overview

This project is a reinforcement-learning-based gameplay testing proof of concept inspired by automated QA workflows in games.

The goal of this project is NOT to build a perfect puzzle-solving AI.

Instead, the focus is on demonstrating:

- autonomous gameplay interaction
- reinforcement learning integration
- scalable testing environments
- automated traversal validation
- gameplay coverage systems
- reward engineering
- generalized environment design

The project uses:

- Python
- Gymnasium
- Stable-Baselines3 (PPO)
- NumPy

---

# Project Features

## Custom Puzzle Environment

A fully custom Gymnasium environment supporting:

- dynamic puzzle sizes
- scalable action spaces
- scalable observation spaces
- reward-based interaction systems

---

## Reinforcement Learning Agent

Uses PPO (Proximal Policy Optimization) from Stable-Baselines3 to:

- learn puzzle interaction behavior
- optimize placements
- maximize completion rewards

---

## Deterministic Solver

Includes a scripted benchmark solver capable of:

- perfect puzzle completion
- deterministic validation
- scalability demonstrations

---

## Scalable Architecture

The environment supports:

- 9-piece puzzles
- 16-piece puzzles
- 25-piece puzzles
- larger future puzzle configurations

without changing environment architecture.

---

# Technologies Used

- Python 3.10+
- Gymnasium
- Stable-Baselines3
- NumPy
- PPO Reinforcement Learning

---

# Installation

## Clone Repository

text git clone <your-repo-url> cd RL_Puzzle_Testing_Agent 

---

## Create Virtual Environment

### Windows

text python -m venv venv venv\Scripts\activate 

### Mac/Linux

text python3 -m venv venv source venv/bin/activate 

---

## Install Dependencies

text pip install -r requirements.txt 

---

# Project Structure

text RL_Puzzle_Testing_Agent/ │ ├── env/ │   └── UpdatedEnv.py │ ├── models/ │   ├── ppo_puzzle_agent_9.zip │   ├── ppo_puzzle_agent_16.zip │   └── ppo_puzzle_agent_25.zip │ ├── logs/ │ ├── train.py ├── testing_agent.py ├── scripted_solver.py ├── multi_size_demo.py │ ├── requirements.txt ├── README.md └── .gitignore 

---

# Running The Project

# 1. Train RL Agent

text python train.py 

This trains a PPO agent and saves the trained model.

---

# 2. Evaluate RL Agent

text python testing_agent.py 

This loads the trained model and runs autonomous gameplay interactions.

---

# 3. Run Deterministic Solver

text python scripted_solver.py 

This demonstrates guaranteed scalable puzzle completion.

---

# 4. Run Scalability Demo

text python multi_size_demo.py 

This demonstrates multiple puzzle sizes using the same environment.

---

# Environment Architecture

The project revolves around a custom Gymnasium environment:

text PuzzlePieceEnv 

The environment contains:

- piece selection mechanics
- piece placement mechanics
- puzzle validation logic
- reward engineering systems
- milestone progression rewards
- gameplay metrics
- scalable observation spaces

---

# Reward Engineering

The reward system was iteratively refined to avoid exploitative RL behavior.

## Positive Rewards

- correct placement rewards
- milestone progression rewards
- full completion reward

## Negative Rewards

- invalid placement penalties
- redundant selection penalties
- unnecessary tidy penalties
- idle action discouragement

---

# Key Engineering Concepts

This project demonstrates:

- reinforcement learning integration
- reward engineering
- environment simulation
- scalable gameplay systems
- automated interaction testing
- generalized environment architecture
- gameplay metric tracking

---

# Why PPO?

PPO was selected because it is:

- stable
- widely adopted
- efficient for experimentation
- commonly used in RL research

---

# Development Process

## Phase 1 — Initial Goal Definition

The project began as a reinforcement-learning-based gameplay testing proof of concept inspired by Puzzle Paradise.

The objective was NOT to build a superhuman puzzle-solving AI.

Instead, the focus was on:

- autonomous interaction testing
- gameplay traversal validation
- scalable environment simulation
- automated QA-style exploration
- reinforcement learning experimentation

---

## Phase 2 — Environment Architecture

A custom Gymnasium environment (PuzzlePieceEnv) was created.

The environment included:

- dynamic puzzle sizes
- piece selection mechanics
- placement mechanics
- validation logic
- gameplay metrics
- completion tracking

---

## Phase 3 — Initial PPO Training

Initial PPO training was implemented using Stable-Baselines3.

Early training issues included:

- reward farming loops
- repeated reset exploitation
- repetitive action loops
- incomplete puzzle solving

The agent frequently:

- solved only a few puzzle pieces
- exploited reward loopholes
- repeated ineffective actions

---

## Phase 4 — Reward Engineering Iteration

Multiple reward balancing passes were implemented.

Changes included:

- removal of explicit reset actions
- milestone rewards
- stronger penalties for redundant actions
- penalties for invalid placements
- scaling tidy penalties

Milestone rewards were introduced:

- +2 reward for 3 correct placements
- +5 reward for 6 correct placements
- +50 reward for full completion

---

## Phase 5 — Environment Generalization

The environment was redesigned to support scalable puzzle sizes.

Instead of hardcoded logic:

- all actions became dynamically generated
- observation sizes became puzzle-size dependent
- reward logic became generalized

This allowed support for:

- 3x3 puzzles
- 4x4 puzzles
- 5x5 puzzles

without rewriting environment logic.

---

## Phase 6 — Deterministic Benchmark Solver

A scripted solver was added.

Purpose:

- verify environment correctness
- create deterministic demonstrations
- provide guaranteed successful completion
- benchmark RL behavior

This solver:

- programmatically selects correct pieces
- places them into matching slots
- scales automatically to any puzzle size

---

## Phase 7 — Scalability Demonstrations

Multi-size demonstrations were added.

The same environment successfully handled:

- 9-piece puzzles
- 16-piece puzzles
- 25-piece puzzles

without architectural changes.

---

# Important Project Positioning

This project should be viewed as:

## an RL-based automated gameplay testing framework

NOT simply:

## a puzzle-solving AI.

The primary focus is:

- gameplay interaction automation
- scalable testing infrastructure
- reinforcement-learning experimentation

---

# Future Improvements

Potential future implementations include:

- Procedural puzzle generation
- Curriculum learning
- Heatmap visualizations
- Multi-agent systems
- Automated bug classification
- Unity ML-Agents integration
- Unreal Engine integration
- Real gameplay traversal testing

---

# Next Steps

The next development goals are:

1. Improve PPO generalization on larger puzzle sizes
2. Add procedurally generated puzzle layouts
3. Add visualization tools for gameplay coverage
4. Introduce curriculum learning techniques
5. Integrate more realistic gameplay interaction systems
6. Explore real-engine integration with Unity or Unreal

---

# Example Commands

## Train Agent

text python train.py 

## Test PPO Agent

text python testing_agent.py 

## Run Scripted Solver

text python scripted_solver.py 

## Run Multi-Size Demo

text python multi_size_demo.py 

---

# Author

Nityam Thakur

Computer Science: Game Design  
University of California, Santa Cruz
