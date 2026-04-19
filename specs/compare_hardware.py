import numpy as np

def calculate_max_range(sensitivity_tesla, dipole_moment=1e-6):
    """
    基于三次方反比定律计算理论最大探测距离
    B = (mu_0 / 4pi) * (m / r^3)  => r = ((mu_0 * m) / (4pi * B))^(1/3)
    """
    mu_0 = 4 * np.pi * 1e-7
    r = ((mu_0 * dipole_moment) / (4 * np.pi * sensitivity_tesla)) ** (1/3)
    return r

# 不同等级硬件的灵敏度 (Tesla)
hardware_data = {
    "Smartphone (Hall Effect)": 1e-5,    # 10 microTesla
    "Industrial Fluxgate": 1e-9,        # 1 nanoTesla
    "Commercial OPM (QuSpin)": 1e-14,   # 10 femtoTesla
    "Military Quantum (Rumored)": 1e-18 # 1 attoTesla (Theoretical limit)
}

print("--- Hardware Detection Range Limit (Theoretical) ---")
for name, sensitivity in hardware_data.items():
    range_m = calculate_max_range(sensitivity)
    print(f"{name:25} | Sensitivity: {sensitivity:.1e} T | Range: {range_m:.2f} meters")
