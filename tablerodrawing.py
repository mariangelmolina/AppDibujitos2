import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Page configuration
st.set_page_config(
    page_title="Mariangel's Board",
    page_icon="✨",
    layout="wide"
)

# Title & Subtitle
st.title("Mariangel's Board yay ✨🎨")
st.caption("Crea, dibuja y exprésate con tu paleta favorita")

# Curated Pastel & Aesthetic Color Palette Presets
PALETTE = {
    "Rosa Pastel 🌸": "#FFB7B2",
    "Lila Mágico 🔮": "#C7CEEA",
    "Azul Cielo ☁️": "#B5EAD7",
    "Menta Fresca 🌿": "#E2F0CB",
    "Crema Cálida 🍦": "#FFFFD1",
    "Durazno Dulce 🍑": "#FFDAC1",
    "Blanco Puro 🤍": "#FFFFFF",
    "Noche Oscura 🌙": "#1A202C"
}

with st.sidebar:
    st.header("⚙️ Propiedades del Tablero")
    
    # Canvas Dimensions
    with st.expander("📐 Dimensiones del Tablero", expanded=False):
        canvas_width = st.slider("Ancho (px)", 300, 900, 650, 50)
        canvas_height = st.slider("Alto (px)", 200, 700, 450, 50)
    
    # Drawing Tools Selector
    drawing_mode = st.selectbox(
        "🛠️ Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
        format_func=lambda x: {
            "freedraw": "✏️ Pincel Libre",
            "line": "📏 Línea Recta",
            "rect": "🔲 Rectángulo",
            "circle": "⚪ Círculo",
            "transform": "🖐️ Mover / Seleccionar",
            "polygon": "🔷 Polígono",
            "point": "📍 Punto"
        }.get(x, x)
    )
    
    # Stroke Width
    stroke_width = st.slider('🖋️ Ancho de línea', 1, 40, 8)
    
    st.divider()
    st.header("🎨 Paleta de Colores")
    
    # Preset Color Selector
    selected_preset = st.selectbox("Selecciona un color predefinido:", list(PALETTE.keys()))
    preset_hex = PALETTE[selected_preset]
    
    # Color Pickers
    stroke_color = st.color_picker("Color de trazo", preset_hex)
    bg_color = st.color_picker("Color de fondo", "#FFFFFF")

# Center Canvas Layout
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    canvas_result = st_canvas(
        fill_color="rgba(255, 183, 178, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}_{selected_preset}",
    )
