// ── StackSage Language Switcher ─────────────────────────────
// Supports: English (en), Chinese (zh), Bangla (bn)

const translations = {
  en: {
    // Navbar
    nav_explore:   'Explore',
    nav_history:   'History',
    nav_bookmarks: 'Bookmarks',

    // Hero
    hero_badge:    'AI-Powered Analysis',
    hero_title1:   'Discover What',
    hero_title2:   'Developers Build',
    hero_sub:      'Search any technology domain. Get real GitHub data, AI-generated trend insights, interactive charts, and a personalized learning roadmap — instantly.',
    search_placeholder: 'e.g. machine learning, web3, rust game engine…',
    search_btn:    'Analyze',
    try_label:     'Try:',

    // Features
    feat1_title: 'Live GitHub Data',
    feat1_desc:  'Pulls real-time repository data — stars, forks, languages, topics, and commit activity.',
    feat2_title: 'Claude AI Insights',
    feat2_desc:  'Advanced prompt engineering extracts trends, rising stars, gaps, and future predictions.',
    feat3_title: '5 Visual Charts',
    feat3_desc:  'Stars ranking, language distribution, activity scatter, topic word cloud, and timeline.',
    feat4_title: 'Learning Roadmap',
    feat4_desc:  'AI generates a custom 3-phase learning path based on the actual tools used by top projects.',

    // Recent
    recent_title: 'Recent Searches',

    // Results
    total_stars:   'Total Stars',
    total_forks:   'Total Forks',
    avg_stars:     'Avg Stars/Repo',
    languages:     'Languages',
    ai_analysis:   'AI Trend Analysis',
    learning_road: 'Learning Roadmap',
    tech_compare:  'Technology Comparison',
    stars_ranking: 'Stars Ranking',
    lang_dist:     'Language Distribution',
    topic_cloud:   'Topic Word Cloud',
    activity_map:  'Activity Map',
    timeline:      'Activity Timeline',
    top_repos:     'Top Repositories',
    new_search:    'New Search',
    powered:       'Claude AI',

    // History
    history_title: 'Search History',
    history_sub:   'Your previous GitHub domain analyses',
    rerun:         'Re-run',
    no_history:    'No search history yet. Go explore some technologies!',

    // Bookmarks
    bm_title:    'Saved Bookmarks',
    bm_sub:      'Repositories you\'ve saved for later',
    no_bm:       'No bookmarks yet. Bookmark repositories from your analysis results.',
    start_exp:   'Start Exploring',

    // Footer
    footer_dev: 'Developed by NK',
  },

  zh: {
    nav_explore:   '探索',
    nav_history:   '历史',
    nav_bookmarks: '书签',

    hero_badge:    'AI 驱动分析',
    hero_title1:   '发现开发者',
    hero_title2:   '正在构建什么',
    hero_sub:      '搜索任何技术领域，获取真实的 GitHub 数据、AI 生成的趋势洞察、交互式图表和个性化学习路线图。',
    search_placeholder: '例如：机器学习、区块链、游戏引擎…',
    search_btn:    '分析',
    try_label:     '试试：',

    feat1_title: '实时 GitHub 数据',
    feat1_desc:  '获取实时仓库数据 — 星标、分叉、语言、话题和提交活动。',
    feat2_title: 'Claude AI 洞察',
    feat2_desc:  '先进的提示工程提取趋势、新兴项目、差距和未来预测。',
    feat3_title: '5 种可视化图表',
    feat3_desc:  '星标排名、语言分布、活动散点图、话题词云和时间线。',
    feat4_title: '学习路线图',
    feat4_desc:  'AI 根据顶级项目实际使用的工具生成定制化三阶段学习路径。',

    recent_title: '最近搜索',

    total_stars:   '总星标数',
    total_forks:   '总分叉数',
    avg_stars:     '平均星标/仓库',
    languages:     '编程语言',
    ai_analysis:   'AI 趋势分析',
    learning_road: '学习路线图',
    tech_compare:  '技术比较',
    stars_ranking: '星标排名',
    lang_dist:     '语言分布',
    topic_cloud:   '话题词云',
    activity_map:  '活动地图',
    timeline:      '活动时间线',
    top_repos:     '热门仓库',
    new_search:    '新搜索',
    powered:       'Claude AI',

    history_title: '搜索历史',
    history_sub:   '您之前的 GitHub 领域分析',
    rerun:         '重新运行',
    no_history:    '暂无搜索历史，快去探索一些技术吧！',

    bm_title:    '已保存书签',
    bm_sub:      '您保存以备后用的仓库',
    no_bm:       '暂无书签，从分析结果中收藏仓库吧。',
    start_exp:   '开始探索',

    footer_dev: 'NK 开发',
  },

  bn: {
    nav_explore:   'অন্বেষণ',
    nav_history:   'ইতিহাস',
    nav_bookmarks: 'বুকমার্ক',

    hero_badge:    'AI চালিত বিশ্লেষণ',
    hero_title1:   'আবিষ্কার করুন',
    hero_title2:   'ডেভেলপাররা কী বানাচ্ছে',
    hero_sub:      'যেকোনো প্রযুক্তি ডোমেইন সার্চ করুন। আসল GitHub ডেটা, AI-জেনারেটেড ট্রেন্ড বিশ্লেষণ, ইন্টারেক্টিভ চার্ট এবং ব্যক্তিগতকৃত লার্নিং রোডম্যাপ পান — তাৎক্ষণিকভাবে।',
    search_placeholder: 'যেমন: মেশিন লার্নিং, ব্লকচেইন, গেম ইঞ্জিন…',
    search_btn:    'বিশ্লেষণ করুন',
    try_label:     'চেষ্টা করুন:',

    feat1_title: 'লাইভ GitHub ডেটা',
    feat1_desc:  'রিয়েল-টাইম রিপোজিটরি ডেটা — স্টার, ফর্ক, ভাষা, টপিক এবং কমিট অ্যাক্টিভিটি।',
    feat2_title: 'Claude AI বিশ্লেষণ',
    feat2_desc:  'উন্নত প্রম্পট ইঞ্জিনিয়ারিং ট্রেন্ড, উদীয়মান প্রজেক্ট এবং ভবিষ্যৎ পূর্বাভাস বের করে।',
    feat3_title: '৫টি ভিজুয়াল চার্ট',
    feat3_desc:  'স্টার র‍্যাংকিং, ভাষা বিতরণ, অ্যাক্টিভিটি স্ক্যাটার, টপিক ওয়ার্ড ক্লাউড এবং টাইমলাইন।',
    feat4_title: 'লার্নিং রোডম্যাপ',
    feat4_desc:  'AI শীর্ষ প্রজেক্টে ব্যবহৃত আসল টুলের উপর ভিত্তি করে কাস্টম ৩-ধাপের শেখার পথ তৈরি করে।',

    recent_title: 'সাম্প্রতিক অনুসন্ধান',

    total_stars:   'মোট স্টার',
    total_forks:   'মোট ফর্ক',
    avg_stars:     'গড় স্টার/রিপো',
    languages:     'প্রোগ্রামিং ভাষা',
    ai_analysis:   'AI ট্রেন্ড বিশ্লেষণ',
    learning_road: 'লার্নিং রোডম্যাপ',
    tech_compare:  'প্রযুক্তি তুলনা',
    stars_ranking: 'স্টার র‍্যাংকিং',
    lang_dist:     'ভাষার বিতরণ',
    topic_cloud:   'টপিক ওয়ার্ড ক্লাউড',
    activity_map:  'অ্যাক্টিভিটি ম্যাপ',
    timeline:      'অ্যাক্টিভিটি টাইমলাইন',
    top_repos:     'শীর্ষ রিপোজিটরি',
    new_search:    'নতুন অনুসন্ধান',
    powered:       'Claude AI',

    history_title: 'অনুসন্ধান ইতিহাস',
    history_sub:   'আপনার আগের GitHub ডোমেইন বিশ্লেষণ',
    rerun:         'পুনরায় চালান',
    no_history:    'এখনো কোনো ইতিহাস নেই। প্রযুক্তি অন্বেষণ করতে যান!',

    bm_title:    'সংরক্ষিত বুকমার্ক',
    bm_sub:      'পরে দেখার জন্য সংরক্ষিত রিপোজিটরি',
    no_bm:       'এখনো কোনো বুকমার্ক নেই। বিশ্লেষণ থেকে রিপো বুকমার্ক করুন।',
    start_exp:   'অন্বেষণ শুরু করুন',

    footer_dev: 'NK দ্বারা তৈরি',
  }
};

// ── Apply translations to the page ───────────────────────────
function applyLanguage(lang) {
  const t = translations[lang];
  if (!t) return;

  // Save to localStorage so it persists across pages
  localStorage.setItem('stacksage_lang', lang);

  // Update every element with a data-i18n attribute
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key]) {
      if (el.tagName === 'INPUT' && el.hasAttribute('placeholder')) {
        el.placeholder = t[key];
      } else {
        el.textContent = t[key];
      }
    }
  });

  // Highlight active language button
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('lang-active', btn.getAttribute('data-lang') === lang);
  });
}

// ── Init on page load ─────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('stacksage_lang') || 'en';
  applyLanguage(saved);
});
