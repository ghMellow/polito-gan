## Lecture Notes: Normalizing Flows
---
title: "Normalizing Flows"
date: "2026-05-12"
topics: [Flows]
source_slides: raw/slides-md/05. Normalizing flows.md
source_transcript: raw/lesson-transcripts/05. Normalizing flow and Latent diffusion models pt 2.md
status: draft
---
# Normalizing Flows (NF)

Normalizing Flows are a technique for probability density estimation. Unlike VAEs which are approximate, NFs aim to provide an **exact** calculation of the likelihood of an observed data point.

## The Core Principle: Change of Variables Theorem
The entire framework relies on the mathematical **change of variables theorem**. If we can define a transformation $f$ that maps a simple, known distribution (like a standard Gaussian $\mathbf{z} \sim \mathcal{N}(0, I)$) into the complex target distribution $\mathbf{x} \sim p_{\mathbf{x}}$, we can calculate the probability density function (PDF) of $\mathbf{x}$:

$$
\log p_{\mathbf{x}}(\mathbf{x}) = \log p_{\mathbf{z}}(\mathbf{z}) + \log \left| \det \left(\frac{\partial \mathbf{z}}{\partial \mathbf{x}}\right) \right|
$$

Where $\mathbf{z} = f(\mathbf{x})$ and the second term is the **Jacobian determinant** of the transformation. For the flow to be "normalizing," this determinant must be easily calculable.

## Structure and Implementation
A flow is constructed by chaining multiple invertible transformations ($f = f_K \circ \dots \circ f_1$). The overall log-likelihood is the sum of the log-likelihoods contribution from each component transformation.

Common NF designs include:
*   **RealNVP (Real-valued Non-linear Transformation)**: Uses coupling layers to ensure the Jacobian matrix is triangular, making the determinant trivial to calculate.
*   **Glow**: An advancement that introduced a structure using invertible 1x1 convolution and self-attention layers to create a more powerful flow structure.

## Comparison to Other Models
*   **Vs. VAEs**: NFs provide an exact likelihood estimation, making them theoretically superior for density estimation, but they are often much harder to train and computationally expensive due to the Jacobian determinant calculations.
*   **Vs. Diffusion**: While both are density estimators, NFs offer direct density calculation, whereas Diffusion models estimate the log-likelihood via sampling and reconstruction error.

*NF's primary strength is its rigorous mathematical foundation, allowing for exact likelihood calculations, provided the required invertible transformations can be found.*