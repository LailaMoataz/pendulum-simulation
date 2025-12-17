import numpy as np

def simulate_pendulum(theta0, omega0, g, L, dt, t_max):
    """
    Simulate a simple pendulum using Euler's method.
    
    theta0 : initial angle (radians)
    omega0 : initial angular velocity (rad/s)
    g      : gravitational acceleration
    L      : length of pendulum
    dt     : time step
    t_max  : maximum time
    """
    n_steps = int(t_max / dt)
    theta = np.zeros(n_steps)
    omega = np.zeros(n_steps)
    time = np.linspace(0, t_max, n_steps)
    
    theta[0] = theta0
    omega[0] = omega0
    
    for i in range(1, n_steps):
        omega[i] = omega[i-1] - (g/L) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i] * dt
        
    return time, theta
