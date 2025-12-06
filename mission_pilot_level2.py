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
import matplotlib
import platform

# --- Auto-Detect Headless Mode (For Pi Zero / SSH Users) ---
if platform.system() == 'Linux' and 'aarch64' not in platform.machine() and 'x86' not in platform.machine():
    matplotlib.use('Agg') # No screen mode
    HEADLESS = True
else:
    HEADLESS = False

import matplotlib.pyplot as plt
from wig_glider_level2 import WIGGliderLevel2

# ==========================================
# 🎮 YOUR MISSION: WRITE THE CONTROLLER HERE
# ==========================================
def my_controller(y_measured, target):
    """
    🎮 MISSION BRIEFING:
    
    You are flying blind in a storm.
    - The sensor 'y_measured' is noisy.
    - The controls behave with a 3-step lag.
    
    Your P-Controller (below) is failing.
    It overreacts to noise and creates a feedback loop of instability.
    
    OBJECTIVE:
    Write a controller that:
    1. Filters out the noise (Don't believe everything the sensor says).
    2. Predicts the future (To handle the delay).
    3. Stabilizes the craft at Altitude = 1.0.
    
    Good luck. You will need it.
    """
    
    # --- DEFAULT: A Naive P-Controller (THIS WILL FAIL) ---
    # Try running this. Watch it shake and crash.
    error = target - y_measured
    
    # High gain amplifies noise -> Crash
    # Low gain is too slow for unstable physics -> Crash
    kp = 0.8 
    u = kp * error
    
    return u
# ==========================================

def run_simulation():
    env = WIGGliderLevel2()
    measurement = env.reset()
    print("🌪️ Launching Level 2: The Stochastic Storm...")
    print("---------------------------------------------")
    
    crashed = False
    
    for t in range(env.max_steps):
        # 1. Ask Pilot for Control
        u = my_controller(measurement, env.target)
        
        # 2. Apply to Physics Engine
        measurement, done = env.step(u)
        
        if done and t < env.max_steps - 1:
            print(f"💥 CRASH! The craft went unstable at step {t}.")
            crashed = True
            break
            
    if not crashed:
        print("✅ SURVIVED! (But was it stable?) Check the graph.")

    # --- VISUALIZATION ---
    true_path, measured_path = env.get_history()
    
    plt.figure(figsize=(10, 6))
    
    # Plot what the sensor saw (The Lie)
    plt.plot(measured_path, 'r.', alpha=0.3, label='Sensor Readings (Noisy)')
    
    # Plot the actual physics (The Truth)
    plt.plot(true_path, 'k-', linewidth=2, label='True Altitude')
    
    # Guidelines
    plt.axhline(env.target, color='g', linestyle='--', linewidth=2, label='Target (1.0)')
    plt.axhline(env.crash_limit, color='r', linestyle=':', label='Crash Limit')
    plt.axhline(-env.crash_limit, color='r', linestyle=':')
    
    plt.title("Level 2 Report: Did you survive the storm?")
    plt.xlabel("Time Steps")
    plt.ylabel("Altitude")
    plt.legend(loc='lower right')
    plt.grid(True, alpha=0.3)
    
    if HEADLESS:
        plt.savefig('level2_result.png')
        print("📸 Graph saved to 'level2_result.png' (Check your file explorer)")
    else:
        plt.show()

if __name__ == "__main__":
    run_simulation()
