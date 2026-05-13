## Lecture Notes: Generative Adversarial Networks
---
title: "Generative Adversarial Networks"
date: "2026-05-12"
topics: [GAN]
source_slides: raw/slides-md/01. Generative adversarial networks.md
source_transcript: raw/lesson-transcripts/01. Intro and Generative adversarial networks.md
status: draft
---

# Generative Adversarial Networks

The core idea of **GANs** is to train two competing networks simultaneously: a **Generator (G)** and a **Discriminator (D)**. This adversarial setup forces the generator to become increasingly adept at fooling the discriminator, resulting in the creation of highly realistic synthetic data.

## The Core Mechanism: Adversarial Game
*(Synthesis of slides and transcript explaining the minimax game.)*

The process is framed as a **minimax game**:
$$ \min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{data}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log (1 - D(G(z)))] $$

*D* tries to distinguish between real data ($x$) and generated data ($G(z)$), while *G* tries to maximize the probability of *D* making an error.

## Key Components
### 1. The Generator (G)
*   **Goal**: To map a simple latent space vector ($z$)—often sampled from a standard Gaussian distribution—to a high-dimensional data point that resembles the real data distribution ($p_{data}$).
*   **Function**: Takes low-dimensional noise ($z$) and outputs synthetic data ($\hat{x} = G(z)$).

### 2. The Discriminator (D)
*   **Goal**: To act as a binary classifier, determining the probability that an input data point is real (close to 1) or fake (close to 0).
*   **Input**: Takes a data point ($x$ or $G(z)$) and outputs $D(x) \in [0, 1]$.

## Training Dynamics
*(Detailed explanation of the alternating training procedure, referencing insights from the lecture transcript.)*

The training is iterative:
1.  **Train D**: Keep G fixed. Optimize D to maximize its ability to correctly classify real vs. fake data.
2.  **Train G**: Keep D fixed. Optimize G to fool D (i.e., make $D(G(z))$ as close to 1 as possible).

## Variations
*   **DCGAN (Deep Convolutional GAN)**: Used architectural constraints (e.g., using convolutional layers and avoiding pooling layers) to stabilize training and enforce structural consistency.
*   **WGAN (Wasserstein GAN)**: Introduced the Wasserstein distance (Earth Mover's distance) to provide a more meaningful gradient estimate than the traditional cross-entropy loss, significantly improving training stability, especially in early stages.

*This note summarizes the conceptual model and training dynamics of GANs, prioritizing the professor's explanation of the minimax game over a purely structural recitation of the slides.*