## Overview (Density Estimation)

Normalizing Flows (NFs) are an explicit and mathematically rigorous family of models for density estimation. Their defining feature is their ability to calculate the **exact** likelihood of any data point, a capability that approximate methods like VAEs lack.

### Core Theory: Change of Variables
The foundation is the change of variables theorem. If we define a series of invertible transformations ($f = f_K \circ \dots \circ f_1$) mapping a simple base distribution ($\mathbf{z}$, e.g., standard Gaussian) to the complex data distribution ($\mathbf{x}$), the log-likelihood of $\mathbf{x}$ can be calculated using the determinant of the Jacobian matrix of the total transformation $f$.

$$\log p_{\mathbf{x}}(\mathbf{x}) = \log p_{\mathbf{z}}(\mathbf{z}) + \log | \det J |$$

### Key Requirements
For a flow to be "normalizing," the transformation must be invertible, and the Jacobian determinant $|\det J|$ must be mathematically tractable for computation.

### Variational Comparison
*   **Vs. VAEs**: While VAEs are highly popular for their stability and simplicity, they are generally an approximation of the true likelihood function; NFs provide an exact density estimate.
*   **Vs. Diffusion Models**: Diffusion models are excellent for synthesis and sampling but often provide the log-likelihood estimate indirectly via reconstruction error.

**Advanced NFs** like those combining RealNVP and Glow improve structure by using specialized layers (like coupling layers) that guarantee the Jacobian is simple enough to compute efficiently.

*NFs are essential when *exact* density evaluation is a core requirement of the application.*