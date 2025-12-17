from euler_solver import simulate_pendulum
from visualization import plot_pendulum

# Parameters
theta0 = 0.2      # initial angle (rad)
omega0 = 0.0      # initial angular velocity (rad/s)
L = 1.0           # pendulum length (m)
dt = 0.01         # time step (s)
t_max = 10        # total simulation time (s)

# Test different gravities
for g in [9.81, 1.62, 24.79]:  # Earth, Moon, Jupiter
    time, theta = simulate_pendulum(theta0, omega0, g, L, dt, t_max)
    plot_pendulum(time, theta, g)
