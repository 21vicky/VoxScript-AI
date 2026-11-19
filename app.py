import html
import os
import tempfile
from pathlib import Path

import streamlit as st
import whisper


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="VoxScript AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# THEME & STYLES
# =========================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #0b1120;
    --panel: #151f33;
    --panel-soft: #1b2940;
    --border: #2b3a55;
    --muted: #9aa9c2;
    --text: #f8fafc;
    --purple: #8b5cf6;
    --purple-light: #c4b5fd;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 50% -15%, rgba(91, 33, 182, .22), transparent 45%),
        var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 1120px;
    padding-top: 2.2rem;
    padding-bottom: 2.5rem;
}

header[data-testid="stHeader"] {
    background: rgba(11, 17, 32, .75);
}

section[data-testid="stSidebar"] {
    background: #101a2c;
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] * {
    color: var(--text);
}

.hero {
    background: linear-gradient(120deg, #1e2a68 0%, #392681 55%, #581c87 100%);
    border: 1px solid rgba(139, 92, 246, .65);
    border-radius: 22px;
    padding: 34px 38px;
    margin: 0 0 32px 0;
    box-shadow: 0 18px 55px rgba(0, 0, 0, .20);
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 13px;
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 999px;
    background: rgba(255,255,255,.10);
    color: #ddd6fe;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: .8px;
}

.hero h1 {
    color: #fff !important;
    font-size: clamp(32px, 4vw, 46px);
    line-height: 1.15;
    font-weight: 800;
    margin: 18px 0 10px 0;
}

.hero p {
    color: #e2ddff !important;
    font-size: 15px;
    line-height: 1.7;
    margin: 0;
    max-width: 680px;
}

.section-heading {
    color: #d6ccff;
    font-size: 19px;
    font-weight: 750;
    margin: 0 0 13px 0;
}

.info-card {
    background: linear-gradient(145deg, #18243a, #141e31);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 23px 18px;
    text-align: center;
    min-height: 126px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.info-card .eyebrow {
    color: #a5b4fc;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: .8px;
    margin-bottom: 12px;
}

.info-card .value {
    color: #fff;
    font-size: 19px;
    line-height: 1.55;
    font-weight: 800;
    margin: 0;
}

div[data-testid="stFileUploader"] {
    background: rgba(24, 36, 58, .75);
    border: 1px dashed #7662e8;
    border-radius: 15px;
    padding: 13px;
}

div[data-testid="stFileUploader"] section {
    background: transparent;
}

div[data-testid="stAudio"] {
    margin-top: 10px;
}

.stButton > button {
    background: linear-gradient(90deg, #6366f1, #9333ea);
    color: white;
    border: 0;
    border-radius: 11px;
    min-height: 46px;
    font-weight: 750;
    transition: .2s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #4f46e5, #7e22ce);
    color: white;
    border: 0;
    transform: translateY(-1px);
}

.stDownloadButton > button {
    background: #047857;
    color: white;
    border: 0;
    border-radius: 11px;
    min-height: 44px;
    font-weight: 750;
}

.stDownloadButton > button:hover {
    background: #059669;
    color: white;
    border: 0;
}

div[data-testid="stTextArea"] textarea {
    background: #111c2e;
    color: #f8fafc;
    border: 1px solid #344563;
    border-radius: 12px;
    line-height: 1.7;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

hr {
    border-color: var(--border);
    margin: 28px 0;
}

.footer {
    background: rgba(21, 31, 51, .75);
    border: 1px solid var(--border);
    border-radius: 16px;
    text-align: center;
    padding: 22px;
    margin-top: 24px;
}

.footer h3 {
    color: #c4b5fd !important;
    font-size: 18px;
    margin: 0 0 8px 0;
}

.footer p {
    color: var(--muted) !important;
    margin: 4px 0;
    font-size: 13px;
}

div[data-testid="stMetric"] {
    background: #17243a;
    border: 1px solid var(--border);
    padding: 14px;
    border-radius: 13px;
}
</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# CONSTANTS
# =========================================================

LANGUAGES = {
    "Auto Detect": None,
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
}

SUPPORTED_TYPES = ["mp3", "wav", "m4a", "ogg", "flac"]
MAX_FILE_SIZE_MB = 200


# =========================================================
# WHISPER MODEL
# =========================================================

@st.cache_resource(show_spinner=False)
def load_whisper_model(model_name: str):
    """Load and cache the Whisper model so it is not reloaded each rerun."""
    return whisper.load_model(model_name, device="cpu")


# =========================================================
# SIDEBAR SETTINGS
# =========================================================

with st.sidebar:
    st.title("⚙️ Settings")
    st.divider()

    selected_language = st.selectbox(
        "🌍 Audio language",
        options=list(LANGUAGES.keys()),
        index=0,
    )

    model_name = st.selectbox(
        "🤖 Whisper model",
        options=["tiny", "base", "small"],
        index=1,
        help="Tiny is faster; Small can be more accurate but needs more memory.",
    )

    st.divider()
    st.markdown("### 🛠️ Built with")
    st.write("🐍 Python")
    st.write("🔥 PyTorch")
    st.write("🎙️ OpenAI Whisper")
    st.write("🌐 Streamlit")
    st.write("🎵 FFmpeg")

    st.divider()
    st.caption("30 Days 30 AI Projects")
    st.caption("Day 13 · VoxScript AI")


# =========================================================
# HERO
# Important: keep HTML tags flush-left inside Markdown.
# Indented HTML can be interpreted as a Markdown code block.
# =========================================================

st.markdown(
    """
<div class="hero">
<div class="hero-badge">⚡ AI POWERED SPEECH RECOGNITION</div>
<h1>🎙️ VoxScript AI</h1>
<p>Transform your voice into text using OpenAI Whisper.<br>
Intelligent multilingual speech recognition, right from your browser.</p>
</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# UPLOAD SECTION
# =========================================================

upload_col, formats_col = st.columns([1.55, 1], gap="large")

with upload_col:
    st.markdown('<div class="section-heading">📂 Upload your audio</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose an audio file",
        type=SUPPORTED_TYPES,
        help=f"Supported: MP3, WAV, M4A, OGG and FLAC. Maximum size: {MAX_FILE_SIZE_MB} MB.",
    )

with formats_col:
    st.markdown('<div class="section-heading">📌 Supported formats</div>', unsafe_allow_html=True)
    st.markdown(
        """
<div class="info-card">
<div class="eyebrow">SUPPORTED AUDIO</div>
<p class="value">MP3 · WAV · M4A<br>OGG · FLAC</p>
</div>
""",
        unsafe_allow_html=True,
    )


# =========================================================
# AUDIO PREVIEW & TRANSCRIPTION
# =========================================================

if uploaded_file is not None:
    st.divider()
    st.markdown('<div class="section-heading">🎧 Audio preview</div>', unsafe_allow_html=True)

    file_size_mb = len(uploaded_file.getvalue()) / (1024 * 1024)

    if file_size_mb > MAX_FILE_SIZE_MB:
        st.error(f"File is too large ({file_size_mb:.1f} MB). Please upload a file under {MAX_FILE_SIZE_MB} MB.")
    else:
        st.audio(uploaded_file)
        st.success(f"Uploaded successfully: {uploaded_file.name} · {file_size_mb:.2f} MB")

        start_col, clear_col = st.columns([3, 1])

        with start_col:
            start_transcription = st.button(
                "🚀 Start transcription",
                use_container_width=True,
                type="primary",
            )

        with clear_col:
            if st.button("🗑️ Clear result", use_container_width=True):
                st.session_state.pop("voxscript_result", None)
                st.rerun()

        if start_transcription:
            temp_path = None

            try:
                file_extension = Path(uploaded_file.name).suffix.lower() or ".wav"

                with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_audio:
                    temp_audio.write(uploaded_file.getvalue())
                    temp_path = temp_audio.name

                with st.spinner(f"🤖 Loading Whisper '{model_name}' model..."):
                    model = load_whisper_model(model_name)

                transcription_options = {
                    "task": "transcribe",
                    "fp16": False,
                    "verbose": False,
                }

                language_code = LANGUAGES[selected_language]
                if language_code:
                    transcription_options["language"] = language_code

                with st.spinner("🎙️ VoxScript AI is processing your audio. This may take a few minutes..."):
                    result = model.transcribe(temp_path, **transcription_options)

                transcript = result.get("text", "").strip()
                detected_language = result.get("language", "unknown")

                if transcript:
                    st.session_state["voxscript_result"] = {
                        "transcript": transcript,
                        "language": detected_language,
                        "filename": uploaded_file.name,
                    }
                    st.success("🎉 Transcription completed successfully!")
                else:
                    st.session_state.pop("voxscript_result", None)
                    st.warning("No speech was detected. Please try another audio file.")

            except Exception as error:
                st.error(f"Transcription failed: {error}")
                st.info("Check that the audio file is valid and FFmpeg is installed and available in PATH.")
            finally:
                if temp_path and os.path.exists(temp_path):
                    try:
                        os.remove(temp_path)
                    except OSError:
                        pass


# =========================================================
# TRANSCRIPTION RESULT
# =========================================================

saved_result = st.session_state.get("voxscript_result")

if saved_result:
    transcript = saved_result["transcript"]
    detected_language = saved_result["language"]

    st.divider()
    st.markdown('<div class="section-heading">📝 Transcription result</div>', unsafe_allow_html=True)

    st.text_area(
        "Recognized speech",
        value=transcript,
        height=260,
        key="voxscript_transcript_display",
    )

    word_count = len(transcript.split())
    character_count = len(transcript)

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric("🌍 Detected language", detected_language.upper())

    with metric2:
        st.metric("🔤 Characters", f"{character_count:,}")

    with metric3:
        st.metric("📝 Words", f"{word_count:,}")

    st.download_button(
        label="📥 Download transcript (.txt)",
        data=transcript,
        file_name="voxscript_transcript.txt",
        mime="text/plain",
        use_container_width=True,
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
<div class="footer">
<h3>🎙️ VoxScript AI</h3>
<p>Powered by OpenAI Whisper · Built with Python &amp; Streamlit</p>
<p>30 Days 30 AI Projects · Day 13</p>
</div>
""",
    unsafe_allow_html=True,
)
