# StackSage — GitHub Trend Intelligence & AI Insights Platform

> A full-stack Flask web application that combines live GitHub API data with Claude AI to reveal technology trends, community health, and learning roadmaps.

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API keys
Edit `config.py`:
```python
ANTHROPIC_API_KEY = "your_anthropic_api_key_here"
GITHUB_TOKEN      = "your_github_token_here"  # Optional but recommended
```

### 3. Run
```bash
python app.py
```

Visit `http://127.0.0.1:5000`

---

## 🔑 API Keys

| Service     | Where to Get                                        | Required? |
|-------------|-----------------------------------------------------|-----------|
| Anthropic   | https://console.anthropic.com/                      | ✅ Yes    |
| GitHub PAT  | https://github.com/settings/tokens (no scopes)     | Recommended |

Without a GitHub token you still get 60 API requests/hour (enough for testing).

---

## 📁 Project Structure

```
stacksage/
├── app.py              # Flask routes + application logic
├── github_api.py       # GitHub REST API integration
├── ai_analyzer.py      # Anthropic Claude prompt engineering
├── visualizer.py       # Matplotlib charts + WordCloud
├── database.py         # SQLite persistence (history + bookmarks)
├── config.py           # API keys + configuration
├── requirements.txt    # Python dependencies
├── templates/
│   ├── base.html       # Shared layout + navbar
│   ├── index.html      # Home / search page
│   ├── results.html    # Analysis results
│   ├── history.html    # Search history
│   └── bookmarks.html  # Saved repositories
└── static/
    ├── css/style.css   # Dark cyberpunk theme
    └── js/main.js      # Client-side interactions
```

---

## ✨ Features

- **Live GitHub Search** — Queries GitHub API for top repositories by stars
- **5 Interactive Charts** — Stars ranking, language donut, activity scatter, topic word cloud, timeline
- **Claude AI Analysis** — 6-section trend report with community health, rising stars, future outlook
- **Learning Roadmap** — 3-phase personalized learning path based on real-world tool usage
- **Technology Comparison** — AI-generated comparison table for top languages found
- **Search History** — SQLite-backed history with one-click re-run
- **Bookmarks** — Save interesting repositories for later

---

## 🛠️ Technologies Used

| Layer         | Technology                |
|---------------|---------------------------|
| Backend       | Python 3.11, Flask 3.0    |
| AI            | Anthropic Claude (claude-opus-4-5) |
| Data Fetching | GitHub REST API v3, requests |
| Visualization | matplotlib, wordcloud, numpy |
| Storage       | SQLite3                   |
| Frontend      | HTML5, CSS3, Vanilla JS   |
| Fonts         | Orbitron, Inter (Google Fonts) |

---

## 📸 Pages

| URL         | Description                      |
|-------------|----------------------------------|
| `/`         | Home + search                    |
| `/analyze`  | POST → runs full analysis        |
| `/history`  | Past searches                    |
| `/bookmarks`| Saved repositories               |
| `/api/bookmark` | AJAX bookmark endpoint       |

---

*Final Project — Object-Oriented Technology — 2025*
