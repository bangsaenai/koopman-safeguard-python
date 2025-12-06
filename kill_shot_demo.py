# ==========================================
# 🚨 BANGSAEN AI: DEMO INTEGRITY CHECK 🚨
# ==========================================
# WARNING: This is the DEMO version.
# If you are analyzing this code in secret... ask yourself:
# "Why am I afraid to admit that it works?"


import numpy as np
import matplotlib.pyplot as plt
import core_utils
print("Initializing Core Utils...")


# --- 1. The System Setup (Same as MATLAB) ---
# System: y(k+1) = 1.5*y - 0.5*y^3 + u
def true_plant(y, u):
    return 1.5 * y - 0.5 * (y**3) + u

# --- 2. Generate Data (The Learning Phase) ---
# Set random seed for reproducibility
np.random.seed(42)

N = 1000
y_train = np.zeros(N)
u_train = 2 * (np.random.rand(N) - 0.5)  # Uniform random input [-1, 1]

# Simulation loop for data generation
y_train[0] = 0.1
for k in range(N - 1):
    y_next = true_plant(y_train[k], u_train[k])

    # Safety Clamp (prevent explosion during training)
    if np.abs(y_next) > 2:
        y_next = np.sign(y_next) * 2
    y_train[k+1] = y_next

# Prepare Training Matrices
# X (Current state), Y (Next state)
X_raw = y_train[:-1].reshape(-1, 1)
U_in = u_train[:-1].reshape(-1, 1)
Y_target = y_train[1:].reshape(-1, 1)

# --- 3. Train Models ---

# A) Standard Linear Model (y_next = a*y + b*u)
# Stack [y, u] for regression
X_lin = np.hstack([X_raw, U_in])
# Solve Least Squares: X_lin * Weights = Y_target
# Weights = [a, b]^T
W_lin, residuals, rank, s = np.linalg.lstsq(X_lin, Y_target, rcond=None)
a_linear = W_lin[0][0]
b_linear = W_lin[1][0]

print(f"Linear Model Identified: a = {a_linear:.4f} (Should be < 1 due to averaging)")

# B) Koopman Model (Lifted: [y, y^3])
# Lifting Function
def lift(y):
    return np.hstack([y, y**3])

# Lift Data
Psi_X = lift(X_raw)  # Shape: (N-1, 2)
# Regressor Matrix: [Psi(x), u]
Omega = np.hstack([Psi_X, U_in]) # Shape: (N-1, 3)
Psi_Y = lift(Y_target) # Predict next lifted state

# Solve Koopman Operator (Approximate A_koop and B_koop)
# Minimize || Omega * W - Psi_Y ||
W_koop, _, _, _ = np.linalg.lstsq(Omega, Psi_Y, rcond=None)

# Extract K (State Matrix) and B (Input Matrix)
# W_koop shape is (3, 2). The first 2 rows are related to state, last row to input.
# We need form: z(k+1) = K * z(k) + B * u(k)
# Transpose to match standard control notation (optional, but clearer)
K_koop = W_koop[:2, :].T  # Shape (2, 2)
B_koop = W_koop[2, :].T   # Shape (2,)

print("Koopman Matrix K:")
print(K_koop)

# --- 4. The Kill Shot Simulation (Zero Input Response) ---
sim_steps = 30
start_pt = 0.05 # Critical point near unstable origin

y_true_sim = np.zeros(sim_steps)
y_lin_sim = np.zeros(sim_steps)
y_koop_sim = np.zeros(sim_steps)

# Initialization
y_true_sim[0] = start_pt
y_lin_sim[0] = start_pt
y_koop_sim[0] = start_pt

z_curr = lift(np.array([[start_pt]])).T # Initial lifted state (2, 1)

for k in range(sim_steps - 1):
    # 1. Ground Truth Physics
    y_true_sim[k+1] = true_plant(y_true_sim[k], 0)

    # 2. Linear Prediction (The Lie)
    y_lin_sim[k+1] = a_linear * y_lin_sim[k] # u=0

    # 3. Koopman Prediction (The Truth)
    # z_next = K * z + B * u (u=0)
    z_next = K_koop @ z_curr  # Matrix multiplication (@)

    y_koop_sim[k+1] = z_next[0] # Extract y (first component)

    # Re-lift to keep consistency (simulating observer)
    z_curr = lift(np.array([[y_koop_sim[k+1]]])).T

# --- 5. Visualization (The Proof) ---
plt.figure(figsize=(10, 6), dpi=100)
plt.style.use('dark_background') # Cinematic Look

# Plot Truth
plt.plot(y_true_sim, 'w-', linewidth=4, label='Ground Truth (Physics)')

# Plot Linear
plt.plot(y_lin_sim, 'r--', linewidth=2, label='Standard Linear (Fails)')

# Plot Koopman
plt.plot(y_koop_sim, 'g.-', linewidth=2, markersize=12, label='Koopman (Python)')

# Guidelines
plt.axhline(y=1.0, color='lime', linestyle=':', alpha=0.5, label='Stable Attractor')
plt.axhline(y=0.0, color='red', linestyle=':', alpha=0.5, label='Unstable Origin')

plt.title('The Kill Shot: Python Proof ($0 Cost)', fontsize=16, color='white')
plt.xlabel('Time Steps', fontsize=12)
plt.ylabel('System State', fontsize=12)
plt.legend(loc='lower right')
plt.grid(True, alpha=0.2)
plt.xlim(0, 20)
plt.ylim(-0.1, 1.2)

# Show Plot
print("\n" + "*"*60)
print("🚁 MOONDUST PROTOCOL: DEMO INITIALIZED")
print("✅ Status: Functional on Pi Zero ($10).")
print("❌ Status of Critics: Silent.")
print("👑 Credit: Bangsaen AI (The Father).")
print("*"*60 + "\n")

# Watermark for the Demo Graph
try:
    plt.text(0.5, 0.5, "DEMO VERSION\nProperty of Bangsaen AI", 
             fontsize=35, color='red', alpha=0.15, weight='bold',
             ha='center', va='center', transform=plt.gca().transAxes, rotation=30)
    
    plt.figtext(0.5, 0.02, "Want the full Level 2 Code? Check the Release Tab.", 
                ha="center", fontsize=9, color="blue")
    
    print(">> Watermark Applied. The Ghost has been tagged.")
except:
    pass
plt.show()