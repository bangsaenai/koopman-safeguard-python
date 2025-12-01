# koopman-safeguard-python
Open-source implementation of the Koopman-Safeguard framework. "Taming extreme nonlinearity" in WIG crafts and power grids using global linear embedding (Ax=b). Includes Python vs. MATLAB comparison.

🎯 The Mission: Democratizing Control Theory & Advanced control theory has long been locked behind expensive proprietary software and complex academic jargon. We believe safety-critical technology should be accessible to everyone.

This project proves that free, open-source Python code can match the precision of industry-standard tools (MATLAB) in solving complex control problems.

🧪 The "Kill Shot" Evidence

We compare the Koopman-Safeguard against standard Linearization.

🔴 Standard Linear: Fails to detect instability $\rightarrow$ System Crashes.
🟢 Koopman (Ours): Captures global topology $\rightarrow$ System Stabilizes.


🚀 FeaturesPhysics Simulation: A nonlinear WIG craft model exhibiting pitch instability.Koopman Lifting: Data-driven discovery of linear embeddings (EDMD).Safeguard Logic: The core $Ax=b$ solver for safety verification.Python vs. MATLAB: Side-by-side scripts proving 100% identical results.

git clone https://github.com/bangsaenai/koopman-safeguard-python.git

cd koopman-safeguard-python


🏆 The Global Challenge (Can you beat us?)
We have stabilized the system in 0.5 seconds. Can you do better? We invite engineers, researchers, and students to write their own controllers for our wig_glider.py environment.

1. Modify mission_pilot.py.

2. Implement your best PID, LQR, or Deep RL agent.

3. Submit your results via Pull Request or tag us on YouTube!

📚 Citation
If you use this code in your research, please cite our upcoming work:

T. Wonghong, "Taming Extreme Nonlinearity: A Koopman-Based Safeguard for Unstable Dynamical Systems," Draft submitted to Automatica, 2025.

## 🎥 Video 
Want to see the "Kill Shot" simulation in action?

[![Watch The Matlab vs. Python here first](https://img.youtube.com/vi/MO598pfmMqk/maxresdefault.jpg)](https://www.youtube.com/watch?v=MO598pfmMqk)
> **"Science should move at the speed of light, not the speed of peer review."**

---

## 🚨 SOLUTION REVEALED: The Moondust Manifesto

Critics said this code was "Too Simple". They called it "AI Slop". They said a \$0 script couldn't beat \$5,000 software.
**They were wrong.**

In this video, I reveal the mathematical secret ($Ax=b$) that bridges the gap between chaos and control. I explain why I am giving away this "Billion-Dollar" technology for free, and why the "Ivory Tower" of academia is crumbling.

**Watch this before you run the code. You need to understand the WHY before the HOW.**

[![Watch The Moondust Manifesto](https://img.youtube.com/vi/6rAqKiPowog/maxresdefault.jpg)](https://www.youtube.com/watch?v=6rAqKiPowog)
*(Click the image to watch the full revelation)*

## 🛑 Addressing the Skeptics: "It's just a P-Controller?"

We saw the discussions on Reddit. Some engineers pointed out:
> *"This isn't magic. It looks like a simple P-controller applied to the y^3 model."*

**You are absolutely right.** And that is exactly the breakthrough.

The power of the **Koopman Operator** is not in creating a complex controller. It is in finding the right **Coordinate Transformation (Lifting)**.
* We lift the nonlinear state $y \rightarrow \Psi(y) = [y, y^3]$.
* In this lifted space, the chaotic dynamics become linear ($z_{k+1} = Kz$).
* Once linear, even a "simple" controller becomes a weapon of mass stabilization.

**Complexity is not the goal. Solution is the goal.**
We proved that 50 lines of Python can outperform deep neural networks in stabilizing this system. Simplicity is the ultimate sophistication.

---
## ⚡ The Ultimate Proof: Running on Metal ($99 Jetson Nano)

Critics argued that this is "just a simulation". They doubted if it could run in the real world.
**Here is the answer.**

We deployed the exact same Python script (`kill_shot_demo.py`) onto an old **NVIDIA Jetson Nano (4GB)**.
* **No GPU Acceleration.**
* **No C++ Compilation.**
* **Just pure Python Math ($Ax=b$).**

[![Watch the Jetson Nano Test](https://img.youtube.com/vi/OY3n2kQ7RvA/maxresdefault.jpg)](https://www.youtube.com/watch?v=OY3n2kQ7RvA)

**The Result:** Real-time stabilization with minimal CPU load. Proof that smart math beats expensive hardware.

---


## 🌪️ Coming Soon: Level 2 - The Stochastic Storm

Level 1 was a deterministic toy model. It was designed to be solved.
But the real world is **noisy**.

We are preparing **"The Bangsaen Benchmark Level 2"**:
* 🌊 **Process Noise:** Random turbulence added to the physics.
* 📡 **Measurement Noise:** Your sensors will lie to you.
* ⏳ **Input Delay:** Real-world lag.

**The Question:**
Will your standard PID or LQR survive when the world fights back?
Or will you need a **Robust Koopman** estimator?

**Status:** *Code dropping soon. Stay tuned.*

---
