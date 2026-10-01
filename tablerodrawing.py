import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Custom CSS for page styling, pastel colors, and decorative sparkling header
st.markdown(
    """
    <style>
    /* Main Background with soft pastel aesthetic */
    .stApp {
        background-color: #FAF5FF;
    }
    
    /* Decorative Header with glitter beads styling */
    .glitter-header {
        text-align: center;
        font-family: 'Playfair Display', serif;
        color: #7C3AED;
        font-size: 2.5rem;
        padding: 10px;
        background: linear-gradient(90deg, #F3E8FF, #FCE7F3, #E0E7FF);
        border-radius: 15px;
        border: 2px dashed #C084FC;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(192, 132, 252, 0.2);
    }
    
    /* Decorative bead border frame around the main layout */
    .bead-frame {
        border: 3px dotted #A855F7;
        padding: 15px;
        border-radius: 20px;
        background-color: #FFFFFF;
        box-shadow: 0 8px 16px rgba(168, 85, 247, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="glitter-header">✨ ✨ Tablero Mágico de Dibujo ✨ ✨</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("✨ Propiedades y Estilo")
    
    # Preset "Pretty Palette" selection
    st.subheader("🎨 Paletas Predefinidas")
    palette_choice = st.selectbox(
        "Elige un tono favorito:",
        ("Rosa Pastel", "Perla Nacardada", "Lavanda Soñadora", "Menta Fresca", "Oro Rosa", "Personalizado")
    )
    
    # Map palette choices to pretty HEX colors
    palette_colors = {
        "Rosa Pastel": "#FFB7B2",
        "Perla Nacardada": "#FDFBF7",
        "Lavanda Soñadora": "#E2F0CB",
        "Menta Fresca": "#B5EAD7",
        "Oro Rosa": "#E8B4B8",
        "Personalizado": "#FF9AA2"
    }
    
    default_color = palette_colors.get(palette_choice, "#FF9AA2")
    
    st.subheader("📏 Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
    
    # Enhanced drawing modes including "Glitter / Beads" stamp mode
    st.subheader("🛠️ Herramienta")
    selected_tool = st.selectbox(
        "Herramienta de Dibujo:",
        ("Trazo Libre (Pincel)", "Puntos de Brillitos (Glitter/Beads)", "Línea", "Rectángulo", "Círculo", "Mover / Transformar")
    )
    
    # Map friendly names back to fabric.js modes
    mode_mapping = {
        "Trazo Libre (Pincel)": "freedraw",
        "Puntos de Brillitos (Glitter/Beads)": "point",
        "Línea": "line",
        "Rectángulo": "rect",
        "Círculo": "circle",
        "Mover / Transformar": "transform"
    }
    drawing_mode = mode_mapping[selected_tool]
    
    # Stroke width slider
    stroke_width = st.slider('Tamaño del trazo / brillito', 1, 50, 15)
    
    # Stroke color picker initialized to preset palette
    stroke_color = st.color_picker("Color de Trazo / Brillo", default_color)
    
    # Background color
    bg_color = st.color_picker("Color del Lienzo", "#FFFFFF")

# Display the canvas wrapped inside decorative glitter beads container
st.markdown('<div class="bead-frame">', unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="rgba(255, 192, 203, 0.3)",  # Soft translucent fill
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"glitter_canvas_{canvas_width}_{canvas_height}_{palette_choice}",
)

st.markdown('</div>', unsafe_allow_html=True)
