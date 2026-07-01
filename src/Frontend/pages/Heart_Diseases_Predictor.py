import os
import requests
from dotenv import load_dotenv
import streamlit as st

# ----------------------------------------------------------------------------
# Configuration & Environment
# ----------------------------------------------------------------------------
load_dotenv()
API_URL = os.getenv("API_URL")

st.set_page_config(
    page_title="MedBuddy.ML | Heart Disease Risk Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Custom CSS — Color palette, cards, buttons, typography
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        /* ---------- Global: dark, professional clinical theme ---------- */
        .stApp {
            background: radial-gradient(circle at 20% 0%, #16202e 0%, #0e1620 55%, #0a0f17 100%);
            color: #dde4ee;
        }
        html, body, [class*="css"] {
            font-family: 'Segoe UI', 'Inter', -apple-system, sans-serif;
        }

        /* Default text & widget label color for dark background */
        .stMarkdown, .stText, label, p, span {
            color: #c7d0e0;
        }
        h1, h2, h3, h4, h5 { color: #f1f4f9; }

        /* Number / select input boxes */
        .stNumberInput input, .stSelectbox div[data-baseweb="select"] > div {
            background-color: #1b2734 !important;
            color: #f1f4f9 !important;
            border: 1px solid #2e3d4f !important;
            border-radius: 8px !important;
        }
        .stSelectbox div[data-baseweb="select"] svg { color: #c7d0e0 !important; }

        /* ---------- Hero header ---------- */
        .hero-container {
            background: linear-gradient(135deg, #0f2a44 0%, #16456e 55%, #1c5d92 100%);
            padding: 2.2rem 2rem;
            border-radius: 16px;
            margin-bottom: 1.8rem;
            border: 1px solid #25496b;
            box-shadow: 0 8px 28px rgba(0, 0, 0, 0.45);
        }
        .hero-title {
            color: #ffffff;
            font-size: 2.1rem;
            font-weight: 800;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }
        .hero-subtitle {
            color: #c7dcf2;
            font-size: 1.05rem;
            margin-top: 0.4rem;
            font-weight: 400;
        }
        .hero-badge {
            display: inline-block;
            background: rgba(255,255,255,0.12);
            color: #eaf2fb;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.78rem;
            margin-top: 0.8rem;
            border: 1px solid rgba(255,255,255,0.25);
        }

        /* ---------- Section cards ---------- */
        .section-card {
            background: #131d29;
            padding: 1.4rem 1.5rem 0.6rem 1.5rem;
            border-radius: 14px;
            border: 1px solid #233040;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            margin-bottom: 1.2rem;
        }
        .section-heading {
            font-size: 1.05rem;
            font-weight: 700;
            color: #7fb4e8;
            margin-bottom: 0.6rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            border-bottom: 1px solid #233040;
            padding-bottom: 0.5rem;
        }

        /* ---------- Buttons ---------- */
        div.stButton > button {
            background: linear-gradient(135deg, #1c5d92 0%, #2f8fd1 100%);
            color: white;
            font-weight: 700;
            font-size: 1.05rem;
            padding: 0.7rem 0;
            border-radius: 10px;
            border: none;
            width: 120%;
            box-shadow: 0 4px 16px rgba(47, 143, 209, 0.35);
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }
        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(47, 143, 209, 0.5);
            color: white;
            border: none;
        }

        /* ---------- Result cards ---------- */
        .result-card-high {
            background: linear-gradient(135deg, #2c1518 0%, #341a1a 100%);
            border-left: 6px solid #e15b56;
            padding: 1.3rem 1.5rem;
            border-radius: 12px;
            margin-top: 0.5rem;
            border-top: 1px solid #3a2024;
            border-right: 1px solid #3a2024;
            border-bottom: 1px solid #3a2024;
        }
        .result-card-low {
            background: linear-gradient(135deg, #102420 0%, #122b24 100%);
            border-left: 6px solid #3fbd7a;
            padding: 1.3rem 1.5rem;
            border-radius: 12px;
            margin-top: 0.5rem;
            border-top: 1px solid #1c3b32;
            border-right: 1px solid #1c3b32;
            border-bottom: 1px solid #1c3b32;
        }
        .result-title {
            font-size: 1.25rem;
            font-weight: 800;
            margin-bottom: 0.3rem;
        }
        .result-title-high { color: #f0837e; }
        .result-title-low { color: #6fd6a0; }

        .result-sub {
            color: #b6c0d1;
            font-size: 0.95rem;
        }

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {
            background: #0c141e;
            border-right: 1px solid #1f2b3a;
        }
        section[data-testid="stSidebar"] * {
            color: #cdd8e8 !important;
        }

        /* ---------- Footer note / disclaimer ---------- */
        .disclaimer-box {
            background: #241f0f;
            border: 1px solid #4a3f1c;
            border-radius: 10px;
            padding: 0.8rem 1rem;
            font-size: 0.85rem;
            color: #e3c878;
            margin-top: 1rem;
        }

        /* ---------- Metric & caption tweaks ---------- */
        div[data-testid="stMetric"] {
            background: #131d29;
            border: 1px solid #233040;
            border-radius: 12px;
            padding: 0.8rem 1rem;
        }
        div[data-testid="stMetricLabel"] { color: #9aaac1 !important; }
        div[data-testid="stMetricValue"] { color: #f1f4f9 !important; }
        .stCaption, [data-testid="stCaptionContainer"] { color: #6b7a90 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Sidebar — Branding, instructions, disclaimer
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 💗 MedBuddy.ML")
    st.markdown("##### AI-Powered Heart Risk Assessment")
    st.markdown("---")
    st.markdown(
        """
        **How it works:**
        1. Fill in the patient's clinical details
        2. Click **Predict Risk**
        3. Review the AI-generated risk assessment

        This tool uses a trained machine learning
        model to estimate the likelihood of heart
        disease based on standard cardiac diagnostic
        indicators.
        """
    )
    st.markdown("---")
    st.markdown(
        """
        <div class="disclaimer-box">
        ⚠️ <b>Disclaimer:</b> The predictions generated by this application
        are based on machine learning models and should be used for informational
        purposes only.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# Hero Header
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero-container">
        <h3 class="hero-title">🫀 MedBuddy.ML</h3>
        <p class="hero-subtitle">AI-Powered Heart Disease Risk Predictor — clinical-grade insights, instantly.</p>
        <span class="hero-badge">🤖 Machine Learning Model</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "##### 📋 Enter the patient's clinical details below, then click **Predict Risk** to generate an assessment."
)
st.write("")

# ----------------------------------------------------------------------------
# Input Form — grouped into clear clinical sections
# ----------------------------------------------------------------------------

# --- Section 1: Demographics & Basic Vitals ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<p class="section-heading">🧑‍⚕️ Demographics &amp; Basic Vitals</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age (years)", 1, 120, 52)
    sex_label = st.selectbox("Sex", ["Male", "Female"])
    sex = 1 if sex_label == "Male" else 0

with col2:
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 0, 250, 125)
    chol = st.number_input("Cholesterol (mg/dl)", 0, 600, 212)

with col3:
    fbs_label = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["No", "Yes"])
    fbs = 1 if fbs_label == "Yes" else 0
    thalach = st.number_input("Max Heart Rate Achieved (thalach)", 0, 250, 168)

st.markdown('</div>', unsafe_allow_html=True)

# --- Section 2: Cardiac Symptoms & ECG ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<p class="section-heading">📈 Cardiac Symptoms &amp; ECG Results</p>', unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    cp = st.number_input("Chest Pain Type (cp) [0–3]", 0, 3, 0)
    restecg = st.number_input("Resting ECG Result (restecg) [0–2]", 0, 2, 1)

with col5:
    exang_label = st.selectbox("Exercise-Induced Angina?", ["No", "Yes"])
    exang = 1 if exang_label == "Yes" else 0
    oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 10.0, 1.0)

with col6:
    slope = st.number_input("Slope of Peak Exercise ST [0–2]", 0, 2, 2)

st.markdown('</div>', unsafe_allow_html=True)

# --- Section 3: Advanced Diagnostic Indicators ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<p class="section-heading">🔬 Advanced Diagnostic Indicators</p>', unsafe_allow_html=True)

col7, col8 = st.columns(2)

with col7:
    ca = st.number_input("Number of Major Vessels Colored (ca) [0–4]", 0, 4, 0)

with col8:
    thal = st.number_input("Thalassemia (thal) [0–3]", 0, 3, 2)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------------------------------
# Predict button & API call (core logic unchanged)
# ----------------------------------------------------------------------------
predict_clicked = st.button("🔍 Predict Risk")

if predict_clicked:
    input_data = {
        "disease": "heart_diseases",
        "features": {
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal,
        },
    }

    try:
        with st.spinner("Analyzing patient data with the ML model..."):
            response = requests.post(API_URL, json=input_data)

        if response.status_code != 200:
            st.error("⚠️ Something went wrong... Try again later.")

        else:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]
            # diagnosis = result["diagnosis"]

            st.divider()
            st.markdown("### 🧾 Prediction Result")

            res_col1, res_col2 = st.columns([1, 2])

            with res_col1:
                st.metric(
                    label="Heart Disease Probability",
                    value=f"{probability:.2f}",
                )
                # Probability shown as a visual progress bar (0-1 range assumed)
                try:
                    st.progress(min(max(float(probability), 0.0), 1.0))
                except (TypeError, ValueError):
                    pass

            with res_col2:
                if prediction == 1:
                    st.markdown(
                        f"""
                        <div class="result-card-high">
                            <p class="result-title result-title-high">🚨 diagnosis</p>
                            <p class="result-sub">The model indicates an elevated risk of heart disease
                            based on the provided clinical data. Please consult a cardiologist for a
                            comprehensive evaluation.</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"""
                        <div class="result-card-low">
                            <p class="result-title result-title-low">✅ diagnosis</p>
                            <p class="result-sub">The model indicates a low risk of heart disease based
                            on the provided clinical data. Continue regular checkups and a heart-healthy
                            lifestyle.</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    except requests.exceptions.RequestException:
        st.error("⚠️ Unable to reach the prediction service. Please check your connection or try again later.")

# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
st.write("")
st.divider()
st.caption("MedBuddy.ML © 2026 · Powered by Machine Learning ·created by Kaushal Kumar .")