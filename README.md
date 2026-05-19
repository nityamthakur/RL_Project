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

bash git clone <your-repo-url> cd RL_Puzzle_Testing_Agent 

---

## Create Virtual Environment

### Windows

bash python -m venv venv venv\Scripts\activate 

### Mac/Linux

bash python3 -m venv venv source venv/bin/activate 

---

## Install Dependencies

bash pip install -r requirements.txt 

---

# Project Structure

RL_Puzzle_Testing_Agent/
│
├── env/
│   └── UpdatedEnv.py
│
├── models/
│   └── ppo_puzzle_agent_9.zip
│
├── logs/
│
├── train.py
├── testing_agent.py
├── scripted_solver.py
├── multi_size_demo.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

# Running The Project

# 1. Train RL Agent

bash python train.py 

This trains a PPO agent and saves the trained model.

---

# 2. Evaluate RL Agent

bash python testing_agent.py 

This loads the trained model and runs autonomous gameplay interactions.

---

# 3. Run Deterministic Solver

bash python scripted_solver.py 

This demonstrates guaranteed scalable puzzle completion.

---

# 4. Run Scalability Demo

bash python multi_size_demo.py 

This demonstrates multiple puzzle sizes using the same environment.

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

- Procedural puzzle generation
- Curriculum learning
- Heatmap visualizations
- Multi-agent systems
- Automated bug classification
- Unity/Unreal integration
- Real gameplay traversal testing

---

# Author

Nityam Thakur

Computer Science: Game Design  
University of California, Santa Cruz
