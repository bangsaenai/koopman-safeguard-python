import numpy as np
import matplotlib.pyplot as plt
from wig_glider import WIGGlider

# --- YOUR MISSION START HERE ---
def my_controller(current_state, target):
    """
    TODO: Write your control logic here!
    You can use PID, LQR, MPC, Neural Networks, or Magic.
    Input: Current State (y)
    Output: Control Action (u)
    """
    
    # Example 1: Doing Nothing (Passive) -> WILL CRASH
    # u = 0 
    
    # Example 2: Simple Proportional Controller (Try tuning this!)
    error = target - current_state
    kp = 0.1 # <--- Change this. Can you find a value that works?
    u = kp * error
    
    # --- PRO TIP: The system is NONLINEAR. Linear controllers might fail. ---
    
    return u
# -------------------------------

# --- SIMULATION LOOP (DO NOT CHANGE) ---
def run_simulation():
    env = WIGGlider()
    state = env.reset()
    print("🚀 Launching WIG Craft...")
    
    control_effort = 0
    
    for t in range(env.max_steps):
        # Call your controller
        u = my_controller(state, env.target)
        
        # Apply to plant
        state, crashed = env.step(u)
        control_effort += u**2
        
        if crashed:
            break
            
    # Results
    if not crashed:
        final_error = abs(state - env.target)
        print(f"✅ SUCCESS! Mission Complete.")
        print(f"   Final Error: {final_error:.4f}")
        print(f"   Fuel Used (Effort): {control_effort:.4f}")
    else:
        print("❌ MISSION FAILED.")

    # Visualization
    history = env.get_history()
    plt.figure(figsize=(10,5))
    plt.plot(history, 'b.-', label='Trajectory', linewidth=2)
    plt.axhline(env.target, color='g', linestyle='--', label='Target (Safe)')
    plt.axhline(env.crash_limit, color='r', linestyle=':', label='Crash Limit')
    plt.axhline(-env.crash_limit, color='r', linestyle=':')
    plt.title("Mission Report: WIG Craft Stability")
    plt.xlabel("Time Steps")
    plt.ylabel("State")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_simulation()
