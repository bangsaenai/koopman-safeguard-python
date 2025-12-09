# 📑 BEYOND THE DERIVATIVE: A New Paradigm for Capstone Design
### *Solving Non-Linear Instability via Koopman Operators on Edge Microcontrollers*

**Authored by:** Bangsaen AI Labs (The Father)
**Context:** Advanced Control Systems / Engineering Education Reform
**Standard:** ABET Criterion 3 & 5 Compliant

---

## 📝 Abstract

Traditional engineering education often culminates in the PID Controller, a tool that fails catastrophically when applied to **"Complex Engineering Problems"** as defined by ABET—specifically in highly non-linear environments like Wing-In-Ground (WIG) effect craft.

This article proposes a paradigm shift for Capstone Design: replacing expensive hardware and legacy PID tuning with **Koopman Operator Theory** running on low-cost ESP32 microcontrollers. By lifting non-linear dynamics into a linear infinite-dimensional space, we demonstrate how students can solve complex instability issues without "D-term" noise amplification, effectively replacing financial budget with mathematical rigor.

---

## 1. The Crisis in Engineering Education

According to **ABET Criterion 3 (Student Outcomes)**, students must demonstrate *"an ability to identify, formulate, and solve complex engineering problems."*

However, the reality in many universities—particularly in developing regions—is a reliance on "Safe Problems":
* **Linear Systems:** Controlling water levels or motor speeds.
* **Brute Force Hardware:** Solving problems by purchasing expensive flight controllers (e.g., Pixhawk) rather than engineering the control logic.

**Project Iron Man (Mark 2)** was created to break this cycle. It forces the student to confront a chaotic, non-linear environment (Ground Effect) using a microcontroller that costs less than lunch ($5), prohibiting the use of brute-force hardware.

---

## 2. The Problem: Why PID Fails the "Mark 2" Rig

In the development of the **Mark 2 Avionics Rig**, we encountered the fundamental limitations of classical control theory:

### A. The Derivative (D) Nightmare
* **The Context:** A WIG-Craft flying centimeters above the surface experiences high-frequency vibration and aerodynamic turbulence.
* **The Failure:** The PID's **Derivative (D) term** calculates the rate of change of error ($dE/dt$). In a high-vibration environment, the D-term amplifies sensor noise, causing extreme servo jitter and thermal runaway.
* **The Trap:** Increasing filtering adds **Phase Lag**, causing the system to react too slowly to prevent a crash.

### B. Reactive vs. Predictive
* PID is **reactive** (Error exists -> Correct it).
* In high-speed ground effect flight, if you wait for the error to occur, you have already crashed.

---

## 3. The Solution: The Koopman Operator

To solve this without upgrading hardware, we applied **Koopman Operator Theory**, a method often reserved for supercomputers, optimized here for the ESP32.

### A. The Concept
Instead of fighting the non-linear dynamics in state space, we "lift" the state observables into a higher-dimensional space where the evolution of the system becomes **linear**.

$$g(x_{k+1}) = K g(x_k)$$

### B. Why It Beats PID
1.  **No D-Term Required:** Because the Koopman Operator learns the *physics* (dynamics) of the system, it predicts the next state inherently. We do not need to calculate the derivative of the error. **Zero D-term = Zero Noise Amplification.**
2.  **Predictive Control:** The system anticipates turbulence rather than reacting to it.
3.  **Computational Efficiency:** Once the $K$ matrix is computed (offline or via adaptive mixing), the runtime execution on the ESP32 is simple matrix multiplication—faster than a complex PID loop with filters.

---

## 4. Mapping to ABET Criteria

Project Iron Man Mark 2 is not just a prototype; it is a blueprint for a compliant **Capstone Design Project**:

| ABET Criterion | Implementation in Mark 2 |
| :--- | :--- |
| **1. Complex Engineering Problem** | Solving Ground Effect instability (Aerodynamic non-linearity) without standard libraries. |
| **2. Engineering Design** | Designing a custom avionics architecture on bare-metal hardware. |
| **3. Conflicting Constraints** | Achieving high-frequency control (>500Hz) and stability under extreme cost constraints (<$15) and power limits. |
| **4. Modern Tools** | utilizing **Data-Driven Control** and **Koopman Theory** instead of manual heuristic tuning. |

---

## 5. Conclusion: The "Alien Engineering" Philosophy

This project proves that **financial constraints are not an excuse for mediocrity.**
In fact, constraints are the fuel for innovation.

By refusing to use expensive Flight Controllers, we forced ourselves to discover a superior mathematical solution. This is the essence of **Alien Engineering**: doing more with less, using the power of pure logic.

**To the Students & Professors:**
Stop teaching students how to tune $K_p, K_i, K_d$.
Start teaching them how to model the physics of the universe.

**The Era of PID is over.**

---

*Bangsaen AI Labs*
*Open Source for the True Engineers*
