# Derivation of 1D Fixed-Intercept MSE Loss (Quadratic Form)

For a simple 1D linear regression model with a fixed intercept $b$, the prediction model is:
$$\hat{y}_i = w x_i + b$$

The Mean Squared Error (MSE) loss function is:
$$f(w) = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i)^2 = \frac{1}{N} \sum_{i=1}^N (w x_i + b - y_i)^2$$

---

## 1. Expanding the Loss into Quadratic Form

Regroup the terms inside the square to isolate $w$:
$$(w x_i + b - y_i)^2 = \Big( (x_i w) + (b - y_i) \Big)^2$$

Apply the binomial expansion $(u + v)^2 = u^2 + 2uv + v^2$, where $u = x_i w$ and $v = (b - y_i)$:
$$\Big( (x_i w) + (b - y_i) \Big)^2 = x_i^2 w^2 + 2 x_i (b - y_i) w + (b - y_i)^2$$

Substitute this expanded expression back into the summation:
$$f(w) = \frac{1}{N} \sum_{i=1}^N \left[ x_i^2 w^2 + 2 x_i (b - y_i) w + (b - y_i)^2 \right]$$

Distribute the summation and the $\frac{1}{N}$ scaling across each term:
$$f(w) = \left( \frac{1}{N} \sum_{i=1}^N x_i^2 \right) w^2 + \left( \frac{2}{N} \sum_{i=1}^N x_i (b - y_i) \right) w + \left( \frac{1}{N} \sum_{i=1}^N (b - y_i)^2 \right)$$

---

## 2. Defining Constants A, B, and C

The loss function $f(w)$ is a quadratic equation in terms of $w$:
$$f(w) = A w^2 + B w + C$$

Where the coefficients are defined as:

* **$A$ (Quadratic Coefficient):**
  $$A = \frac{1}{N} \sum_{i=1}^N x_i^2 = \text{mean}(x^2)$$

* **$B$ (Linear Coefficient):**
  $$B = \frac{2}{N} \sum_{i=1}^N x_i (b - y_i) = 2 \cdot \text{mean}\big(x(b - y)\big)$$

* **$C$ (Constant Coefficient / Minimum Residual Variance):**
  $$C = \frac{1}{N} \sum_{i=1}^N (b - y_i)^2 = \text{mean}\big((b - y)^2\big)$$