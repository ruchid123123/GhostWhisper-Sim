import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from core.signal_generator import generate_heartbeat_magnetic_signal
from core.noise_factory import NoiseFactory

# --- Physical Constants & Hardware Specs ---
SENSOR_TYPES = {
    "Smartphone (Hall Effect)": 1e-5,    # 10 microTesla
    "Industrial Fluxgate": 1e-9,        # 1 nanoTesla
    "Commercial OPM (QuSpin)": 1e-14,   # 10 femtoTesla
    "Military Quantum (Rumored)": 1e-18 # 1 attoTesla
}

st.set_page_config(page_title="Ghost Whisper Sim v2.0", layout="wide")
st.title("🛡️ Ghost Whisper (幽灵低语) 模拟系统 v2.0")
st.markdown("---")

with st.sidebar:
    st.header("🎛️ 任务配置 / Mission Config")
    sensor_name = st.selectbox("选择探测器类型 / Select Sensor", list(SENSOR_TYPES.keys()))
    dist_km = st.slider("探测距离 / Distance (km)", 0.01, 100.0, 1.0)
    env_type = st.selectbox("环境类型 / Environment", ["Desert (Low Noise)", "Urban (High EMI)"])
    
    st.markdown("---")
    st.info(f"**当前传感器灵敏度:**\n{SENSOR_TYPES[sensor_name]:.1e} Tesla")
    
    run_scan = st.button("🚀 开始扫描 / Execute Scan")

if run_scan:
    # 1. 物理计算：信号衰减
    # 基础心磁场强度约为 1pT (1e-12 T) @ 0.1m
    base_field = 1e-12 
    # 距离衰减 (基于 1/r^3)
    # 计算相对于 0.1m 的比例
    r_ratio = (dist_km * 1000) / 0.1
    attenuation = 1.0 / (r_ratio ** 3)
    signal_strength = base_field * attenuation
    
    # 2. 生成信号与噪声
    t, raw_wave = generate_heartbeat_magnetic_signal(duration=3, fs=500)
    target_signal = raw_wave * (signal_strength / np.max(raw_wave))
    
    # 获取所选传感器的底噪
    noise_floor = SENSOR_TYPES[sensor_name]
    
    # 生成环境噪声 + 传感器底噪
    nf = NoiseFactory(fs=500)
    env_mode = 'urban' if "Urban" in env_type else 'desert'
    # 这里的噪声模型简化为传感器底噪占据主导
    total_noise = np.random.normal(0, noise_floor, len(t))
    
    received_signal = target_signal + total_noise
    
    # 3. 结果判定
    snr = 20 * np.log10(signal_strength / noise_floor)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📡 原始接收波形 / Raw Magnetic Flux")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(t, received_signal, color='gray', alpha=0.7, label="Raw Signal")
        ax.axhline(y=noise_floor, color='blue', linestyle='--', label="Sensor Noise Floor")
        ax.axhline(y=-noise_floor, color='blue', linestyle='--')
        ax.set_ylabel("Field Strength (Tesla)")
        ax.set_xlabel("Time (s)")
        ax.legend()
        st.pyplot(fig)

    with col2:
        st.subheader("❤️ 提取结果 / AI Extraction")
        if snr > -30: # 假设 AI 具备强大的降噪能力，信噪比不低于 -30dB 即可锁定
            st.success(f"✅ **目标已锁定!**")
            st.metric("Signal-to-Noise Ratio (SNR)", f"{snr:.2f} dB")
            st.metric("Estimated Distance", f"{dist_km} km")
            
            fig_ai, ax_ai = plt.subplots(figsize=(10, 4))
            ax_ai.plot(t, raw_wave, color='red', label="Recovered Heartbeat")
            ax_ai.set_ylim(-2, 2)
            ax_ai.legend()
            st.pyplot(fig_ai)
        else:
            st.error(f"❌ **信号已淹没!**")
            st.warning(f"由于探测距离过远或传感器精度不足，信号已完全淹没在噪声中。")
            st.metric("SNR (Critical Low)", f"{snr:.2f} dB")
            
            # 显示一团乱麻
            fig_fail, ax_fail = plt.subplots(figsize=(10, 4))
            ax_fail.plot(t, received_signal / noise_floor, color='black', alpha=0.3)
            ax_fail.set_title("No Periodic Pattern Detected")
            st.pyplot(fig_fail)

    st.markdown("---")
    st.caption("物理模型说明：系统基于磁偶极子 1/r³ 衰减定律。即使是量子传感器，在 1km 外探测心跳也是极具挑战性的。")
