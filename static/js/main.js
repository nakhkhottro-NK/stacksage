// ── StackSage — main.js ─────────────────────────────────────────

// Set query from quick-tag click
function setQuery(text) {
  const input = document.getElementById('queryInput');
  const domain = document.getElementById('domainInput');
  if (input) {
    input.value = text;
    if (domain) domain.value = text;
    input.focus();
  }
}

// Show loading state on form submit
const searchForm = document.getElementById('searchForm');
if (searchForm) {
  searchForm.addEventListener('submit', function () {
    const domainInput = document.getElementById('domainInput');
    const queryInput  = document.getElementById('queryInput');
    if (domainInput && queryInput) {
      domainInput.value = queryInput.value.trim();
    }
    const btn = document.getElementById('searchBtn');
    if (btn) {
      btn.querySelector('.btn-text')?.classList.add('hidden');
      btn.querySelector('.btn-loading')?.classList.remove('hidden');
      btn.disabled = true;
    }
  });
}

// Toast notification helper
function showToast(message, isError = false) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = message;
  toast.style.background = isError ? 'var(--accent2)' : 'var(--accent3)';
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}

// Bookmark a repository via AJAX
async function bookmarkRepo(name, url, stars, language, description) {
  try {
    const resp = await fetch('/api/bookmark', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ repo_name: name, repo_url: url, stars, language, description })
    });
    const data = await resp.json();
    if (data.success) {
      showToast(`✓ Bookmarked: ${name.split('/').pop()}`);
    } else {
      showToast('Failed to bookmark.', true);
    }
  } catch (err) {
    showToast('Network error.', true);
  }
}

// Auto-dismiss flash messages
document.querySelectorAll('.flash').forEach(el => {
  setTimeout(() => {
    el.style.transition = 'opacity .5s';
    el.style.opacity = '0';
    setTimeout(() => el.remove(), 500);
  }, 5000);
});
