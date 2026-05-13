## Bayesian Deep Learning
This model incorporates uncertainty quantification into its predictions by treating model weights not as fixed values ($\theta$) but as probability distributions ($p(\theta|D)$). This allows the system to output not just a single prediction, but a probability *range* (or credible interval), which is vital for mission-critical systems.

### The Problem of Uncertainty
In traditional deep learning, a model predicts $\mathbf{y} = f(\mathbf{x}; \theta_{\text{best}})$. This output is a single point estimate. If the model encounters data outside its training distribution (out-of-distribution data), its prediction $\mathbf{y}$ may be highly confident but fundamentally wrong. Bayesian methods quantify this uncertainty.

### Core Methodology: Bayes' Theorem and Inference
The goal is to solve Bayes' Theorem for the weights $\theta$:
$$ p(\theta|D) = \frac{p(D|\theta) p(\theta)}{p(D)} $$

Practical methods use approximations because calculating the true posterior $p(\theta|D)$ is impossible:
1.  **Variational Inference (VI) / MCMC**: These techniques map the true complex posterior into a mathematically simple, tractable distribution $q(\theta)$, making optimization feasible.
2.  **Monte Carlo Dropout (MC Dropout)**: A computationally efficient proxy. By literally running the model multiple times while keeping dropout active during inference, we generate an ensemble of predictions. The variance across this ensemble serves as a practical proxy for the epistemic uncertainty.

*Key Takeaway: BDL changes the output from a single number to a probability distribution, providing a measure of confidence alongside the prediction.*