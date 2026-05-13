## Overview and Principles

Latent Diffusion Models (LDMs) are state-of-the-art generative models that overcome the computational burden of working in high-dimensional pixel space by performing the diffusion process in a compressed **latent space**.

### The Diffusion Process
LDMs define a gradual, controlled degradation process (the forward process). Data $x_0$ is slowly corrupted by iteratively adding Gaussian noise ($x_t$), eventually transforming it into pure noise ($x_T$).

The genius of the model lies in learning how to reverse this process (the reverse process). The model $\epsilon_\theta$ is trained not to predict the next clean state, but to precisely predict the noise ($\epsilon$) added at step $t$, given $x_t$ and $t$.

### The Latent Space Pipeline
The full generative process works as a pipeline:
1.  **Compression (VAE Encoder)**: A pre-trained Variational Autoencoder (VAE) maps the high-resolution image $x$ to a compact latent vector $z$.
2.  **Denoising (U-Net)**: The diffusion process runs on $z$, iteratively predicting and removing noise until a clean latent representation $z_0$ is achieved.
3.  **Conditioning**: Text prompts are integrated into the U-Net's cross-attention layers, ensuring every step of the denoising process is guided by the semantic text embedding.
4.  **Reconstruction (VAE Decoder)**: The final latent vector $z_0$ is passed through the VAE decoder to reconstruct the final, high-resolution image $x$.

*LDMs are highly scalable and stable, making them the dominant method for complex text-to-image synthesis.*