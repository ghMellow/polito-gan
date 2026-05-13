## Lecture Notes: Reinforcement Learning
---
title: "Reinforcement Learning"
date: "2026-05-12"
topics: [RL]
source_slides: raw/slides-md/08. Reinforcement learning.md
source_transcript: raw/lesson-transcripts/06. Reinforcement learning.md
status: draft
---
# Reinforcement Learning (RL)

Reinforcement Learning is a mathematical framework where an **Agent** learns optimal behavior (a **policy**) by interacting with an **Environment** to maximize a cumulative **Reward**.

## Core Concepts and Terminology
*   **Agent**: The learning entity (the algorithm).
*   **Environment**: The world the agent operates in (the simulation).
*   **State ($s$)**: A complete description of the current situation in the environment.
*   **Action ($a$)**: A move or decision the agent makes.
*   **Reward ($r$)**: The immediate numerical feedback signal (+/-) received after taking an action.
*   **Policy ($\pi$)**: The agent's strategy; a function mapping states to actions ($\pi: s \rightarrow a$).
*   **Value Function ($V$ or $Q$)**: A prediction of the *expected total future reward* starting from a given state or state-action pair.

## The Value Function: The Goal
The fundamental goal of all RL algorithms is to find the **optimal policy ($\pi^*$)**, which maximizes the expected return $G_t$. This is achieved by accurately estimating the optimal value function, $V^*(s)$ or $Q^*(s, a)$.

### 1. Model-Free Learning
Most practical RL agents are *model-free*, meaning they learn the policy and value function through trial and error (experience) without needing to know the environment's exact *transition dynamics* $P(s'|s, a)$.

### 2. Q-Learning (Value-Based)
Q-Learning is a seminal algorithm that learns the **Action-Value Function $Q(s, a)$**. It iteratively updates $Q(s, a)$ using the Bellman optimality equation:
$$ Q(s, a) \leftarrow (1 - \alpha) Q(s, a) + \alpha [\text{Reward} + \gamma \max_{a'} Q(s', a')] $$
The $\max_{a'} Q(s', a')$ component ensures that the agent always assumes the best possible action will be taken next.

## Advanced Policies: Policy Gradients
While Q-learning focuses on value estimation, **Policy Gradient methods** (like REINFORCE and Actor-Critic) directly learn the policy $\pi$ (the mapping from state to action).
*   **Actor-Critic Models**: Combine the best of both worlds. The **Actor** learns the policy (the actions), and the **Critic** learns the value function (evaluating how good those actions were), stabilizing and improving learning efficiency.

*RL is fundamentally about decision-making under uncertainty, where immediate rewards must be weighed against long-term cumulative goals.*