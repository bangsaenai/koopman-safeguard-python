# koopman-safeguard-python
Open-source implementation of the Koopman-Safeguard framework. Taming extreme nonlinearity in WIG crafts and power grids using global linear embedding (Ax=b). Includes Python vs. MATLAB comparison.

🎯 The Mission: Democratizing Control TheoryAdvanced control theory has long been locked behind expensive proprietary software and complex academic jargon. We believe safety-critical technology should be accessible to everyone.This project proves that free, open-source Python code can match the precision of industry-standard tools (MATLAB) in solving complex control problems.🧪 The "Kill Shot" EvidenceWe compare the Koopman-Safeguard against standard Linearization.

🔴 Standard Linear: Fails to detect instability $\rightarrow$ System Crashes.
🟢 Koopman (Ours): Captures global topology $\rightarrow$ System Stabilizes.

![image](https://github.com/bangsaenai/koopman-safeguard-python/issues/1) 

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

