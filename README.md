<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hand Boundary POC – README</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #050a0f;
    --bg2: #0c1420;
    --bg3: #0f1c2a;
    --card: #0d1a26;
    --border: rgba(0,200,120,0.15);
    --border2: rgba(0,200,120,0.3);
    --green: #00c878;
    --green2: #00ff94;
    --amber: #ffb300;
    --red: #ff4444;
    --text: #e8f4ee;
    --muted: #7a9a8a;
    --mono: 'Space Mono', monospace;
    --sans: 'DM Sans', sans-serif;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--sans);
    font-size: 16px;
    line-height: 1.7;
    overflow-x: hidden;
  }

  /* ── HERO ── */
  .hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    position: relative;
    padding: 4rem 2rem;
    overflow: hidden;
  }

  .hero-grid {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,200,120,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,200,120,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    animation: gridScroll 20s linear infinite;
  }

  @keyframes gridScroll {
    0% { background-position: 0 0; }
    100% { background-position: 48px 48px; }
  }

  .hero-glow {
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,200,120,0.08) 0%, transparent 70%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation: pulse 4s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.6; }
    50% { transform: translate(-50%, -50%) scale(1.15); opacity: 1; }
  }

  .hero-content { position: relative; z-index: 2; max-width: 800px; }

  .eyebrow {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.2em;
    color: var(--green);
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.2s forwards;
  }

  .hero h1 {
    font-family: var(--mono);
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.4s forwards;
  }

  .hero h1 span { color: var(--green); }

  .hero p {
    font-size: 1.1rem;
    color: var(--muted);
    max-width: 540px;
    margin: 0 auto 2.5rem;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.6s forwards;
  }

  .hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 2.5rem;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.8s forwards;
  }

  .badge {
    font-family: var(--mono);
    font-size: 11px;
    padding: 6px 14px;
    border: 1px solid var(--border2);
    border-radius: 4px;
    color: var(--green);
    background: rgba(0,200,120,0.05);
    letter-spacing: 0.05em;
  }

  .cta-row {
    display: flex;
    gap: 14px;
    justify-content: center;
    flex-wrap: wrap;
    opacity: 0;
    animation: fadeUp 0.6s ease 1s forwards;
  }

  .btn-primary {
    font-family: var(--mono);
    font-size: 13px;
    font-weight: 700;
    padding: 14px 32px;
    background: var(--green);
    color: #050a0f;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    transition: transform 0.15s, box-shadow 0.15s;
    letter-spacing: 0.05em;
  }

  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0,200,120,0.35);
  }

  .btn-outline {
    font-family: var(--mono);
    font-size: 13px;
    padding: 14px 32px;
    background: transparent;
    color: var(--green);
    border: 1px solid var(--border2);
    border-radius: 4px;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    transition: background 0.15s, transform 0.15s;
    letter-spacing: 0.05em;
  }

  .btn-outline:hover {
    background: rgba(0,200,120,0.07);
    transform: translateY(-2px);
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* ── SECTIONS ── */
  section {
    padding: 6rem 2rem;
    max-width: 1000px;
    margin: 0 auto;
  }

  .section-label {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--green);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
  }

  section h2 {
    font-family: var(--mono);
    font-size: clamp(1.5rem, 3vw, 2rem);
    font-weight: 700;
    margin-bottom: 2.5rem;
    color: var(--text);
  }

  /* ── STATE MACHINE ── */
  .state-machine {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 3rem 0;
    overflow-x: auto;
    padding-bottom: 1rem;
  }

  .state {
    flex: 1;
    min-width: 160px;
    padding: 1.5rem;
    border: 1px solid;
    border-radius: 8px;
    text-align: center;
    position: relative;
    transition: transform 0.2s, box-shadow 0.2s;
    cursor: default;
  }

  .state:hover { transform: translateY(-4px); }

  .state.safe {
    border-color: rgba(0,200,120,0.4);
    background: rgba(0,200,120,0.05);
  }

  .state.warn {
    border-color: rgba(255,179,0,0.4);
    background: rgba(255,179,0,0.05);
  }

  .state.danger {
    border-color: rgba(255,68,68,0.4);
    background: rgba(255,68,68,0.05);
  }

  .state-icon { font-size: 2rem; margin-bottom: 0.5rem; display: block; }
  .state-name { font-family: var(--mono); font-size: 13px; font-weight: 700; }
  .state.safe .state-name { color: var(--green); }
  .state.warn .state-name { color: var(--amber); }
  .state.danger .state-name { color: var(--red); }
  .state-desc { font-size: 12px; color: var(--muted); margin-top: 0.4rem; }

  .state-arrow {
    font-family: var(--mono);
    font-size: 20px;
    color: var(--muted);
    padding: 0 8px;
    flex-shrink: 0;
  }

  /* ── TECH CARDS ── */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
  }

  .tech-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.5rem 1.25rem;
    transition: border-color 0.2s, transform 0.2s;
  }

  .tech-card:hover {
    border-color: var(--border2);
    transform: translateY(-3px);
  }

  .tech-icon {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--green);
    letter-spacing: 0.1em;
    margin-bottom: 0.75rem;
    display: block;
  }

  .tech-card h3 {
    font-family: var(--mono);
    font-size: 14px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 0.35rem;
  }

  .tech-card p { font-size: 13px; color: var(--muted); }

  /* ── FILE TREE ── */
  .file-tree {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 2rem;
    font-family: var(--mono);
    font-size: 13px;
    line-height: 2;
  }

  .tree-line { display: flex; align-items: center; gap: 8px; }
  .tree-indent { padding-left: 1.5em; }
  .tree-dir { color: var(--green); }
  .tree-file { color: var(--text); }
  .tree-file.main { color: var(--green2); }
  .tree-comment { color: var(--muted); font-size: 11px; }

  /* ── TERMINAL ── */
  .terminal {
    background: #020609;
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    margin: 1.5rem 0;
  }

  .term-bar {
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .term-dot { width: 10px; height: 10px; border-radius: 50%; }
  .term-dot.r { background: #ff5f57; }
  .term-dot.y { background: #ffbd2e; }
  .term-dot.g { background: #28c840; }
  .term-title { font-family: var(--mono); font-size: 11px; color: var(--muted); margin-left: 8px; }

  .term-body { padding: 1.5rem; }
  .term-line { font-family: var(--mono); font-size: 13px; line-height: 2; display: flex; gap: 10px; }
  .prompt { color: var(--green); }
  .cmd { color: var(--text); }
  .comment-line { color: var(--muted); font-size: 12px; padding-left: 1em; }

  /* ── LIVE DEMO CARD ── */
  .demo-card {
    position: relative;
    border: 1px solid rgba(0,200,120,0.3);
    border-radius: 12px;
    padding: 3rem 2rem;
    text-align: center;
    overflow: hidden;
    background: var(--card);
  }

  .demo-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 0%, rgba(0,200,120,0.08) 0%, transparent 60%);
    pointer-events: none;
  }

  .demo-status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--green);
    background: rgba(0,200,120,0.1);
    border: 1px solid rgba(0,200,120,0.3);
    border-radius: 100px;
    padding: 6px 16px;
    margin-bottom: 1.5rem;
  }

  .status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--green);
    animation: blink 1.5s ease-in-out infinite;
  }

  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.2; }
  }

  .demo-card h3 {
    font-family: var(--mono);
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
  }

  .demo-card p { color: var(--muted); margin-bottom: 2rem; max-width: 400px; margin-left: auto; margin-right: auto; }

  .demo-features {
    display: flex;
    gap: 24px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 2rem;
  }

  .demo-feat {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .demo-feat::before {
    content: '✓';
    color: var(--green);
    font-weight: 700;
  }

  /* ── DIVIDER ── */
  .divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 0 2rem;
  }

  /* ── FOOTER ── */
  footer {
    text-align: center;
    padding: 3rem 2rem;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--muted);
    border-top: 1px solid var(--border);
  }

  footer a { color: var(--green); text-decoration: none; }

  /* ── SCROLL REVEAL ── */
  .reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }

  .reveal.visible {
    opacity: 1;
    transform: none;
  }

  /* ── ANIMATED FINGER ── */
  .finger-demo {
    display: flex;
    justify-content: center;
    margin: 3rem 0;
  }

  .zone-wrapper {
    position: relative;
    width: 340px;
    height: 160px;
  }

  .danger-box {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 110px;
    height: 110px;
    border: 2px dashed var(--red);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--red);
    letter-spacing: 0.1em;
  }

  .finger-tip {
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 28px;
    height: 28px;
    animation: fingerMove 4s ease-in-out infinite;
  }

  .finger-circle {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: var(--green);
    transition: background 0.3s;
  }

  @keyframes fingerMove {
    0%, 10% { left: 0; }
    45% { left: calc(100% - 140px); }
    55% { left: calc(100% - 140px); }
    90%, 100% { left: 0; }
  }

  .status-label {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    font-family: var(--mono);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.15em;
    animation: statusCycle 4s ease-in-out infinite;
  }

  @keyframes statusCycle {
    0%, 30% { color: var(--green); }
    0%, 30% { opacity: 1; }
    35%, 65% { color: var(--amber); }
    70%, 100% { color: var(--red); }
  }

  @media (max-width: 600px) {
    .state-machine { flex-direction: column; }
    .state-arrow { transform: rotate(90deg); }
  }
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-grid"></div>
  <div class="hero-glow"></div>
  <div class="hero-content">
    <p class="eyebrow">✋ Proof of Concept · Computer Vision · Real-Time</p>
    <h1>Hand Boundary<br><span>Danger Zone</span></h1>
    <p>Real-time finger tracking meets virtual safety boundaries. No MediaPipe. No cloud. Pure OpenCV on CPU.</p>
    <div class="hero-badges">
      <span class="badge">OpenCV</span>
      <span class="badge">Streamlit</span>
      <span class="badge">WebRTC</span>
      <span class="badge">CPU Only</span>
      <span class="badge">Python 3.8+</span>
    </div>
    <div class="cta-row">
      <a href="https://finger-danger-zone-rvxmehtcvory4mcnau5w6x.streamlit.app/" target="_blank" class="btn-primary">→ Launch Live App</a>
      <a href="https://github.com/coderjaynt/finger-danger-zone" target="_blank" class="btn-outline">⌥ View on GitHub</a>
    </div>
  </div>
