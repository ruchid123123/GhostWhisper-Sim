import numpy as np
def generate_heartbeat_magnetic_signal(duration=10, fs=1000, heart_rate=70):
    t = np.linspace(0, duration, int(duration * fs))
    period = 60.0 / heart_rate
    signal = np.zeros_like(t)
    for i in range(int(duration / period)):
        start = int(i * period * fs)
        if start + 200 < len(signal):
            signal[start:start+50] += 0.2 * np.sin(np.linspace(0, np.pi, 50))
            signal[start+60:start+100] += 1.5 * np.sin(np.linspace(-np.pi, np.pi, 40))
            signal[start+120:start+200] += 0.4 * np.sin(np.linspace(0, np.pi, 80))
    return t, signal
