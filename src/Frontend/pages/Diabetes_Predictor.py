import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(PROJECT_ROOT))

import requests
import streamlit as st

from src.Frontend.config.setting import Settings

settings = Settings()
API_URL = settings.api_url

# ---------------------------------------------------------------------------
# ⚠️ Update this if your home page file has a different name/path.
# ---------------------------------------------------------------------------
HOME_PAGE = "app.py"

st.set_page_config(
    page_title="Dr.ML - Diabetes Prediction",
    page_icon="🩺",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Theme — shared with the landing page (indigo = diabetes accent)
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    :root{
        --bg:#0A0E1A;
        --panel:rgba(255,255,255,0.04);
        --panel-border:rgba(255,255,255,0.08);
        --indigo:#6C7BFF;
        --indigo-dim:rgba(108,123,255,0.12);
        --danger:#E2544F;
        --danger-dim:rgba(226,84,79,0.12);
        --success:#22D3B8;
        --success-dim:rgba(34,211,184,0.12);
        --amber:#F0A857;
        --amber-dim:rgba(240,168,87,0.12);
        --text-primary:#E9EDF5;
        --text-secondary:#8891A7;
    }

    html, body, [class*="css"]{ font-family:'Inter', sans-serif; }

    .stApp{
        background:
            radial-gradient(circle at 10% 0%, rgba(108,123,255,0.08), transparent 42%),
            var(--bg);
    }

    #MainMenu, footer, header{visibility:hidden;}
    .block-container{ padding-top:2rem; max-width:720px; }

    /* ---------------- Back link ---------------- */
    div[data-testid="stPageLink"]{
        padding:0 !important;
        background:transparent !important;
        margin-bottom:0.8rem;
    }
    div[data-testid="stPageLink"] p{
        font-family:'JetBrains Mono', monospace !important;
        font-size:0.78rem !important;
        letter-spacing:0.04em;
        color:var(--text-secondary) !important;
    }
    div[data-testid="stPageLink"]:hover p{ color:var(--indigo) !important; }

    /* ---------------- Hero ---------------- */
    .hero-eyebrow{
        font-family:'JetBrains Mono', monospace;
        font-size:0.72rem;
        letter-spacing:0.18em;
        text-transform:uppercase;
        color:var(--indigo);
        margin-bottom:0.6rem;
        display:flex;
        align-items:center;
        gap:0.5rem;
    }
    .hero-eyebrow::before{
        content:"";
        width:6px; height:6px;
        border-radius:50%;
        background:var(--indigo);
        box-shadow:0 0 8px var(--indigo);
        display:inline-block;
    }
    .hero-title{
        font-family:'Space Grotesk', sans-serif;
        font-weight:700;
        font-size:2.1rem;
        color:var(--text-primary);
        margin:0;
    }
    .hero-sub{
        font-size:0.95rem;
        color:var(--text-secondary);
        margin-top:0.5rem;
    }
    .hero-sub b{ color:var(--text-primary); font-weight:500; }

    /* ---------------- Mini ECG divider ---------------- */
    .ecg-wrap{ margin:1.4rem 0 1.8rem 0; opacity:0.9; }
    .ecg-line{
        stroke:var(--indigo);
        stroke-width:2;
        fill:none;
        stroke-linecap:round;
        stroke-linejoin:round;
        stroke-dasharray:340;
        stroke-dashoffset:340;
        animation:draw 2s ease-out forwards;
        filter:drop-shadow(0 0 4px rgba(108,123,255,0.5));
    }
    @keyframes draw{ to{ stroke-dashoffset:0; } }

    /* ---------------- Form card ---------------- */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(div.form-tag){
        background:var(--panel);
        border:1px solid var(--panel-border) !important;
        border-radius:16px !important;
        padding:0.4rem !important;
        backdrop-filter:blur(12px);
        -webkit-backdrop-filter:blur(12px);
    }

    .section-label{
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        font-size:0.9rem;
        color:var(--text-primary);
        margin:0.4rem 0 0.7rem 0;
        display:flex;
        align-items:center;
        gap:0.5rem;
    }
    .section-label::before{
        content:"";
        width:3px; height:14px;
        background:var(--indigo);
        border-radius:2px;
        display:inline-block;
    }

    div[data-testid="stNumberInput"] label{
        font-size:0.78rem !important;
        color:var(--text-secondary) !important;
        font-weight:500 !important;
    }
    div[data-testid="stNumberInput"] input{
        background:rgba(255,255,255,0.03) !important;
        border:1px solid var(--panel-border) !important;
        border-radius:10px !important;
        color:var(--text-primary) !important;
        font-family:'JetBrains Mono', monospace !important;
    }
    div[data-testid="stNumberInput"] input:focus{
        border-color:var(--indigo) !important;
        box-shadow:0 0 0 1px var(--indigo) !important;
    }
    div[data-testid="stNumberInput"] button{
        background:rgba(255,255,255,0.03) !important;
        border-color:var(--panel-border) !important;
        color:var(--text-secondary) !important;
    }

    /* ---------------- Predict button ---------------- */
    div[data-testid="stButton"] button{
        background:linear-gradient(90deg, var(--indigo), #8A97FF) !important;
        color:#0A0E1A !important;
        border:none !important;
        border-radius:12px !important;
        font-weight:600 !important;
        font-family:'Space Grotesk', sans-serif !important;
        padding:0.7rem 0 !important;
        margin-top:1.4rem !important;
        box-shadow:0 4px 18px rgba(108,123,255,0.25);
        transition:opacity 0.2s ease, transform 0.15s ease;
    }
    div[data-testid="stButton"] button:hover{ opacity:0.9; transform:translateY(-1px); }
    div[data-testid="stButton"] button:active{ transform:translateY(0px); }
    div[data-testid="stButton"] button p{ color:#0A0E1A !important; font-weight:600 !important; }

    /* ---------------- Result panel ---------------- */
    .result-card{
        margin-top:1.8rem;
        background:var(--panel);
        border:1px solid var(--panel-border);
        border-radius:16px;
        padding:1.5rem 1.5rem;
        backdrop-filter:blur(12px);
        -webkit-backdrop-filter:blur(12px);
        animation:fadeUp 0.4s ease-out;
    }
    @keyframes fadeUp{
        from{ opacity:0; transform:translateY(8px); }
        to{ opacity:1; transform:translateY(0); }
    }
    .result-row{
        display:flex;
        justify-content:space-between;
        align-items:center;
        flex-wrap:wrap;
        gap:0.8rem;
    }
    .result-label{
        font-family:'JetBrains Mono', monospace;
        font-size:0.72rem;
        letter-spacing:0.1em;
        text-transform:uppercase;
        color:var(--text-secondary);
    }
    .result-prob{
        font-family:'Space Grotesk', sans-serif;
        font-weight:700;
        font-size:2.1rem;
        color:var(--text-primary);
        margin-top:0.2rem;
    }
    .result-badge{
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        font-size:0.88rem;
        padding:0.5rem 1rem;
        border-radius:999px;
        display:inline-flex;
        align-items:center;
        gap:0.5rem;
    }
    .result-badge::before{
        content:"";
        width:7px; height:7px;
        border-radius:50%;
        display:inline-block;
    }
    .badge-danger{ background:var(--danger-dim); color:var(--danger); border:1px solid rgba(226,84,79,0.3); }
    .badge-danger::before{ background:var(--danger); box-shadow:0 0 6px var(--danger); }
    .badge-success{ background:var(--success-dim); color:var(--success); border:1px solid rgba(34,211,184,0.3); }
    .badge-success::before{ background:var(--success); box-shadow:0 0 6px var(--success); }

    /* ---------------- Risk meter ---------------- */
    .risk-meter{ margin-top:1.3rem; }
    .risk-meter-track{
        width:100%;
        height:8px;
        border-radius:999px;
        background:rgba(255,255,255,0.06);
        overflow:hidden;
    }
    .risk-meter-fill{
        height:100%;
        border-radius:999px;
        transition:width 0.6s ease;
    }
    .risk-meter-labels{
        display:flex;
        justify-content:space-between;
        margin-top:0.4rem;
        font-family:'JetBrains Mono', monospace;
        font-size:0.68rem;
        color:var(--text-secondary);
        letter-spacing:0.06em;
        text-transform:uppercase;
    }

    /* ---------------- Details recap chips ---------------- */
    .recap-title{
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        font-size:0.85rem;
        color:var(--text-primary);
        margin:1.4rem 0 0.7rem 0;
    }
    .recap-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));
        gap:0.55rem;
    }
    .recap-chip{
        background:rgba(255,255,255,0.03);
        border:1px solid var(--panel-border);
        border-radius:10px;
        padding:0.55rem 0.7rem;
    }
    .recap-chip-label{
        font-family:'JetBrains Mono', monospace;
        font-size:0.65rem;
        color:var(--text-secondary);
        letter-spacing:0.05em;
        text-transform:uppercase;
    }
    .recap-chip-value{
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        font-size:0.95rem;
        color:var(--text-primary);
        margin-top:0.15rem;
    }

    .error-box{
        margin-top:1.6rem;
        background:var(--danger-dim);
        border:1px solid rgba(226,84,79,0.3);
        border-radius:10px;
        padding:0.9rem 1.1rem;
        color:var(--text-primary);
        font-size:0.88rem;
    }
    .error-box .caption{
        color:var(--text-secondary);
        font-family:'JetBrains Mono', monospace;
        font-size:0.76rem;
        margin-top:0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------------------------
# Back link + Hero
# ---------------------------------------------------------------------------
st.page_link(HOME_PAGE, label="Dr. ML", icon="🫁")

st.markdown(
    """
    <div class="hero-eyebrow">diabetes model</div>
    <h1 class="hero-title">🩸 Diabetes risk predictor</h1>
    <p class="hero-sub">Enter patient details below and click <b>Predict</b> to get an instant risk read.</p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="ecg-wrap">
        <svg width="100%" height="40" viewBox="0 0 600 40" preserveAspectRatio="none">
            <path class="ecg-line" d="M0,20 L110,20 L130,20 L145,4 L160,34 L175,0 L190,30 L205,20 L230,20 L600,20" />
        </svg>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------------------------
# Form
# ---------------------------------------------------------------------------
with st.container(border=True):
    st.markdown('<div class="form-tag"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">🩺 Vitals</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        glucose = st.number_input("Glucose (mg/dL)", 0, 400, 120)
        blood_pressure = st.number_input("Blood Pressure (mmHg)", 0, 250, 70)
    with col2:
        bmi = st.number_input("BMI", 0.0, 70.0, 28.5)
        skin_thickness = st.number_input("Skin Thickness (mm)", 0, 100, 25)

    st.markdown('<div class="section-label">📋 History</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        pregnancies = st.number_input("Pregnancies", 0, 20, 2)
        insulin = st.number_input("Insulin (mu U/mL)", 0, 900, 80)
    with col4:
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.45)
        age = st.number_input("Age", 1, 120, 35)

    predict_clicked = st.button("🔍 Predict", use_container_width=True)
st.sidebar.write("2")

# ---------------------------------------------------------------------------
# Prediction
# ---------------------------------------------------------------------------
if predict_clicked:
    payload = {
        "disease": "diabetes",
        "features": {
            "Pregnancies": pregnancies,
            "Glucose": glucose,
            "BloodPressure": blood_pressure,
            "SkinThickness": skin_thickness,
            "Insulin": insulin,
            "BMI": bmi,
            "DiabetesPedigreeFunction": dpf,
            "Age": age,
        },
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        st.markdown(
            f"""
            <div class="error-box">
                Unable to reach prediction service.
                <div class="caption">{e}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.stop()

    result = response.json()
    prediction = int(result["prediction"])
    probability = float(result["probability"])

    if prediction == 1:
        badge_class = "badge-danger"
        badge_text = "⚠️ Diabetes"
    else:
        badge_class = "badge-success"
        badge_text = "✅ No diabetes"

    # Risk meter color follows the probability, independent of the binary label
    pct = max(0.0, min(1.0, probability)) * 100
    if probability < 0.33:
        meter_color = "var(--success)"
    elif probability < 0.66:
        meter_color = "var(--amber)"
    else:
        meter_color = "var(--danger)"

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-row">
                <div>
                    <div class="result-label">Diabetes probability</div>
                    <div class="result-prob">{probability:.2f}</div>
                </div>
                <div class="result-badge {badge_class}">{badge_text}</div>
            </div>
            <div class="risk-meter">
                <div class="risk-meter-track">
                    <div class="risk-meter-fill" style="width:{pct:.0f}%; background:{meter_color};"></div>
                </div>
                <div class="risk-meter-labels">
                    <span>Low risk</span>
                    <span>High risk</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="recap-title">Submitted values</div>', unsafe_allow_html=True)
    recap_items = [
        ("Pregnancies", pregnancies),
        ("Glucose", f"{glucose} mg/dL"),
        ("Blood pressure", f"{blood_pressure} mmHg"),
        ("Skin thickness", f"{skin_thickness} mm"),
        ("Insulin", f"{insulin} mu U/mL"),
        ("BMI", bmi),
        ("Pedigree function", dpf),
        ("Age", age),
    ]
    chips_html = "".join(
        f"""<div class="recap-chip">
                <div class="recap-chip-label">{label}</div>
                <div class="recap-chip-value">{value}</div>
            </div>"""
        for label, value in recap_items
    )
    st.markdown(f'<div class="recap-grid">{chips_html}</div>', unsafe_allow_html=True)