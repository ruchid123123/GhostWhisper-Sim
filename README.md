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

### 🧬 Technical Deep Dive: The Physics of Bio-Magnetism

#### 1. The Magnetic Dipole Model
The human heart's electrical activity (depolarization and repolarization) generates a weak magnetic field called the **Magnetocardiogram (MCG)**. In long-range detection, the heart is modeled as a **Magnetic Dipole ($m$)**.
The magnetic flux density $B$ at a distance $r$ is given by:
$$B(r) \approx \frac{\mu_0}{4\pi} \frac{m}{r^3}$$
Where:
- $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$ (Permeability of free space)
- $m \approx 10^{-6} \text{ A}\cdot\text{m}^2$ (Human heart dipole moment)

#### 2. The Quantum Advantage
Standard Hall-effect sensors or fluxgates have a noise floor of $\sim 10^{-9} \text{ T}$. 
"Ghost Whisper" utilizes **Optically Pumped Magnetometers (OPMs)** or **SQUIDs**, reaching sensitivities of:
- **OPM Sensitivity**: $\sim 1 \text{ fT}/\sqrt{\text{Hz}}$ ($10^{-15} \text{ T}$)
- **Environmental Noise**: Earth's magnetic field is $\sim 50 \text{ }\mu\text{T}$. 

**The Challenge:** Extracting a $10^{-15} \text{ T}$ signal from a $10^{-5} \text{ T}$ noisy background—a Signal-to-Noise Ratio (SNR) of **-200 dB**.

---

<a name="chinese"></a>
## 🇨🇳 中文

### 🧬 技术深度解析：生物磁学物理原理

#### 1. 磁偶极子模型
人类心脏的电活动（去极化和复极化）会产生微弱的磁场，称为**心磁图 (MCG)**。在远距离探测中，心脏被抽象为一个**磁偶极子 ($m$)**。
距离 $r$ 处的磁感应强度 $B$ 由下式给出：
$$B(r) \approx \frac{\mu_0}{4\pi} \frac{m}{r^3}$$
其中：
- $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$ (真空磁导率)
- $m \approx 10^{-6} \text{ A}\cdot\text{m}^2$ (人类心脏磁矩)

#### 2. 量子探测优势
普通的霍尔传感器或磁通门传感器的噪声底噪约为 $10^{-9} \text{ T}$。
“幽灵低语”利用了**光泵磁力计 (OPMs)** 或 **超导量子干涉仪 (SQUIDs)**，探测灵敏度可达：
- **OPM 灵敏度**: $\sim 1 \text{ fT}/\sqrt{\text{Hz}}$ ($10^{-15} \text{ T}$)
- **环境背景**: 地磁场约为 $50 \text{ }\mu\text{T}$。

**核心挑战：** 从 $10^{-5} \text{ T}$ 的强地磁背景中提取 $10^{-15} \text{ T}$ 的极微弱信号，其信噪比 (SNR) 低至 **-200 dB**。本项目模拟了如何通过 AI 模式识别来解决这一极端难题。

---

## 🛠️ Quick Start / 快速开始
```bash
pip install -r requirements.txt
streamlit run app.py
```

