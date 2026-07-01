import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.append(PROJECT_ROOT)

import streamlit as st

st.set_page_config(
    page_title="Dr. ML — Multi-Disease Predictor",
    page_icon="🩺",
    layout="centered"
)

# ---------------------------------------------------------------------------
# ⚠️ Update these to match the actual filenames inside your pages/ folder.
# Streamlit derives page paths from the files it finds there, e.g.
# "pages/1_Diabetes_Predictor.py". Get these wrong and the cards won't navigate.
# ---------------------------------------------------------------------------
DIABETES_PAGE = "pages/Diabetes_Predictor.py"
HEART_PAGE = "pages/Heart_Diseases_Predictor.py"

# ---------------------------------------------------------------------------
# Theme
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    :root{
        --bg:#0A0E1A;
        --panel:rgba(255,255,255,0.04);
        --panel-border:rgba(255,255,255,0.08);
        --teal:#22D3B8;
        --teal-dim:rgba(34,211,184,0.12);
        --indigo:#6C7BFF;
        --indigo-dim:rgba(108,123,255,0.12);
        --amber:#F0A857;
        --text-primary:#E9EDF5;
        --text-secondary:#8891A7;
        --text-muted:#5B6478;
    }

    html, body, [class*="css"]{
        font-family:'Inter', sans-serif;
    }

    .stApp{
        background:
            radial-gradient(circle at 15% 0%, rgba(34,211,184,0.06), transparent 40%),
            radial-gradient(circle at 85% 15%, rgba(108,123,255,0.07), transparent 45%),
            var(--bg);
    }

    #MainMenu, footer, header{visibility:hidden;}

    .block-container{
        padding-top:2.5rem;
        padding-bottom:1rem;
        max-width:760px;
    }

    /* ---------------- Hero ---------------- */
    .hero-eyebrow{
        font-family:'JetBrains Mono', monospace;
        font-size:0.72rem;
        letter-spacing:0.18em;
        text-transform:uppercase;
        color:var(--teal);
        margin-bottom:0.6rem;
        display:flex;
        align-items:center;
        gap:0.5rem;
    }
    .hero-eyebrow::before{
        content:"";
        width:6px;
        height:6px;
        border-radius:50%;
        background:var(--teal);
        box-shadow:0 0 8px var(--teal);
        display:inline-block;
    }
    .hero-title{
        font-family:'Space Grotesk', sans-serif;
        font-weight:700;
        font-size:2.5rem;
        line-height:1.15;
        color:var(--text-primary);
        margin:0;
    }
    .hero-title span{
        background:linear-gradient(90deg, var(--teal), var(--indigo));
        -webkit-background-clip:text;
        background-clip:text;
        color:transparent;
    }
    .hero-sub{
        font-size:1rem;
        color:var(--text-secondary);
        margin-top:0.75rem;
        max-width:520px;
        line-height:1.6;
    }

    /* ---------------- Stack strip ---------------- */
    .stack-strip{
        display:flex;
        flex-wrap:wrap;
        gap:0.5rem;
        margin-top:1.1rem;
    }
    .stack-pill{
        font-family:'JetBrains Mono', monospace;
        font-size:0.7rem;
        letter-spacing:0.03em;
        color:var(--text-secondary);
        background:rgba(255,255,255,0.03);
        border:1px solid var(--panel-border);
        border-radius:999px;
        padding:0.3rem 0.75rem;
        display:inline-flex;
        align-items:center;
        gap:0.4rem;
    }
    .stack-pill .dot{
        width:5px; height:5px;
        border-radius:50%;
        background:var(--teal);
        display:inline-block;
    }

    /* ---------------- ECG signature divider ---------------- */
    .ecg-wrap{
        margin:1.8rem 0 2.2rem 0;
        opacity:0.9;
    }
    .ecg-line{
        stroke:var(--teal);
        stroke-width:2;
        fill:none;
        stroke-linecap:round;
        stroke-linejoin:round;
        stroke-dasharray:340;
        stroke-dashoffset:340;
        animation:draw 2.4s ease-out forwards;
        filter:drop-shadow(0 0 4px rgba(34,211,184,0.5));
    }
    @keyframes draw{
        to{stroke-dashoffset:0;}
    }

    /* ---------------- How it works ---------------- */
    .flow-row{
        display:flex;
        align-items:flex-start;
        margin-bottom:2.1rem;
    }
    .flow-step{
        flex:1;
        display:flex;
        flex-direction:column;
        gap:0.35rem;
    }
    .flow-num{
        font-family:'JetBrains Mono', monospace;
        font-size:0.7rem;
        color:var(--teal);
        letter-spacing:0.05em;
    }
    .flow-label{
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        font-size:0.86rem;
        color:var(--text-primary);
    }
    .flow-desc{
        font-size:0.78rem;
        color:var(--text-muted);
        line-height:1.4;
    }
    .flow-connector{
        flex:0 0 auto;
        width:32px;
        height:1px;
        background:var(--panel-border);
        margin:0 0.6rem;
        margin-top:6px;
    }

    /* ---------------- Predictor cards (clickable via st.page_link) ------- */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(div.card-tag-diabetes),
    div[data-testid="stVerticalBlockBorderWrapper"]:has(div.card-tag-heart){
        background:var(--panel);
        border:1px solid var(--panel-border) !important;
        border-radius:16px !important;
        backdrop-filter:blur(12px);
        -webkit-backdrop-filter:blur(12px);
        transition:border-color 0.2s ease, transform 0.2s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(div.card-tag-diabetes):hover{
        transform:translateY(-2px);
        border-color:var(--indigo) !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(div.card-tag-heart):hover{
        transform:translateY(-2px);
        border-color:var(--teal) !important;
    }

    .card-icon{
        width:38px;
        height:38px;
        border-radius:10px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:1.2rem;
        margin-bottom:0.8rem;
    }
    .card-icon-diabetes{ background:var(--indigo-dim); color:var(--indigo); }
    .card-icon-heart{ background:var(--teal-dim); color:var(--teal); }

    .card-meta{
        font-family:'JetBrains Mono', monospace;
        font-size:0.68rem;
        letter-spacing:0.03em;
        color:var(--text-muted);
        margin-bottom:0.8rem;
    }

    .card-desc{
        font-size:0.86rem;
        color:var(--text-secondary);
        line-height:1.55;
        margin:0.2rem 0 0.4rem 0;
    }

    .card-tag{
        display:inline-block;
        font-family:'JetBrains Mono', monospace;
        font-size:0.66rem;
        letter-spacing:0.03em;
        padding:0.2rem 0.55rem;
        border-radius:6px;
        margin-top:0.6rem;
    }
    .tag-diabetes{ background:var(--indigo-dim); color:var(--indigo); }
    .tag-heart{ background:var(--teal-dim); color:var(--teal); }

    /* Style the page_link itself as the card title + arrow */
    div[data-testid="stPageLink"]{
        padding:0 !important;
        background:transparent !important;
    }
    div[data-testid="stPageLink"] p{
        font-family:'Space Grotesk', sans-serif !important;
        font-weight:600 !important;
        font-size:1.05rem !important;
        color:var(--text-primary) !important;
    }
    div[data-testid="stPageLink"]:hover p{
        color:var(--teal) !important;
    }

    /* ---------------- Status panel ---------------- */
    .status-panel{
        margin-top:1.6rem;
        background:var(--panel);
        border:1px solid var(--panel-border);
        border-left:3px solid var(--amber);
        border-radius:10px;
        padding:0.9rem 1.1rem;
        display:flex;
        align-items:flex-start;
        gap:0.7rem;
    }
    .status-dot{
        width:8px;
        height:8px;
        border-radius:50%;
        background:var(--amber);
        margin-top:0.4rem;
        flex-shrink:0;
        box-shadow:0 0 6px var(--amber);
    }
    .status-text{
        font-size:0.86rem;
        color:var(--text-secondary);
        line-height:1.55;
    }
    .status-text b{
        color:var(--text-primary);
        font-weight:500;
    }
    .status-text code{
        font-family:'JetBrains Mono', monospace;
        font-size:0.78rem;
        background:rgba(255,255,255,0.06);
        padding:0.1rem 0.4rem;
        border-radius:5px;
        color:var(--teal);
    }

    /* ---------------- Footer ---------------- */
    .footer-note{
        margin-top:2.2rem;
        padding-top:1.2rem;
        border-top:1px solid var(--panel-border);
        font-family:'JetBrains Mono', monospace;
        font-size:0.72rem;
        color:var(--text-muted);
        line-height:1.6;
        text-align:center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero-eyebrow">system online</div>
    <h1 class="hero-title">Dr. <span>ML</span></h1>
    <p class="hero-sub">
        A multi-disease risk predictor. Choose a model below and get an
        instant read on your risk profile, powered by models trained on real
        clinical data.
    </p>
    <div class="stack-strip">
        <span class="stack-pill"><span class="dot"></span>FastAPI backend</span>
        <span class="stack-pill"><span class="dot"></span>ML inference</span>
        <span class="stack-pill"><span class="dot"></span>Real-time results</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Signature ECG trace
st.markdown(
    """
    <div class="ecg-wrap">
        <svg width="100%" height="60" viewBox="0 0 600 60" preserveAspectRatio="none">
            <path class="ecg-line" d="M0,30 L110,30 L130,30 L145,10 L160,50 L175,5 L190,45 L205,30 L230,30 L600,30" />
        </svg>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------------------------
# How it works
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="flow-row">
        <div class="flow-step">
            <div class="flow-num">01</div>
            <div class="flow-label">Enter details</div>
            <div class="flow-desc">Fill in clinical markers on either predictor.</div>
        </div>
        <div class="flow-connector"></div>
        <div class="flow-step">
            <div class="flow-num">02</div>
            <div class="flow-label">Model inference</div>
            <div class="flow-desc">The FastAPI backend runs it through the model.</div>
        </div>
        <div class="flow-connector"></div>
        <div class="flow-step">
            <div class="flow-num">03</div>
            <div class="flow-label">Risk score</div>
            <div class="flow-desc">Get a probability and risk read instantly.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------------------------
# Predictor cards — each is a bordered container with a real page_link
# ---------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown('<div class="card-tag-diabetes"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-icon card-icon-diabetes">🩸</div>', unsafe_allow_html=True)
        st.page_link(DIABETES_PAGE, label="Diabetes risk", icon="🫁")
        st.markdown('<div class="card-meta">8 clinical + lifestyle markers</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <p class="card-desc">Estimates diabetes risk from key clinical and lifestyle markers.</p>
            <span class="card-tag tag-diabetes">glucose · BMI · pedigree</span>
            """,
            unsafe_allow_html=True
        )

with col2:
    with st.container(border=True):
        st.markdown('<div class="card-tag-heart"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-icon card-icon-heart">🫀</div>', unsafe_allow_html=True)
        st.page_link(HEART_PAGE, label="Heart disease", icon="💗")
        st.markdown('<div class="card-meta">ECG + lab markers</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <p class="card-desc">Flags cardiovascular risk using standard diagnostic indicators.</p>
            <span class="card-tag tag-heart">cholesterol · ECG · vitals</span>
            """,
            unsafe_allow_html=True
        )

# ---------------------------------------------------------------------------
# Backend status
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="status-panel">
        <div class="status-dot"></div>
        <div class="status-text">
            <strong>Diagnosis Support Tool</strong><br>
            AI-generated risk assessment based on the provided health parameters. Please consult a healthcare professional for an accurate diagnosis and medical advice.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="footer-note">
        Dr. ML v1.0 — predictions are model estimates, not a medical diagnosis.
        Created By <strong>Kaushal Kumar</strong>
    </div>
    """,
    unsafe_allow_html=True
)