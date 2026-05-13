## Lecture Notes: 3D Data Representations
---
title: "3D Data Representations"
date: "2026-05-12"
topics: [3D]
source_slides: raw/slides-md/04. 3D data representations.md
source_transcript: N/A (Slide-based derivation)
status: draft
---

# 3D Data Representations

Modeling and generating 3D geometry is a complex computational problem that requires adapting 2D image-based generative models. This note outlines the common techniques used to represent and synthesize 3D structure from generative AI concepts.

## The Challenge of 3D Structure
Traditional images are 2D projections. Modeling 3D objects requires capturing geometry (shape), material (texture), and camera pose (viewpoint consistency). The data is fundamentally more complex than a simple RGB image.

## Common Representation Formats
Different representations define the object in different ways, each with its own generative challenges:
*   **Point Clouds**: A collection of points in $\mathbb{R}^3$. They are sparse and highly variable, making them difficult to process with standard convolutional networks.
*   **Voxels**: A 3D discrete grid (like voxels in a video game). They are straightforward for CNNs but suffer from the "curse of dimensionality" (memory explodes very quickly).
*   **Meshes (Triangles)**: The industry standard, consisting of vertices and faces (triangles). These are computationally efficient but topologically complex to optimize and sample from.

## Generative Approaches for 3D
1.  **Direct Point Cloud Generation**: Using PointNet or similar architectures to learn the distribution of points directly.
2.  **View Synthesis (2D $\rightarrow$ 3D)**: Training models (often based on diffusion) to generate multi-view images or depth maps, which can then be used to reconstruct a consistent 3D shape.
3.  **Implicit Representations (NeRFs)**: Using Neural Radiance Fields (NeRFs) to represent a scene implicitly as a function $\mathbf{F}: (\mathbf{x}, \mathbf{d}) \rightarrow (\mathbf{c}, \sigma)$, where $(\mathbf{x}, \mathbf{d})$ are $(x, y, z)$ coordinates and viewing direction, and $(\mathbf{c}, \sigma)$ is the predicted color and density (opacity) at that point.

## Synthesis and Future Work
Generative models are moving towards using coupled systems, such as generating a coarse mesh structure first, and then using a diffusion process to refine the texture and high-frequency details while ensuring view-consistency across all outputs.

*The shift in 3D generation is increasingly toward implicit representations (like NeRFs) due to their ability to capture fine-grained details and view-dependent effects.*