import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import difflib
import textstat
import nltk

# Make sure the syllable-counting data is available (needed by textstat)
try:
    nltk.data.find("corpora/cmudict")
except LookupError:
    nltk.download("cmudict")

st.set_page_config(page_title="Grammar & Fluency Checker", page_icon="✎", layout="centered")

# ---------- Design: an editor's markup on a page ----------
# Palette: near-white paper, ink text, a single red-pen accent for corrections,
# a muted green for the readability verdict. No gradients, no card shadows.
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lora:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, 'Segoe UI', sans-serif;
        color: #2B2B26;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
    }

    .stApp {
        background-color: #FDFBF7;
    }

    .block-container {
        max-width: 700px;
        padding-top: 3rem;
    }

    .masthead {
        background: #1E3A2F;
        padding: 2rem 2.2rem;
        border-radius: 4px;
        margin-bottom: 2.2rem;
    }
    .masthead h1 {
        font-family: 'Lora', Georgia, serif;
        font-weight: 600;
        font-size: 2rem;
        margin: 0;
        letter-spacing: -0.01em;
        color: #FDFBF7;
    }
    .masthead p {
        font-size: 0.95rem;
        color: #C9D6CD;
        margin: 0.5rem 0 0 0;
        max-width: 60ch;
    }

    .stTextArea textarea {
        border-radius: 3px;
        border: 1px solid #E3DDCE;
        font-size: 1.02rem;
        font-family: 'Inter', sans-serif;
        background: #FFFFFF;
    }
    .stTextArea textarea:focus {
        border-color: #1E3A2F;
        box-shadow: none;
    }

    .stButton button {
        background: #C5A880;
        color: #1E3A2F;
        border: none;
        border-radius: 3px;
        padding: 0.55rem 1.4rem;
        font-weight: 600;
        font-size: 0.95rem;
    }
    .stButton button:hover {
        background: #B4966C;
        color: #1E3A2F;
    }

    .section {
        border-top: 1px solid #E7E2D8;
        padding-top: 1.3rem;
        margin-top: 1.6rem;
    }
    .section h4 {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 0.85rem;
        color: #1E3A2F;
        margin: 0 0 0.7rem 0;
    }
    .markup-text {
        font-family: 'Lora', Georgia, serif;
        font-size: 1.12rem;
        line-height: 1.75;
        color: #2B2B26;
    }
    .markup-text del {
        color: #A32638;
        text-decoration: line-through;
        text-decoration-color: #A32638;
    }
    .markup-text ins {
        color: #2F6F4F;
        text-decoration: underline;
        text-decoration-color: #2F6F4F;
        font-style: normal;
    }
    .score-row {
        display: flex;
        align-items: baseline;
        gap: 0.7rem;
    }
    .score-number {
        font-family: 'Lora', Georgia, serif;
        font-size: 2.4rem;
        font-weight: 600;
        line-height: 1;
    }
    .score-label {
        font-size: 0.95rem;
        color: #7A7A6E;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("vennify/t5-base-grammar-correction")
    model = AutoModelForSeq2SeqLM.from_pretrained("vennify/t5-base-grammar-correction")
    return tokenizer, model


tokenizer, model = load_model()


def correct_grammar(text):
    input_text = "grammar: " + text
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=256)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def render_markup(original, corrected):
    """Show corrections inline, like a teacher's tracked-change markup."""
    original_words = original.split()
    corrected_words = corrected.split()
    matcher = difflib.SequenceMatcher(None, original_words, corrected_words)
    pieces = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            pieces.append(" ".join(original_words[i1:i2]))
        elif tag == "delete":
            pieces.append(f'<del>{" ".join(original_words[i1:i2])}</del>')
        elif tag == "insert":
            pieces.append(f'<ins>{" ".join(corrected_words[j1:j2])}</ins>')
        elif tag == "replace":
            pieces.append(f'<del>{" ".join(original_words[i1:i2])}</del> <ins>{" ".join(corrected_words[j1:j2])}</ins>')
    return " ".join(pieces)


# ---------- Header ----------
st.markdown("""
    <div class="masthead">
        <h1>Grammar & Fluency Checker</h1>
        <p>A writing companion built by a former English instructor. Paste a sentence or paragraph below for a line edit and a readability score.</p>
    </div>
""", unsafe_allow_html=True)

user_text = st.text_area(
    "Your writing",
    height=150,
    placeholder="Type or paste your English text here…",
    label_visibility="collapsed",
)

check_clicked = st.button("Check my writing")

if check_clicked:
    if not user_text.strip():
        st.warning("Enter some text first.")
    else:
        with st.spinner("Reading your text…"):
            corrected_text = correct_grammar(user_text)
            fluency_score = textstat.flesch_reading_ease(user_text)

        markup_html = render_markup(user_text, corrected_text)

        st.markdown(f"""
            <div class="section">
                <h4>Line edit</h4>
                <div class="markup-text">{markup_html}</div>
            </div>
        """, unsafe_allow_html=True)

        if fluency_score >= 60:
            verdict = "Easy to read"
            score_color = "#2F6F4F"
        elif fluency_score >= 30:
            verdict = "Moderately easy to read — shorter sentences would help"
            score_color = "#B8860B"
        else:
            verdict = "Complex — try breaking this into shorter sentences"
            score_color = "#A32638"

        st.markdown(f"""
            <div class="section">
                <h4>Readability</h4>
                <div class="score-row">
                    <span class="score-number" style="color:{score_color};">{fluency_score:.0f}</span>
                    <span class="score-label">{verdict}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown(
    "<p style='color:#A9A8A3; font-size:0.8rem; margin-top:3rem;'>Built with HuggingFace Transformers and Streamlit.</p>",
    unsafe_allow_html=True,
)
