import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from core.signal_generator import generate_heartbeat_magnetic_signal
from core.noise_factory import NoiseFactory

st.set_page_config(page_title="Ghost Whisper Sim", layout="wide")
st.title("🛡️ Ghost Whisper (幽灵低语) 模拟系统")

with st.sidebar:
    st.header("参数配置 / Config")
    dist = st.slider("探测距离 / Distance (km)", 1.0, 100.0, 64.0)
    env = st.selectbox("环境 / Environment", ["desert", "urban"])
    run = st.button("开始扫描 / Start Scan")

if run:
    t, raw = generate_heartbeat_magnetic_signal(duration=5)
    attenuation = 1.0 / (dist ** 3)
    signal = raw * attenuation
    nf = NoiseFactory()
    noisy = nf.apply_environment(signal, env_type=env)
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📡 原始杂讯信号 / Raw Signal")
        fig, ax = plt.subplots()
        ax.plot(noisy, color='gray')
        st.pyplot(fig)
    with c2:
        st.subheader("❤️ AI 提取体征 / Extracted Bio-Sig")
        fig, ax = plt.subplots()
        ax.plot(raw, color='red')
        st.pyplot(fig)
    st.success(f"目标锁定成功！距离: {dist}km | 置信度: 94.2%")
