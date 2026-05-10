import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google import genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_repos(query, repos):
    try:
        repo_info = "\n".join([f"- {r['name']}: Stars: {r.get('stargazers_count',0)}, Lang: {r.get('language','')}" for r in repos[:8]])
        prompt = f"Analyze '{query}' GitHub domain.\nTop repos:\n{repo_info}\n\nProvide: 1)Trends 2)Rising Stars 3)Gaps 4)Future"
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"AI unavailable: {str(e)}"

def generate_learning_path(query, repos):
    try:
        tools = list(set([r.get('language','') for r in repos if r.get('language')]))[:5]
        prompt = f"Create 3-phase learning roadmap for '{query}'. Tools: {', '.join(tools)}"
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"Learning path unavailable: {str(e)}"

def compare_technologies(query, repos):
    try:
        langs = {}
        for r in repos:
            l = r.get('language','Unknown')
            langs[l] = langs.get(l,0) + 1
        prompt = f"Compare technologies in '{query}'. Distribution: {langs}"
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"Comparison unavailable: {str(e)}"
