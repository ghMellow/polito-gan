## Lecture Notes: Transformers and Autoregressive Models
---
title: "Transformers and Autoregressive Models"
date: "2026-05-12"
topics: [Transformers, Autoregressive]
source_slides: raw/slides-md/02. Transformers and autoregressive.md
source_transcript: raw/lesson-transcripts/03. Transformers and autoregressive pt 2.md
status: draft
---

# Continuation: Autoregressive Generation and GPT

This second part focuses on how Transformers are used in a purely **autoregressive** manner, which is fundamental to modern large language models (LLMs) like GPT.

## Autoregressive Decoding
When a Transformer is used for text generation, it operates auto-regressively. This means that at each step, it predicts the *next* token based on all the tokens generated and provided up to that point.

1.  Token 1 is fed in.
2.  Prediction for Token 2 is made based on Token 1.
3.  Token 2 is fed in, and Prediction for Token 3 is made based on [Token 1, Token 2].
4.  This continues until an end-of-sequence token is generated.

The key constraint here is that the model is **cautious—the context is always limited to what has already been written.**

## Masked Self-Attention
To enable correct autoregressive prediction during training, a crucial modification is required: **Masked Self-Attention**.

*   **The Mask**: During training, when calculating the attention weight for a token at position $i$, the model must be prevented from "cheating" by looking at tokens at positions $j > i$.
*   **Mechanism**: A mask (typically setting certain values to $-\infty$) is applied to the attention scores matrix *before* the softmax calculation. This ensures the attention weights for future positions are zeroed out, enforcing a true causal dependency graph.

## Large Language Models (LLMs)
Modern LLMs, particularly those derived from the GPT architecture, are essentially massive, scaled-up, masked Transformers.
*   **Scale**: Models are trained on vast, diverse datasets, enabling them to capture an encyclopedic and human-like knowledge base.
*   **Emergent Abilities**: Scaling laws suggest that as models get larger (more parameters) and are trained on more data, they develop "emergent abilities"—complex behaviors that were not explicitly programmed (e.g., performing zero-shot reasoning, complex coding).

*This completes the view of the Transformer architecture, showing how the attention mechanism is modified (masked) to enforce directional, causal generation.*