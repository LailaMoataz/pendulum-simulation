import matplotlib.pyplot as plt

def plot_pendulum(time, theta, g):
    plt.figure(figsize=(8,5))
    plt.plot(time, theta, label=f"g = {g} m/s²")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (rad)")
    plt.title("Pendulum Motion Simulation")
    plt.legend()
    plt.grid(True)
    plt.show()