</div>

<!-- WHAT IT DOES -->
<section>
  <div class="reveal">
    <p class="section-label">01 / Overview</p>
    <h2>What this prototype does</h2>
    <p style="color: var(--muted); max-width: 640px; margin-bottom: 2.5rem;">
      A virtual safety zone overlays your live camera feed. As your finger moves toward the boundary, the system transitions through three states — driven entirely by geometry-based distance calculations, running in real-time on any CPU.
    </p>

    <!-- Animated finger demo -->
    <div class="finger-demo">
      <div class="zone-wrapper">
        <p class="status-label" id="statusLabel">SAFE</p>
        <div class="finger-tip" id="fingerTip">
          <div class="finger-circle" id="fingerCircle"></div>
        </div>
        <div class="danger-box">DANGER<br>ZONE</div>
      </div>
    </div>

    <div class="state-machine">
      <div class="state safe">
        <span class="state-icon">🟢</span>
        <div class="state-name">SAFE</div>
        <div class="state-desc">Far from boundary</div>
      </div>
      <div class="state-arrow">→</div>
      <div class="state warn">
        <span class="state-icon">🟡</span>
        <div class="state-name">WARNING</div>
        <div class="state-desc">Approaching zone</div>
      </div>
      <div class="state-arrow">→</div>
      <div class="state danger">
        <span class="state-icon">🔴</span>
        <div class="state-name">DANGER</div>
        <div class="state-desc">Inside boundary</div>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- TECH STACK -->
