### Proof of Equivalence: Matrix Inverse vs. Scalar Calculus (1D Fixed Intercept)

We want to prove that the **Normal Equation** (Linear Algebra) and the **Derivative Minimum** (Calculus) compute the exact same optimal slope $w$.

---

#### 1. Linear Algebra Formulation

Given:
* Feature matrix $X \in \mathbb{R}^{N \times 1}$ containing values $[x_1, x_2, \dots, x_N]^T$
* Adjusted target vector $y_{\text{adj}} \in \mathbb{R}^{N \times 1}$ containing values $[y_1 - b, y_2 - b, \dots, y_N - b]^T$

The 1D Normal Equation is:
$$w_{\text{matrix}} = (X^T X)^{-1} X^T y_{\text{adj}}$$

Evaluating each matrix component:

1. **The dot product $X^T X$:**
   $$X^T X = \begin{bmatrix} x_1 & x_2 & \dots & x_N \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_N \end{bmatrix} = \sum_{i=1}^N x_i^2$$

2. **The scalar inverse $(X^T X)^{-1}$:**
   Since $X^T X$ is a $1 \times 1$ scalar:
   $$(X^T X)^{-1} = \frac{1}{\sum_{i=1}^N x_i^2}$$

3. **The projection $X^T y_{\text{adj}}$:**
   $$X^T y_{\text{adj}} = \begin{bmatrix} x_1 & x_2 & \dots & x_N \end{bmatrix} \begin{bmatrix} y_1 - b \\ y_2 - b \\ \vdots \\ y_N - b \end{bmatrix} = \sum_{i=1}^N x_i(y_i - b)$$

Combining these yields:
$$w_{\text{matrix}} = \frac{\sum_{i=1}^N x_i(y_i - b)}{\sum_{i=1}^N x_i^2}$$

Dividing numerator and denominator by $N$:
$$w_{\text{matrix}} = \frac{\frac{1}{N} \sum_{i=1}^N x_i(y_i - b)}{\frac{1}{N} \sum_{i=1}^N x_i^2}$$

---

#### 2. Scalar Calculus Formulation

> *For the step-by-step algebraic expansion defining coefficients $A$, $B$, and $C$, see [`derivation_1d_mse_quadratic_form.md`](./derivation_1d_mse_quadratic_form.md).*

The MSE Loss function as a parabola is defined as:
$$f(w) = A w^2 + B w + C$$

Where:
$$A = \text{mean}(x^2) = \frac{1}{N} \sum_{i=1}^N x_i^2$$
$$B = 2 \cdot \text{mean}(x(b - y)) = \frac{2}{N} \sum_{i=1}^N x_i(b - y_i)$$

Setting the derivative $f'(w) = 2Aw + B = 0$ gives:
$$w_{\text{calculus}} = -\frac{B}{2A}$$

Substituting $A$ and $B$:
$$w_{\text{calculus}} = -\frac{\frac{2}{N} \sum_{i=1}^N x_i(b - y_i)}{2 \cdot \frac{1}{N} \sum_{i=1}^N x_i^2}$$

Canceling the factor of $2$ and distributing the negative sign into $(b - y_i)$:
$$w_{\text{calculus}} = \frac{\frac{1}{N} \sum_{i=1}^N x_i(y_i - b)}{\frac{1}{N} \sum_{i=1}^N x_i^2}$$

---

#### Conclusion

$$\therefore \quad w_{\text{matrix}} = w_{\text{calculus}} = \frac{\frac{1}{N} \sum_{i=1}^N x_i(y_i - b)}{\frac{1}{N} \sum_{i=1}^N x_i^2}$$

The Matrix Inverse method and the Calculus Derivative method are mathematically identical.