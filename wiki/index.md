# Wiki — Generative AI for Graphics & Multimedia

## Generative Models
- [GAN](models/gan.md) GANs are general frameworks for learning data distributions through adversarial competition. The core architecture consists of two interconnected networks: the **Generator (G)** and the **Discriminator (D)**. The training process is defined by a minimax objective, where G attempts to minimize the probability that D correctly identifies its output as fake, while D attempts to maximize that recognition probability. Key advances include **DCGAN** and **WGAN**, which stabilize training using architectural constraints or a more robust loss measure (Wasserstein distance).
- [VAE](models/vae.md) — Variational Autoencoders for structured latent space learning. Links to: [Image Synthesis](applications/image-synthesis.md)
- [Diffusion](models/diffusion.md) — Emerging state-of-the-art model based on progressive denoising. Links to: [Image Synthesis](applications/image-synthesis.md)
- [Bayesian Deep Learning](models/bayesian-deep-learning.md) — Quantifying model uncertainty through probabilistic weight estimation.
- [EBM](models/energy-based.md) — Model based on potential functions.
- **[Transformers](models/transformers.md)** — Core architecture for sequence processing, including Attention and Masked Self-Attention.
- **[Latent Diffusion](models/latent-diffusion.md)** — Diffusion models operating efficiently in a highly compressed latent space.

## Theoretical Models
- **[RL](models/rl-overview.md)** — Mathematical framework for optimal decision-making in uncertain environments.

## Tools and Applications
- **[ML Agents](tools/mlagents.md)** — Framework for deploying AI policy within simulated or physical environments.
- **[RNN/Transformers](tools/transformer-basics.md)** — Reference guide to foundational sequential architectures.

## Assessment
- [Group Project](assessment/project.md) — guidelines, deadlines, criteria
- ...