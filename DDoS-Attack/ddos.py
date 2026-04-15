import time

def simulate_ddos():
    print("Starting DDoS Simulation...\n")

    for i in range(50):
        print(f"Sending fake request #{i}")
        time.sleep(0.1)

    print("\nTarget overwhelmed (Simulation Complete)")

simulate_ddos()