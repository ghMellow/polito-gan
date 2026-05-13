## Lecture Notes: Course Introduction
---
title: "Course Introduction"
date: "2026-05-12"
topics: [Overview]
source_slides: raw/slides-md/00. Course introduction.md
source_transcript: N/A (Slide-based overview/reference)
status: draft
---

# Course Introduction

This lecture serves as the foundational overview for the discipline of Generative AI for Graphics & Multimedia. The course structure is designed to take students from foundational models to advanced, state-of-the-art techniques.

## Modularity
The course is segmented into several independent yet complementary systems:
1.  **Generative Modeling**: Focuses on the core mathematical mechanisms used to learn probability distributions and synthesize new data (e.g., GANs, VAEs, Diffusion).
2.  **Architecture**: Explores foundational building blocks (e.g., the Transformer, Attention mechanisms).
3.  **Applications**: Demonstrates how these models are implemented in specialized tasks (e.g., 3D reconstruction, synthetic data).

## Key Concepts to Master
*   **Inverse Problem**: Most generative AI tasks are about solving an inverse problem: given a complex target data space and a simple prior distribution, how do we map the simple prior to the complex space?
*   **Latent Space**: The critical concept. The goal of many advanced models is to learn a continuous, structured, and low-dimensional *latent space* $z$, such that sampling from $\mathcal{N}(0, I)$ in that space yields plausible outputs in the high-dimensional pixel space.

## Module Sequence
The course progresses logically:
1.  Start with foundational generative models to introduce the concept of learning a distribution.
2.  Advance to sequence modeling (Transformers) to handle structured data like text.
3.  Introduce specialized domains (3D, Physics) to expand the scope of application.
4.  Conclude with advanced frameworks (ML Agents) for real-world deployment.

*This module sets the scope and context, establishing the shared vocabulary required for studying the advanced topics.*