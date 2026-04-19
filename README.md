# 🛡️ GhostWhisper-Sim (幽灵低语模拟器)

```text
      .---.
     / | \_\    [ GHOST WHISPER SYSTEM ]
    /  |  \ \   Distance: 64.0 km
   |   |   | |  Target: Locked (Heartbeat Detected)
    \  |  / /   Status: Deep Learning Signal Extraction...
     \ | /_/
      '---'     "If it beats, we will find it."
```

[English](#english) | [中文](#chinese)

---

<a name="english"></a>
## 🌍 English

### 🧬 Scientific Principle: The Physics of Detection
The "Ghost Whisper" system relies on **Quantum Magnetometry** (typically SQUIDs or OPMs) to detect the Magnetocardiogram (MCG) of a human target.

The magnetic field strength $B$ of a human heart (modeled as a magnetic dipole $m$) follows the **Inverse-Cube Law**:
$$B(r) \approx \frac{\mu_0}{4\pi} \frac{m}{r^3}$$
At a distance of **64 km**, the signal is attenuated by a factor of $\approx 2.6 \times 10^{14}$. This project simulates how AI-driven **Blind Source Separation (BSS)** recovers these signals from femtotesla-level noise.

---

<a name="chinese"></a>
## 🇨🇳 中文

### 🧬 科学原理：探测背后的物理学
“幽灵低语”系统依赖于**量子磁力测量技术**（如 SQUIDs 或 OPMs）来探测目标的心磁图 (MCG)。

人体心脏产生的磁场强度 $B$（将其模拟为磁偶极子 $m$）遵循**三次方反比定律**：
$$B(r) \approx \frac{\mu_0}{4\pi} \frac{m}{r^3}$$
在 **64 公里** 的距离上，信号衰减倍数约为 $2.6 \times 10^{14}$。本项目模拟了 AI 驱动的**盲源分离 (BSS)** 如何从皮特斯拉 (fT) 级别的极低信噪比杂讯中恢复这些生命体征。

---

## 🛠️ Quick Start / 快速开始
```bash
pip install -r requirements.txt
streamlit run app.py
```
