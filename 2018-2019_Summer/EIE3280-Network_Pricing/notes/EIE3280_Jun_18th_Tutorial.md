### EIE3280 Jun 18th Tutorial

#### Content

- Brief Review

  - Cellular Networks

    TDMA / FDMA / OFDMA*

    - *Signal to Interference Ration(SIR)* $SIN = \frac{S}{I+N}$
    - *Distributed Power Control (DPC)*

  - View 1: Optimization Problem

  - View 2: Game Theory

- Problems

- Summary

---

#### Cellular Network

- Cell

  - Base Stations (BS)
  - Mobile Stations (MS)

- Resource

  - Frequency - *(Important also due to the path-loss)*
  - Time
  - Energy

- Methodologies to allocate the resources

  - Orthogonal allocation: *FDMA, TDMA, CDMA*

  - Non-orthogonal allocation: *(practical) CDMA* 

    - Reasons

      - **Code is finite**

      - When ***the length of the code is long***, in practical CDMA may cause ***uplink problem***

         **(not synchronized)**

  - Methodologies to avoid interference in practical CDMA
    - Near-far problem
    - Feedback control
      - Transmit power control
      - *Received signal power equalization (regulations)*
    - Distributed power control 
      - SIR
      - Distributed power control

$$
\begin{align*}
\gamma_1 &= \frac{p_1}{p_2+n} \\
\gamma_2 &= \frac{p_2}{p_1+n} \\
\log\gamma_1+\log\gamma_2 &= \log p_1 + \log p_2 - \log(p_1+n) - \log(p_2+n)\\
&\text{Contribute to the plotting}
\end{align*}
$$

---

### Linear Algebra for DPC

$$
\begin{align*}
\gamma_i &= \frac{G_{ii}p_i}{\sum_{j\not=i}G_{ij}p_j}\\
         &= \frac{p_i}{\sum_{j\not=i}\frac{G_{ij}}{G_{ii}}p_j}\\
         \frac{1}{r}  &= \lambda
\end{align*}
$$



---

*Q.E.D*