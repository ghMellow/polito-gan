## **Bayes' Rule** 

## **From conditional probability to Bayes’ Rule** 

Let’s start from the **definition of conditional probability** . For any two events A and B with P(B) > 0: 

## **`P(A, B)  =  P(A | B) · P(B)  =  P(B | A) · P(A)`** 

Both middle and right expressions equal the joint probability P(A, B). Set them equal and divide both sides by P(B): 

## **`P(A | B)  =  P(B | A) · P(A)  /  P(B)`** 

That is the entire derivation of the Bayes’ rule  — one line of algebra, no additional assumptions. 

## **Anatomy of the Formula** 

|**Term**|**Meaning**|
|---|---|
|||
|**`P(A | B)`**|**Posterior:**our updated belief about A after seeing B|
|||
|**`P(B | A)`**|**Likelihood**: how probable is the evidence B if A were true|
|||
|**`P(A)`**|**Prior:**our belief about A before seeing any evidence|
|||
|**`P(B)`**|**Evidence (**marginal likelihood): total probability of observing B<br>under all hypotheses|



**Intuitive reading:** _"Start with a belief about A (the prior). Observe evidence B. Scale that belief up or down by how well A predicts B (the likelihood). Normalise so everything sums to 1 (divide by P(B)). The result is your updated belief (the posterior)."_ 

Bayes' rule is **not** a heuristic or a modelling choice — it is a **theorem** that follows directly from the axioms of probability. Any rational agent that updates beliefs on evidence must obey it. 

## **Why Bayes Matters for Generative Models** 

## **Generative modelling: learning p(x)** 

A **generative model** is a model that learns the probability distribution `p(x)` over some data space — images, text, audio, molecules. Once learned, we can **sample** new data by drawing from `p(x)` . 

## **Conditional generation: learning p(x | c)** 

In practice we almost always want to generate data given a **condition** c (a text prompt, a class label, a style reference). The model must learn `p(x | c)` — the distribution of x _given_ c. 

## **The Bayesian bridge** 

Apply Bayes' rule with A = x (data) and B = c (condition): 

```
p(x | c)  =  p(c | x) · p(x)  /  p(c)
```

Bayes connects `p(x|c)` to `p(c|x)` — enabling techniques such as classifier guidance. 

## **The Intractability Problem** 

## **Why P(B) is the bottleneck** 

Bayes' rule is exact, but applying it requires computing the **marginal (evidence)** P(B). In continuous, high-dimensional settings this means evaluating an integral: 

```
p(x)  =  integral  p(x | z) · p(z)  dz
(sum over all possible latent states z)
```

For a latent space of even modest dimension, this integral has no closed form. The cost of numerical approximation grows **exponentially** in the dimension of z — a phenomenon known as the **curse of dimensionality** . For a 512-dimensional latent space, exact marginalisation is computationally impossible. 

**Coming up: autoregressive models** 

The autoregressive factorisation transforms an intractable joint distribution into a **sequence of tractable conditionals** . Each conditional `p(x_t | x_1, ..., x_{t-1})` is modelled by a neural network (e.g. a Transformer) trained with 

maximum-likelihood on the next token. The price paid is **sequential generation** : tokens must be sampled one at a time. 

