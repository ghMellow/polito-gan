## Preliminary Workshop: Bayesian Deep Learning
---
title: "Bayesian Deep Learning"
date: "2026-05-12"
topics: [Bayesian, Uncertainty]
source_slides: raw/slides-md/Bayes_handout.md
source_transcript: N/A (Handout/Reference Material)
status: draft
---

# Bayesian Deep Learning

Bayesian Deep Learning (BDL) is a paradigm shift from traditional deep learning. Instead of learning single point estimates for model weights ($\theta$), BDL treats these weights as probability distributions $p(\theta|D)$, incorporating **model uncertainty** into the predictions.

## Why Bayesian? The Uncertainty Problem
Standard deep learning models, when trained on finite data, only provide a point estimate ($\mathbf{y} = f(\mathbf{x}; \theta_{best})$). They fail to quantify *how confident* they are in that prediction. This is dangerous in critical applications where knowing the uncertainty is as vital as knowing the prediction itself.

## Core Theory: Bayesian Inference
BDL applies Bayes' theorem to the model parameters:
$$ p(\theta|D) = \frac{p(D|\theta) p(\theta)}{p(D)} $$
*   **$p(\theta)$ (Prior)**: Our pre-existing belief about the weights before seeing any data (e.g., assuming weights are normally distributed).
*   **$p(D|\theta)$ (Likelihood)**: How well the model performs given a specific set of weights $\theta$.
*   **$p(\theta|D)$ (Posterior)**: The updated distribution of weights after observing the data, which is the goal.

### Inference Techniques
Since calculating the true posterior $p(\theta|D)$ is usually intractable, approximation methods are used:
1.  **Variational Inference (VI)**: (Ties into VAEs). We approximate the true posterior with a simpler, tractable distribution $q(\theta)$ (e.g., $\mathcal{N}(\mu, \Sigma)$).
2.  **Monte Carlo Dropout (MC Dropout)**: A computationally simpler method adapted from standard deep learning. By keeping dropout active during inference and running the model multiple times, we generate an ensemble of predictions, and the variance across these predictions estimates the model's uncertainty.

*BDL makes the model 'aware' of its own limitations, providing a full probabilistic range (mean $\pm$ variance) rather than just a single guess.*