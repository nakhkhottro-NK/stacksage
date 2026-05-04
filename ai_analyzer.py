"""
ai_analyzer.py — AI-Powered Analysis using Anthropic Claude API
Generates insights, learning paths, and technology comparisons.
"""

import anthropic
import json
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
MODEL = "claude-opus-4-5"


def _call_claude(prompt: str, max_tokens: int = 1200) -> str:
    """Helper to call Claude and return text response."""
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except anthropic.AuthenticationError:
        return "⚠️ Invalid API key. Please check your ANTHROPIC_API_KEY in config.py."
    except anthropic.RateLimitError:
        return "⚠️ Rate limit reached. Please wait a moment and try again."
    except Exception as e:
        return f"⚠️ AI analysis temporarily unavailable: {str(e)}"


def analyze_repos(query: str, repos_data: dict) -> str:
    """
    Main analysis function — generates comprehensive trend insights
    from the GitHub repository data using prompt engineering.
    """
    repos = repos_data.get('repos', [])[:10]
    repo_summary = [
        {
            'name':        r['name'],
            'description': r['description'][:100],
            'stars':       r['stars'],
            'forks':       r['forks'],
            'language':    r['language'],
            'topics':      r['topics'][:6],
            'updated':     r['updated_at']
        }
        for r in repos
    ]

    prompt = f"""You are a senior technology trend analyst specializing in open-source ecosystems.
I searched GitHub for: "{query}" and collected the following repository data:

{json.dumps(repo_summary, indent=2)}

Provide a structured, data-driven analysis with these exact sections:

## 🔥 TREND SUMMARY
What major trends does this data reveal? What is the state of this domain right now?

## 🛠️ DOMINANT TECHNOLOGIES
Which languages, frameworks, and tools dominate? Why are they winning?

## 📊 COMMUNITY HEALTH
Analyze the star-to-fork ratios. Are people using this tech (high stars) or contributing to it (high forks)? What does that tell us?

## ⭐ RISING STARS
Pick 2-3 repos that stand out — not just the biggest, but those with high potential based on recency, topics, or engagement.

## ⚠️ GAPS & OPPORTUNITIES
What is missing in this ecosystem? Where could a new developer contribute most?

## 🔮 FUTURE OUTLOOK
Based on the topics, languages, and activity patterns — where is this domain headed in the next 2 years?

## 💡 ONE-LINE VERDICT
A single powerful sentence summarizing the health and momentum of this ecosystem.

Be specific and reference actual repo names and numbers from the data. Maximum 500 words."""

    return _call_claude(prompt, max_tokens=1400)


def generate_learning_path(domain: str, languages: dict, topics: dict) -> str:
    """
    Generates a structured learning roadmap for entering the given domain,
    based on the actual languages and topics found in real GitHub repos.
    """
    top_langs = ', '.join(list(languages.keys())[:5]) if languages else 'various languages'
    top_topics = ', '.join(list(topics.keys())[:10]) if topics else 'various topics'

    prompt = f"""You are a senior software engineer and educator creating a personalized learning roadmap.

Domain: "{domain}"
Most-used languages in real projects: {top_langs}
Key topics found in open-source repos: {top_topics}

Create a practical, actionable learning roadmap with these sections:

## 🟢 PHASE 1: Foundations (Weeks 1–4)
List exactly 4 concrete steps to get started. Be specific — name actual tools/concepts to learn.

## 🟡 PHASE 2: Building Projects (Months 2–3)
Describe 3 mini-projects that progressively build skills. Include what each project teaches.

## 🔴 PHASE 3: Advanced Mastery (Months 4–6)
Name 3 advanced skills or areas that would make someone job-ready or contribution-ready in this domain.

## 📚 KEY RESOURCES TO FIND
Name 3 types of resources (not specific URLs) that are best for learning this domain (e.g., "official documentation", "hands-on Kaggle competitions").

## ⏱️ TIME ESTIMATE
Honest estimate of how long to reach proficiency for a beginner vs someone with programming experience.

Keep it encouraging, practical, and under 350 words."""

    return _call_claude(prompt, max_tokens=700)


def compare_technologies(tech_list: list, domain: str) -> str:
    """
    Generates a markdown comparison table and recommendation
    for multiple technologies found in a domain.
    """
    techs = ', '.join(tech_list)

    prompt = f"""You are a software architect helping a developer choose between technologies.

Domain: {domain}
Technologies to compare: {techs}

Create a concise comparison using this exact format:

## Technology Comparison: {domain}

| Technology | Primary Use | Learning Curve | Job Market | Best For |
|---|---|---|---|---|
(fill in all technologies)

## 🏆 Recommendation
In exactly 3 sentences: Which technology should someone pick first and why? 
Mention specific trade-offs and what type of developer each technology suits best.

Be honest about trade-offs. Maximum 200 words."""

    return _call_claude(prompt, max_tokens=500)