<section>
  <div class="reveal">
    <p class="section-label">02 / Tech Stack</p>
    <h2>Built with</h2>
    <div class="tech-grid">
      <div class="tech-card">
        <span class="tech-icon">LANG</span>
        <h3>Python 3.8+</h3>
        <p>Core runtime, fully cross-platform</p>
      </div>
      <div class="tech-card">
        <span class="tech-icon">CV</span>
        <h3>OpenCV</h3>
        <p>Fingertip detection & frame processing</p>
      </div>
      <div class="tech-card">
        <span class="tech-icon">NUM</span>
        <h3>NumPy</h3>
        <p>Distance math & array operations</p>
      </div>
      <div class="tech-card">
        <span class="tech-icon">UI</span>
        <h3>Streamlit</h3>
        <p>Zero-config web interface</p>
      </div>
      <div class="tech-card">
        <span class="tech-icon">RTC</span>
        <h3>WebRTC</h3>
        <p>Live browser camera stream</p>
      </div>
      <div class="tech-card">
        <span class="tech-icon">AV</span>
        <h3>av</h3>
        <p>Video frame decoding pipeline</p>
      </div>
    </div>
    <p style="color: var(--muted); font-family: var(--mono); font-size: 12px; margin-top: 1.5rem; letter-spacing: 0.05em;">
      ✦ No MediaPipe &nbsp;·&nbsp; No OpenPose &nbsp;·&nbsp; No cloud services &nbsp;·&nbsp; No GPU required
    </p>
  </div>
</section>

<hr class="divider">

