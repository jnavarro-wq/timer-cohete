import streamlit as st
import time

%%writefile C:/Users/Jorge/app_cohete.py
import streamlit as st
import time

# --- CONFIGURACIÓN VISUAL ---
st.set_page_config(page_title="Timer Calma 🌿", page_icon="🌿", layout="centered")

# Estilo visual limpio y botones verdes
st.markdown("""
    <style>
    .big-font { font-size:80px !important; text-align: center; color: #6aa84f; font-weight: bold; font-family: sans-serif; }
    .stButton>button { width: 100%; background-color: #6aa84f; color: white; height: 60px; font-size: 20px; border-radius: 15px; border: none;}
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 Tiempo de Calma")

# --- MENÚ LATERAL ---
st.sidebar.header("⚙️ Configuración")
minutos = st.sidebar.number_input("Minutos", min_value=0, max_value=60, value=5)
segundos = st.sidebar.number_input("Segundos", min_value=0, max_value=59, value=0)
tiempo_total = (minutos * 60) + segundos

# --- INTERFAZ PRINCIPAL ---
if tiempo_total == 0:
    st.info("Configura el tiempo a la izquierda.")
else:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        iniciar = st.button("¡Iniciar Tiempo! ⏳")

    if iniciar:
        # 1. CONTENEDOR PARA MÚSICA DE FONDO
        # Usamos st.empty() para poder borrar la música cuando termine el tiempo
        contenedor_musica = st.empty()
        
        # URL de Piano Suave (MP3 directo)
        url_piano = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"
        
        with contenedor_musica:
             # Inyectamos audio HTML invisible que se reproduce solo (autoplay) y se repite (loop)
             st.markdown(f"""
                <audio autoplay loop>
                    <source src="{url_piano}" type="audio/mp3">
                </audio>
                """, unsafe_allow_html=True)

        # 2. CUENTA REGRESIVA
        placeholder_reloj = st.empty()
        barra = st.progress(100)
        mensaje = st.empty()
        
        for t in range(tiempo_total, -1, -1):
            mins, secs = divmod(t, 60)
            reloj_fmt = f"{mins:02d}:{secs:02d}"
            
            progreso = t / tiempo_total
            barra.progress(progreso)
            placeholder_reloj.markdown(f'<p class="big-font">{reloj_fmt}</p>', unsafe_allow_html=True)
            
            # Mensajes de refuerzo positivo
            if progreso > 0.5: mensaje.success("🌟 Respiramos profundo...")
            elif progreso > 0.2: mensaje.warning("🍃 Seguimos tranquilos...")
            elif progreso > 0: mensaje.info("🍂 Ya casi terminamos...")
            
            time.sleep(1)
            
        # 3. DETENER MÚSICA DE FONDO
        # Al vaciar el contenedor, la música de piano se corta inmediatamente.
        contenedor_musica.empty()

        # 4. SONIDO FINAL (Campanita)
        st.balloons()
        mensaje.success("✨ ¡Tiempo Terminado!")
        
        # Usamos st.audio nativo con autoplay para asegurar que suene el final
        # URL de Efecto de sonido 'Success' (MP3)
        st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3", format="audio/mp3", autoplay=True)