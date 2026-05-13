## Background and Core Concepts

**Transformers** revolutionized sequence processing by eliminating the need for recurrence. They rely entirely on the **Attention Mechanism**, allowing every element in the sequence to be compared against every other element simultaneously.

### The Self-Attention Mechanism
Self-attention calculates a weight matrix that quantifies the relationship between every token pair. This is computed using drei vectors derived from input embeddings:
1.  **Query (Q)**: What information a token is looking for.
2.  **Key (K)**: What information a token contains.
3.  **Value (V)**: The information payload carried by the token.

The weight is calculated via a scaled dot-product attention: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$.
**Multi-Head Attention** runs this process in parallel to allow the model to focus on multiple types of dependencies simultaneously.

### Positional Encoding
Since the Transformer processes tokens in parallel, it loses word order information. **Positional Encoding** solves this by injecting position-specific signals into the input embeddings, ensuring that the model knows the order of tokens.

### Autoregressive Generation
For text generation (like GPT), the architecture must be modified to enforce causality. This requires **Masked Self-Attention**, where the attention scores for any given token are masked (set to $-\infty$) if they correspond to a future token.

*This model structure is foundational for modern LLMs and sequence tasks.*