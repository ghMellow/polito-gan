## Overview

Reinforcement Learning (RL) is a paradigm for teaching an **Agent** to operate within an **Environment** to maximize a cumulative reward signal. Unlike supervised learning, RL learns through interaction and feedback (trial-and-error).

### Core Components and Goal
The objective is to find an optimal **Policy ($\pi^*$)**, which defines the best behavior for the agent. This is fundamentally driven by the **Value Function ($V$ or $Q$)**, which estimates the expected total future reward achievable from a given state or state-action pair.

### Learning Methodologies
RL generally falls into two approaches:

1.  **Value-Based Approaches (e.g., Q-Learning)**: The agent estimates the optimal $Q(s, a)$ value function using the Bellman equation. The policy is implicitly derived by always choosing the action $a$ that maximizes $Q(s, a)$. This is stable and foundational.
2.  **Policy-Based Approaches (e.g., Actor-Critic)**: These methods directly learn the policy $\pi$ (the action mapping). The **Actor** component acts as the policy, while the **Critic** component evaluates the quality of the action taken by predicting the value function, reducing variance and improving stability over pure policy gradients.

### Modern Advancements
*   **Deep RL**: Utilizing deep neural networks to handle complex, high-dimensional state inputs (like raw camera feeds), making RL feasible for real-world robotics and games.
*   **Model-Free Learning**: Most modern agents are model-free, meaning they learn optimal behavior without needing explicit knowledge of the environment's transition dynamics.

*RL is crucial for decision-making problems where the outcome depends on a long sequence of actions and long-term planning is required.*