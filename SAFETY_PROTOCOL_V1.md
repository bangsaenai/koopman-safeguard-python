## 🛑 APPENDIX A: SAFETY & FAIL-SAFE ARCHITECTURE (ABET Outcome 4)

**To the Critics concerned about "Flying Projectiles":**
We anticipated your concern. An engineered system is not complete without a definition of failure modes.
Here is the **"Protocol Zero"** Safety Layer embedded in the Iron Man Mark 2-5 architecture:

### 1. The Watchdog (Hardware Level)
We do not trust software. Code can hang. Loops can freeze.
* **Mechanism:** We utilize the **ESP32 Independent Watchdog Timer (IWDT)**.
* **Logic:** If the main Physics Loop (Core 0) fails to "pet the dog" (reset the timer) every **10ms**, the hardware forces an instant **System Reset**.
* **Result:** The PWM signals to servos are cut immediately. The craft becomes inert. It does not "lock" in full throttle. It falls.

### 2. The Kill-Switch (RF Level - Mark 4)
We do not trust autonomy alone.
* **Mechanism:** The **LoRa (SX1278)** module listens on a dedicated interrupt pin.
* **Logic:** A specific encrypted 1-byte payload (`0xFF`) triggers a high-priority interrupt that overrides all flight logic.
* **Result:** **Instant Disarm.** Even if the AI thinks it should fly, the Human Commander has the final veto power from 5km away.

### 3. The Brownout Detector (Power Level)
* **Mechanism:** ESP32 Internal Brownout Detector + INA219 (Mark 5).
* **Logic:** If voltage drops below safe levels (LiPo critical), the system enters **"Glide Mode"** automatically to prevent logic corruption from unstable power.

---
**Summary for Auditors:**
We have implemented a **Defense-in-Depth** strategy.
1.  **Code Freeze?** -> Watchdog kills it.
2.  **AI Rogue?** -> LoRa kills it.
3.  **Battery Die?** -> Brownout saves it.

**We fly fast. But we fail safe.**