<!-- PROJECT STRUCTURE -->
<section>
  <div class="reveal">
    <p class="section-label">03 / Structure</p>
    <h2>Project layout</h2>
    <div class="file-tree">
      <div class="tree-line"><span class="tree-dir">finger-danger-zone/</span></div>
      <div class="tree-indent">
        <div class="tree-line"><span class="tree-file">├─ README.md</span></div>
        <div class="tree-line"><span class="tree-file">├─ requirements.txt</span></div>
        <div class="tree-line"><span class="tree-file">├─ packages.txt</span></div>
        <div class="tree-line"><span class="tree-file main">├─ streamlit_app.py</span> <span class="tree-comment">← entry point</span></div>
        <div class="tree-line"><span class="tree-dir">└─ src/</span></div>
        <div class="tree-indent">
          <div class="tree-line"><span class="tree-file">├─ __init__.py</span></div>
          <div class="tree-line"><span class="tree-file">├─ config.py</span> <span class="tree-comment">← thresholds & zones</span></div>
          <div class="tree-line"><span class="tree-file">├─ hand_tracking.py</span> <span class="tree-comment">← fingertip detection</span></div>
          <div class="tree-line"><span class="tree-file">├─ virtual_boundary.py</span> <span class="tree-comment">← zone logic</span></div>
          <div class="tree-line"><span class="tree-file">└─ main.py</span> <span class="tree-comment">← state machine</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- SETUP -->
<section>
  <div class="reveal">
    <p class="section-label">04 / Setup</p>
    <h2>Install & run locally</h2>

    <p style="color: var(--muted); margin-bottom: 1.5rem;">Clone the repo and get running in under two minutes.</p>

    <div class="terminal">
      <div class="term-bar">
        <div class="term-dot r"></div>
        <div class="term-dot y"></div>
        <div class="term-dot g"></div>
        <span class="term-title">terminal</span>
      </div>
      <div class="term-body">
        <div class="term-line"><span class="prompt">#</span><span class="cmd" style="color:var(--muted)"> clone the repository</span></div>
        <div class="term-line"><span class="prompt">$</span><span class="cmd"> git clone https://github.com/coderjaynt/finger-danger-zone</span></div>
        <div class="term-line"><span class="prompt">$</span><span class="cmd"> cd finger-danger-zone</span></div>
        <br>
        <div class="term-line"><span class="prompt">#</span><span class="cmd" style="color:var(--muted)"> create virtual environment</span></div>
        <div class="term-line"><span class="prompt">$</span><span class="cmd"> python -m venv .venv</span></div>
        <div class="term-line"><span class="prompt">$</span><span class="cmd"> source .venv/bin/activate</span> <span class="tree-comment"> # Windows: .\.venv\Scripts\activate</span></div>
        <br>
        <div class="term-line"><span class="prompt">#</span><span class="cmd" style="color:var(--muted)"> install dependencies</span></div>
        <div class="term-line"><span class="prompt">$</span><span class="cmd"> pip install -r requirements.txt</span></div>
        <br>
        <div class="term-line"><span class="prompt">#</span><span class="cmd" style="color:var(--muted)"> run the app</span></div>
        <div class="term-line"><span class="prompt">$</span><span class="cmd"> streamlit run streamlit_app.py</span></div>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- LIVE DEMO -->
<section>
  <div class="reveal">
    <p class="section-label">05 / Live Demo</p>
    <h2>Try it now</h2>
    <div class="demo-card">
      <div class="demo-status">
        <span class="status-dot"></span>
        LIVE · Deployed on Streamlit Cloud
      </div>
      <h3>finger-danger-zone</h3>
      <p>No install needed. Open in any browser with a webcam and start moving your finger.</p>
      <div class="demo-features">
        <span class="demo-feat">Runs fully in-browser</span>
        <span class="demo-feat">Real-time fingertip tracking</span>
        <span class="demo-feat">Virtual boundary interaction</span>
        <span class="demo-feat">CPU-only processing</span>
      </div>
      <a href="https://finger-danger-zone-rvxmehtcvory4mcnau5w6x.streamlit.app/" target="_blank" class="btn-primary">
        → Open Live App
      </a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <p>Built by <a href="https://github.com/coderjaynt">@coderjaynt</a> &nbsp;·&nbsp; OpenCV · Streamlit · WebRTC &nbsp;·&nbsp; CPU Only · No cloud · No MediaPipe</p>
</footer>

<script>
  // Scroll reveal
  const reveals = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.15 });
  reveals.forEach(el => io.observe(el));

  // Sync finger animation with label and color
  const label = document.getElementById('statusLabel');
  const circle = document.getElementById('fingerCircle');
  const DURATION = 4000;
  function updateStatus() {
    const t = (Date.now() % DURATION) / DURATION;
    let status, color;
    if (t < 0.35) { status = 'SAFE'; color = '#00c878'; }
    else if (t < 0.65) { status = 'WARNING'; color = '#ffb300'; }
    else { status = 'DANGER'; color = '#ff4444'; }
    label.textContent = status;
    label.style.color = color;
    circle.style.background = color;
    circle.style.boxShadow = `0 0 12px ${color}66`;
    requestAnimationFrame(updateStatus);
  }
  updateStatus();
</script>
</body>
</html>
