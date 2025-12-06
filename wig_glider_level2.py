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

class WIGGliderLevel2:
    """
    🌪️ LEVEL 2 PHYSICS ENGINE: "The Stochastic Storm"
    
    This simulation introduces REAL-WORLD CHAOS.
    In Level 1, the world was perfect. In Level 2, the world fights back.
    
    The Equation of Chaos:
    x(k+1) = 1.5*x(k) - 0.5*x(k)^3 + u(k-3) + w(k)
    y(k)   = x(k) + v(k)
    
    The 3 Enemies of Control:
    1. Process Noise (w): Wind gusts that push the craft randomly.
    2. Measurement Noise (v): Your sensors lie. You never know the true altitude.
    3. Input Delay (tau=3): You command the flaps, but they react 3 steps later.
    
    Warning: Standard PID derivatives will amplify noise. High gains will cause oscillation due to lag.
    """
    
    def __init__(self):
        self.state = 0.1 # Initial state (Near unstable equilibrium)
        self.target = 1.0 # Safe altitude
        self.crash_limit = 2.0
        
        self.time_step = 0
        self.max_steps = 300 # Longer flight to test stability over time
        
        # --- CHALLENGE PARAMETERS ---
        self.input_delay = 3      # INCREASED DELAY (Makes PID very unstable)
        self.wind_intensity = 0.05
        self.sensor_noise = 0.05
        
        # Buffer for simulating Delay (Queue)
        self.u_buffer = [0.0] * (self.input_delay + 1)
        
        # History
        self.history_true = [self.state]
        self.history_measured = [self.state]
        self.done = False

    def reset(self):
        self.state = 0.1
        self.time_step = 0
        self.u_buffer = [0.0] * (self.input_delay + 1)
        self.history_true = [self.state]
        self.history_measured = [self.state]
        self.done = False
        # Return initial noisy measurement
        return self.state + np.random.normal(0, self.sensor_noise)

    def step(self, u_command):
        if self.done: return 0, True

        # 1. Manage Input Delay (The "Lag" Trap)
        # Push new command, Pop old command
        self.u_buffer.append(u_command)
        u_applied = self.u_buffer.pop(0)

        # 2. Process Noise (The "Wind" Trap)
        # Continuous turbulence + Random strong gusts
        wind = np.random.normal(0, self.wind_intensity) 
        if np.random.rand() < 0.02: # 2% chance of a violent gust
            wind += np.random.choice([-0.3, 0.3])

        # 3. Physics Update (Unstable Nonlinear)
        y = self.state
        # The equation that kills linear control at y=0
        y_next = 1.5 * y - 0.5 * (y**3) + u_applied + wind

        # Check Crash Conditions
        if abs(y_next) > self.crash_limit:
            self.done = True
            y_next = np.sign(y_next) * self.crash_limit # Cap for plot visualization

        self.state = y_next
        self.history_true.append(self.state)

        # 4. Measurement Noise (The "Sensor" Trap)
        measured_y = y_next + np.random.normal(0, self.sensor_noise)
        self.history_measured.append(measured_y)
        
        self.time_step += 1
        if self.time_step >= self.max_steps:
            self.done = True

        return measured_y, self.done

    def get_history(self):
        return np.array(self.history_true), np.array(self.history_measured)
