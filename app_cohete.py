import streamlit as st
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Timer Cohete 🚀", page_icon="🚀", layout="centered")

# Estilo CSS para que se vea grande y bonito para niños
st.markdown("""
    <style>
    .big-font {
        font-size:80px !important;
        text-align: center;
        color: #FF4B4B;
        font-weight: bold;
        font-family: sans-serif;
    }
    .stButton>button {
        width: 100%;
        background-color: #0099ff;
        color: white;
        height: 60px;
        font-size: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TÍTULO ---
st.title("🚀 Misión: Control de Tiempo")
st.markdown("---")

# --- BARRA LATERAL (CONFIGURACIÓN) ---
st.sidebar.header("⚙️ Configuración")
minutos = st.sidebar.number_input("Minutos", min_value=0, max_value=60, value=5)
segundos = st.sidebar.number_input("Segundos", min_value=0, max_value=59, value=0)
tiempo_total = (minutos * 60) + segundos

# --- INTERFAZ PRINCIPAL ---
if tiempo_total == 0:
    st.warning("⚠️ Por favor, pon tiempo en el menú de la izquierda.")
else:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        iniciar = st.button("¡INICIAR DESPEGUE! 🚀")

    if iniciar:
        placeholder_reloj = st.empty()
        barra = st.progress(100)
        mensaje = st.empty()
        
        for t in range(tiempo_total, -1, -1):
            # Calcular minutos y segundos
            mins, secs = divmod(t, 60)
            reloj_fmt = f"{mins:02d}:{secs:02d}"
            
            # Actualizar barra y números
            progreso = t / tiempo_total
            barra.progress(progreso)
            placeholder_reloj.markdown(f'<p class="big-font">{reloj_fmt}</p>', unsafe_allow_html=True)
            
            # Mensajes divertidos
            if progreso > 0.5:
                mensaje.info("🟢 Todo tranquilo en el espacio...")
            elif progreso > 0.2:
                mensaje.warning("🟠 ¡Atención! Se acaba el combustible...")
            elif progreso > 0:
                mensaje.error("🔴 ¡Aterrizaje inminente!")
            
            time.sleep(1)
        
        # Al finalizar
        mensaje.success("🏁 ¡EL COHETE HA ATERRIZADO!")
        st.balloons()
