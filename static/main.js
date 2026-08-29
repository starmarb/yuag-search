document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#label');
  const out = document.querySelector('#live-results');
  let controller, timer;

  input.addEventListener('input', () => {
    clearTimeout(timer);
    timer = setTimeout(async () => {
      const q = input.value.trim();
      if (q.length < 2) { out.innerHTML = ''; return; }
      controller?.abort();
      controller = new AbortController();
      try {
        const res = await fetch(`/api/search?l=${encodeURIComponent(q)}`,
                                { signal: controller.signal });
        const rows = await res.json();
        out.innerHTML = rows.map(r =>
          `<div><a href="/object/${r[0]}">${r[1]}</a> — ${r[2]}</div>`
        ).join('');
      } catch (e) { if (e.name !== 'AbortError') console.error(e); }
    }, 250);
  });
});