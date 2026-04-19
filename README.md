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
The human heart's electrical activity generates a weak magnetic field ($10^{-12} \text{ T}$ near the chest). At a distance $r$, the field $B$ is:
$$B(r) \approx \frac{\mu_0}{4\pi} \frac{m}{r^3}$$
Where $m \approx 10^{-6} \text{ A}\cdot\text{m}^2$.

#### 2. Hardware Tiers & Detection Limits (Theoretical)
| Hardware Tier | Sensitivity (Tesla) | Max Range (Human Heart) |
| :--- | :--- | :--- |
| **Smartphone (Hall Effect)** | $10^{-5}$ | $0.02$ meters |
| **Industrial Fluxgate** | $10^{-9}$ | $0.46$ meters |
| **Commercial OPM (QuSpin)** | $10^{-14}$ | $21.5$ meters |
| **Military Quantum (Rumored)** | $10^{-18}$ | $464.2$ meters* |
*Note: Detection at 64km ($B \approx 10^{-22} \text{ T}$) requires extreme **Gradiometer Arrays** and **Stochastic Resonance** AI algorithms to break the standard quantum limit.*

#### 3. Core Hardware Requirements
- **Atomic Vapor Cell**: High-purity Rubidium ($^{87}\text{Rb}$) or Cesium ($^{133}\text{Cs}$) cells.
- **Low-Noise VCSEL**: Vertical-Cavity Surface-Emitting Lasers with $< 100 \text{ kHz}$ linewidth.
- **Magnetic Shielding/Cancellation**: Active 3-axis Helmholtz coils to nullify Earth's magnetic field.
- **Processing**: High-speed FPGA for real-time Blind Source Separation (BSS).

---

<a name="chinese"></a>
## 🇨🇳 中文

### 🧬 技术深度解析：硬件需求与探测极限

#### 1. 磁偶极子衰减定律
人类心脏产生的磁场强度在胸口附近约为 $1 \text{ pT}$。根据三次方反比定律，距离 $r$ 处的场强为：
$$B(r) \approx \frac{\mu_0}{4\pi} \frac{m}{r^3}$$
其中 $m \approx 10^{-6} \text{ A}\cdot\text{m}^2$。

#### 2. 硬件分级与理论探测极限
| 硬件等级 | 灵敏度 (Tesla) | 理论最大距离 (人体心跳) |
| :--- | :--- | :--- |
| **普通手机 (霍尔感应)** | $10^{-5}$ | $0.02$ 米 |
| **工业级磁通门** | $10^{-9}$ | $0.46$ 米 |
| **民用量子级 (OPM)** | $10^{-14}$ | $21.5$ 米 |
| **军用绝密级 (Rumored)** | $10^{-18}$ | $464.2$ 米* |
*注：在 64 公里外探测 ($B \approx 10^{-22} \text{ T}$) 需要极其庞大的**梯度计阵列 (Gradiometer Array)** 和**随机共振 (Stochastic Resonance)** 算法来突破标准量子极限。*

#### 3. 核心物理设备清单
- **原子蒸气室 (Vapor Cell)**: 高纯度铷 ($^{87}\text{Rb}$) 或铯 ($^{133}\text{Cs}$) 蒸汽室。
- **低噪声 VCSEL 激光器**: 谱宽小于 $100 \text{ kHz}$ 的垂直腔面发射激光器。
- **磁场抵消系统**: 主动式三轴赫姆霍兹线圈 (Helmholtz Coils)，用于实时抵消地磁场。
- **实时处理单元**: 基于 FPGA 的超低延迟盲源分离 (BSS) 信号处理单元。

---

## 🛠️ Quick Start / 快速开始
```bash
pip install -r requirements.txt
streamlit run app.py
```

