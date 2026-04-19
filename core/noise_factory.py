import numpy as np
class NoiseFactory:
    def __init__(self, fs=1000):
        self.fs = fs
    def apply_environment(self, signal, env_type='desert'):
        noise = np.random.normal(0, 1.0, len(signal))
        if env_type == 'urban':
            t = np.linspace(0, len(signal)/self.fs, len(signal))
            noise += 5.0 * np.sin(2 * np.pi * 50 * t)
        return signal + noise
