# 🎥 Phidata Video AI Summarizer Agent

This project is a **Multimodal AI Video Summarizer** built using [Phidata](https://www.phidata.io/) and [Streamlit](https://streamlit.io/), powered by Gemini, Groq, DuckDuckGo, and YFinance tools.

Users can upload a video, ask questions, and get intelligent summaries or insights about the video content. Additionally, a separate agent playground is available for financial queries and web search.

---

## 🌟 Features

- 🎞️ Upload and analyze video content
- 🤖 Ask natural language questions about the video
- 🔍 Includes web search for contextual insights
- 📈 Separate finance and search agent playground using Groq and YFinance tools
- 🔐 API keys securely managed via `.env`

---

## 📁 Project Structure

```
├── app.py # Streamlit-based video summarization app
├── playground.py # Agent playground (finance & web search)
├── .env # API keys (not committed)
├── .streamlit/
│ └── secrets.toml # Alternative secret management
├── requirements.txt # Dependencies

```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ShrutiPriya13/video-summarizer-agent.git
cd video-summarizer-agent

```

### 2. Install Dependencies

Make sure you are using Python 3.9+.

```bash 
pip install -r requirements.txt
```

Create requirements.txt if not already present:
`streamlit`
`phi`
`google-generativeai`
`groq`
`duckduckgo-search`
`yfinance`
`python-dotenv`


### 3. Set Up API Keys

Option A:
Create a .env file in the root directory:
`GOOGLE_API_KEY="your_google_api_key"`
`OPENAI_API_KEY="your_openai_api_key"`
`GROQ_API_KEY="your_groq_api_key"`
`PHI_API_KEY="your_phi_api_key"`

Option B: Using Streamlit Secrets
Create a file at .streamlit/secrets.toml:

`GOOGLE_API_KEY = "your_google_api_key"`
`OPENAI_API_KEY = "your_openai_api_key"`
`GROQ_API_KEY = "your_groq_api_key"`
`PHI_API_KEY = "your_phi_api_key"`

## 🧠 Run the Applications

### ▶️ Video Summarizer App (Streamlit)

This is the main app for video summarization.

```bash
streamlit run app.py
```
- Upload a video file (.mp4, .mov, .avi)

- Ask a question in natural language

- Click "🔍 Analyze Video" to get insights

---

### 🧪 AI Playground (Web Search & Finance)

Run using:

```bash
python playground.py
```

The playground hosts:

- Web Search Agent (Groq + DuckDuckGo)

- Financial Agent (Groq + YFinance)



## Built With

- Streamlit

- Phidata

- Google Gemini

- Groq

- DuckDuckGo Search API

- YFinance


## 📬 Contact

For questions or improvements, feel free to open an issue.


## 📜 License

This project is licensed under the MIT License.
[MIT](LICENSE)