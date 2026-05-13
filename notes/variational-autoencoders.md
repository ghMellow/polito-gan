## Lecture Notes: Variational Autoencoders (VAEs)
---
title: "Variational Autoencoders"
date: "2026-05-12"
topics: [VAEs]
source_slides: raw/slides-md/03. Variational autoencoders.md
source_transcript: N/A (Slide-based derivation)
status: draft
---

# Variational Autoencoders (VAEs)

VAEs are a generative model that provides a structured and mathematically sound alternative to traditional autoencoders, aiming to learn the underlying probability distribution of the data ($\mathbf{p}(\mathbf{x})$). Unlike standard autoencoders, VAEs do not just learn an arbitrary compression; they enforce that the latent space follows a simple prior distribution, typically a standard Gaussian ($\mathcal{N}(0, I)$).

## The Core Problem: Inferring the Posterior
A standard autoencoder learns an encoding function $q_\phi(z|x)$ that maps an input $\mathbf{x}$ to a latent vector $z$. This $q_\phi$ is an approximation (or *inference*) of the true posterior probability $\mathbf{p}(z|x)$—the true probability of the latent representation $z$ given $\mathbf{x}$. VAEs aim to model this intractable posterior.

## The Variational Objective (ELBO)
VAEs introduce a **variational lower bound** on the log-likelihood of the data, known as the Evidence Lower Bound (ELBO):

$$ \log p_\mathbf{x}(\mathbf{x}) \ge \mathbb{E}_{q_\phi(z|x)} \left[ \log \frac{p_\mathbf{x}(\mathbf{x}|z)}{q_\phi(z|x)} \right] - D_{KL}(q_\phi(z|x) \parallel p(z)) $$

During training, the model maximizes the ELBO. This decomposes into two terms:
1.  **Reconstruction Term:** $\mathbb{E}[\log p_\mathbf{x}(\mathbf{x}|z)]$. This measures how well the decoder can reconstruct the input from the sampled latent code $z$.
2.  **KL Divergence Term:** $D_{KL}(q_\phi(z|x) \parallel p(z))$. This regularizes the latent space by forcing the learned posterior $q_\phi(z|x)$ to stay close to the simple prior distribution $p(z)$.

## The Inference Process
Instead of outputting a single latent vector $z$, the encoder is designed to output the parameters ($\mu$ and $\sigma$) of a Gaussian distribution:
$$ q_\phi(z|x) = \mathcal{N}(z; \mu(x), \Sigma(x)) $$
By modeling the distribution, we allow the model to perform *stochastic sampling* later, which is key to generating diverse and varied outputs.

### Latent Space Implications
The requirement that the latent space adheres to $\mathcal{N}(0, I)$ is critical because it guarantees that a simple sampling method (drawing $z$ directly from $\mathcal{N}(0, I)$) will yield plausible inputs for the decoder, enabling high-quality generation.

*Conclusion: VAEs leverage the ELBO to make the latent space structured and continuous, enabling meaningful sampling for generative tasks.*