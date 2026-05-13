---
title: "Generative Adversarial Networks (GANs)"
category: models
tags: [generative-model, adversarial, image-synthesis, minimax, wasserstein]
related: [vae.md, diffusion.md]
last_updated: 2026-05-09
status: complete
---

Generative Adversarial Networks (GANs) represent a powerful framework for model learning that tackles complex data distributions by pitting two neural networks against each other in a zero-sum minimax game. They are primarily used for high-fidelity image and multimedia synthesis.

### Structure and Principle

A GAN consists of two primary components:

1.  **The Generator ($\mathbf{G}$):** This network takes a random noise vector $\mathbf{z}$ (sampled from a latent space $\mathcal{Z}$) and maps it to the input space, generating a synthetic or "fake" sample $\mathbf{G}(\mathbf{z})$.
2.  **The Discriminator ($\mathbf{D}$):** This network acts as a binary classifier. Given an image (either real $x$ or fake $G(\mathbf{z})$), $\mathbf{D}$ estimates the probability that the input belongs to the real data distribution $P_{\text{data}}$.

The training process is designed as a **minimax game**, where:
*   **Discriminator's Objective:** To maximize the probability of correctly classifying real data as real and generated data as fake.
*   **Generator's Objective:** To minimize this probability by generating samples so realistic that the Discriminator cannot differentiate them from real data.

### Core Mechanisms and Early Models

Early implementations often used Convolutional GANs (DCGANs) for image tasks. The objective function involves calculating the expected value under $P_{\text{data}}$ and $P_g$:

$$\min_G \max_D \mathbb{E}_{x \sim P_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim P_z}[\log(1 - D(G(z)))]$$

**Challenges with Standard GAN Formulation:**
1.  **Vanishing Gradients:** When the Discriminator becomes too skilled, it can output values close to 0 or 1 (highly confident prediction). This proximity leads to vanishing gradients for the Generator, causing it to cease learning, even if the image quality could improve.
2.  **Mode Collapse:** The Generator can become "lazy," finding a small subset of the data manifold (a specific set of samples) where the Discriminator is weakest, and only generating samples from that limited subset, failing to capture the full diversity of the real data distribution.

### Advanced GANs: Wasserstein GAN (WGAN)

To overcome these training stability issues, Wasserstein GANs (WGANs) replace the binary classification objective with the **Wasserstein Metric** (or Earth Mover's Distance). Instead of a binary classifier $\mathbf{D}$, the model uses a **Critic ($C$)** that outputs a single real value representing the "distance" or "score" between the real and fake distributions.

The Wasserstein distance measures the minimum "cost" required to transform one probability distribution into another. The training objective thus becomes:

$$\min_G \max_C \left( \mathbb{E}_{z \sim P_z}[C(G(z))] - \mathbb{E}_{x \sim P_{\text{data}}}[C(x)] \right)$$

By maximizing this difference, both networks are encouraged to push the distributions closer together in a stable manner, resulting in a much more robust training process and better diversity coverage.

### Conclusion

GANs remain a cornerstone of generative modeling, offering high-resolution synthesis capabilities. While the initial formulation is theoretically complex and unstable, modern variants (like WGANs) achieve stable convergence by reframing the objective as a distance measurement, which is mathematically and computationally more manageable.

**Key Takeaways:**
*   GANs use a Generator ($\mathbf{G}$) and a Discriminator/Critic ($\mathbf{D}$/$\mathbf{C}$).
*   The process is framed as a zero-sum minimax game.
*   WGANs enhance stability by using the Wasserstein metric, replacing binary classification with a continuous "distance" score.