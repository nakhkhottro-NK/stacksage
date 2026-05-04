"""
StackSage - GitHub Trend Intelligence & AI-Powered Tech Analysis
Main Flask Application
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from github_api import search_repositories, get_trending_languages, get_repo_stats_summary
from ai_analyzer import analyze_repos, generate_learning_path, compare_technologies
from visualizer import (create_stars_chart, create_language_chart,
                        create_activity_scatter, create_wordcloud, create_timeline_chart)
from database import init_db, save_search, get_recent_searches, get_search_by_id, add_bookmark, get_bookmarks
import json

app = Flask(__name__)
app.secret_key = "stacksage_secret_2025"


@app.route('/')
def index():
    recent_searches = get_recent_searches(5)
    bookmarks_count = len(get_bookmarks())
    return render_template('index.html', recent_searches=recent_searches, bookmarks_count=bookmarks_count)


@app.route('/analyze', methods=['POST'])
def analyze():
    query = request.form.get('query', '').strip()
    domain = request.form.get('domain', query)

    if not query:
        flash('Please enter a search query.', 'error')
        return redirect(url_for('index'))

    # --- 1. Fetch GitHub Data ---
    repos_data = search_repositories(query, per_page=12)

    if 'error' in repos_data and not repos_data.get('repos'):
        flash(f"GitHub API error: {repos_data['error']}", 'error')
        return redirect(url_for('index'))

    repos = repos_data['repos']
    if not repos:
        flash(f'No repositories found for "{query}". Try a different keyword.', 'error')
        return redirect(url_for('index'))

    # --- 2. Compute Statistics ---
    languages = get_trending_languages(repos)

    all_topics = {}
    for r in repos:
        for t in r['topics']:
            all_topics[t] = all_topics.get(t, 0) + 1

    stats = {
        'total_found': repos_data['total_count'],
        'analyzed': len(repos),
        'total_stars': sum(r['stars'] for r in repos),
        'total_forks': sum(r['forks'] for r in repos),
        'avg_stars': sum(r['stars'] for r in repos) // max(len(repos), 1),
        'top_repo': max(repos, key=lambda r: r['stars'])['name'].split('/')[-1],
        'languages': languages,
        'top_topics': dict(sorted(all_topics.items(), key=lambda x: x[1], reverse=True)[:15])
    }

    # --- 3. AI Insights ---
    ai_insights = analyze_repos(query, repos_data)
    learning_path = generate_learning_path(domain, languages, all_topics)

    tech_comparison = None
    if len(languages) >= 2:
        tech_comparison = compare_technologies(list(languages.keys())[:4], domain)

    # --- 4. Generate Charts ---
    charts = {
        'stars': create_stars_chart(repos),
        'languages': create_language_chart(languages),
        'activity': create_activity_scatter(repos),
        'wordcloud': create_wordcloud(all_topics, query),
        'timeline': create_timeline_chart(repos)
    }

    # --- 5. Persist to DB ---
    search_id = save_search(query, domain, repos, ai_insights)

    return render_template('results.html',
        query=query,
        domain=domain,
        repos=repos,
        stats=stats,
        ai_insights=ai_insights,
        learning_path=learning_path,
        tech_comparison=tech_comparison,
        charts=charts,
        search_id=search_id
    )


@app.route('/history')
def history():
    searches = get_recent_searches(20)
    return render_template('history.html', searches=searches)


@app.route('/bookmarks')
def bookmarks():
    books = get_bookmarks()
    return render_template('bookmarks.html', bookmarks=books)


@app.route('/api/bookmark', methods=['POST'])
def bookmark():
    data = request.get_json()
    add_bookmark(
        data.get('repo_name', ''),
        data.get('repo_url', ''),
        data.get('stars', 0),
        data.get('language', 'Unknown'),
        data.get('description', '')
    )
    return jsonify({'success': True, 'message': 'Bookmarked successfully!'})


@app.route('/api/quick-compare', methods=['POST'])
def quick_compare():
    data = request.get_json()
    techs = data.get('technologies', [])
    domain = data.get('domain', 'general')
    if len(techs) < 2:
        return jsonify({'error': 'Please provide at least 2 technologies.'})
    result = compare_technologies(techs, domain)
    return jsonify({'comparison': result})

with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True, port=5000)

