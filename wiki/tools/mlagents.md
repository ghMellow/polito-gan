## ML Agents
This concept represents the deployment and practical usage of AI models (particularly those trained with RL or Deep Learning) within a controlled, interactive environment.

### The Interaction Loop
An ML Agent operates in a continuous loop:
1.  **Observation ($\mathbf{s}$)**: The agent receives a state vector from the Environment (e.g., camera feed, joint angles).
2.  **Action ($\mathbf{a}$)**: The agent's policy translates this observation into a discrete or continuous action.
3.  **Execution & Reward ($r$)**: The Environment simulates the action $\mathbf{a} \rightarrow s'$, and provides a scalar reward $r$ based on performance.

### Key Deployment Techniques
*   **Deep Reinforcement Learning (DRL)**: This is the underlying mathematical tool, allowing the agent to use deep neural networks to process high-dimensional sensory data and map it directly to actions.
*   **Curriculum Learning**: A structural design principle where the complexity of the task is increased gradually. This prevents the agent from being overwhelmed by the largest possible task immediately, stabilizing training.
*   **Imitation Learning**: Rather than starting from pure random exploration, the agent's initial policy is seeded by training it to mimic the behavior of an expert (demonstrations). This drastically accelerates convergence.

*ML Agent systems require robust API integration to manage the state flow between the control loop and the simulated/physical environment.*