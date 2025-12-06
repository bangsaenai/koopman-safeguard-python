# ==============================================================================
# 🚁 WIG GLIDER SIMULATION ENVIRONMENT
# ==============================================================================
# Developed by: Bangsaen AI (The Pilot & The System)
# Origin: https://github.com/bangsaenai/koopman-safeguard-python
# License: MIT (Attribution Required)
#
# ⚠️ WARNING:
# This code is part of the "Moondust Protocol".
# If you use this simulation in your paper/project without citation,
# you are violating the core principles of Open Science.
# ==============================================================================
import numpy as np

class WIGGlider:
    """
    The 'Bangsaen Control Benchmark-1' (BCB-1)
    System: Wing-in-Ground Craft Pitch Dynamics (Unstable)
    Goal: Stabilize the craft at the target altitude/angle without crashing.
    """
    def __init__(self):
        self.state = 0.05 # Initial state (Critical unstable point)
        self.target = 1.0 # The safe stable equilibrium
        self.crash_limit = 2.0 # If state > 2 or < -2, vehicle crashes
        self.time_step = 0
        self.max_steps = 100
        self.history = []
        self.done = False

    def reset(self):
        self.state = 0.05
        self.time_step = 0
        self.history = [self.state]
        self.done = False
        return self.state

    def step(self, u_control):
        """
        The Nonlinear Physics Engine (The Beast)
        Equation: y(k+1) = 1.5*y - 0.5*y^3 + u
        """
        if self.done:
            raise Exception("Game Over: The craft has already crashed. Please reset.")

        # 1. Physics Update (Unstable Dynamics)
        # Note: The '1.5' term creates exponential divergence if not controlled.
        # The '-0.5*y^3' term adds complex nonlinearity.
        y = self.state
        y_next = 1.5 * y - 0.5 * (y**3) + u_control
        
        # 2. Add realistic disturbance (Wind Gust)
        # Random wind hits at step 10 and 20 to test robustness
        if self.time_step == 10: y_next += 0.2
        if self.time_step == 20: y_next -= 0.3

        # 3. Check Crash Conditions
        if abs(y_next) > self.crash_limit:
            self.done = True
            print(f"💥 CRASH! The craft lost control at step {self.time_step}.")
            y_next = np.sign(y_next) * self.crash_limit # Cap for plotting

        # Update
        self.state = y_next
        self.time_step += 1
        self.history.append(self.state)
        
        return self.state, self.done

    def get_history(self):
        return np.array(self.history)
