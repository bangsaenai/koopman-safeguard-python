import numpy as np

class WIGGliderLevel2:
    """
    🌪️ The 'Bangsaen Control Benchmark - Level 2' (Stochastic Storm)
    
    Challenger Note:
    This environment simulates a WIG Craft flying in turbulent wind with laggy controls.
    
    Dynamics:
    x(k+1) = 1.5*x(k) - 0.5*x(k)^3 + u(k-tau) + w(k)
    y(k)   = x(k) + v(k)
    
    Where:
    - w(k): Process Noise (Wind Gusts)
    - v(k): Measurement Noise (Sensor Jitter)
    - tau : Input Delay (Lag)
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
