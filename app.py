from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file

import time
from pathlib import Path
import tempfile
import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(
    page_title="Multimodal AI Agent - Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

# Title
st.title("🎥 Video AI Summarizer Agent")
st.header("Powered by Gemini 2.0 Flash Exp + DuckDuckGo")

# Get API key from Streamlit Secrets
API_KEY = st.secrets.get("GOOGLE_API_KEY")
if not API_KEY:
    st.error("⚠️ GOOGLE_API_KEY is missing. Please add it to Streamlit Secrets.")
    st.stop()

# Configure Gemini
genai.configure(api_key=API_KEY)

# Cached agent
@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

# Initialize agent
agent = initialize_agent()

# Upload section
video_file = st.file_uploader(
    "📤 Upload a video file",
    type=['mp4', 'mov', 'avi'],
    help="Upload a video for AI analysis"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp:
        temp.write(video_file.read())
        video_path = temp.name

    st.video(video_path)

    query = st.text_area(
        "🤔 What do you want to ask?",
        placeholder="E.g., Summarize the video, give key insights, etc."
    )

    if st.button("🔍 Analyze Video"):
        if not query:
            st.warning("⚠️ Please enter a question before analyzing.")
        else:
            try:
                with st.spinner("⏳ Uploading and processing video..."):
                    uploaded = upload_file(video_path)
                    while uploaded.state.name == "PROCESSING":
                        time.sleep(1)
                        uploaded = get_file(uploaded.name)

                # Prompt
                prompt = f"""
Analyze the uploaded video for content and context.
Respond to the following query using video insights and web research:
{query}

Return a clear, human-readable, and actionable response.
                """

                # Run agent
                response = agent.run(prompt, videos=[uploaded])

                # Show result
                st.subheader("✅ AI Response")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"❌ Error: {e}")
            finally:
                Path(video_path).unlink(missing_ok=True)
else:
    st.info("📂 Please upload a video to begin.")

# Custom UI style
st.markdown("""
<style>
.stTextArea textarea {
    height: 100px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 0.9em;'>"
    "Made with ❤️ using Gemini & DuckDuckGo + Streamlit"
    "</div>",
    unsafe_allow_html=True
)
