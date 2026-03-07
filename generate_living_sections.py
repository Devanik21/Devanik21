"""
Generate living, breathing SVG sections using foreignObject.
These SVGs embed HTML+CSS with animations so the content itself floats and breathes.
"""

import math


def generate_living_hero():
    """Hero section: name, designation, and a tagline floating on a wave."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 280" width="100%">
<style>
  @keyframes gentleFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
  }
  @keyframes breathe {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 1; }
  }
  @keyframes slowSway {
    0%, 100% { transform: translateX(0px) translateY(0px); }
    25% { transform: translateX(3px) translateY(-5px); }
    75% { transform: translateX(-3px) translateY(-3px); }
  }
  @keyframes pulseGlow {
    0%, 100% { filter: drop-shadow(0 0 8px rgba(0,212,255,0.3)); }
    50% { filter: drop-shadow(0 0 20px rgba(0,212,255,0.6)); }
  }
  @keyframes waveFlow {
    from { transform: translateX(0); }
    to { transform: translateX(-800px); }
  }
  @keyframes particleDrift {
    0% { transform: translateY(0) translateX(0); opacity: 0; }
    10% { opacity: 0.6; }
    90% { opacity: 0.6; }
    100% { transform: translateY(-250px) translateX(40px); opacity: 0; }
  }
</style>
<defs>
  <linearGradient id="heroBg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0a0a1a" stop-opacity="0.95"/>
    <stop offset="100%" stop-color="#0d1117" stop-opacity="0.98"/>
  </linearGradient>
  <linearGradient id="waveGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#9B59B6" stop-opacity="0.03"/>
  </linearGradient>
  <linearGradient id="waveStroke" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.15"/>
    <stop offset="50%" stop-color="#9B59B6" stop-opacity="0.25"/>
    <stop offset="100%" stop-color="#00D4FF" stop-opacity="0.15"/>
  </linearGradient>
</defs>

<!-- Background -->
<rect width="800" height="280" fill="url(#heroBg)" rx="12"/>

<!-- Animated wave background layers -->'''

    # Generate wave paths
    for i, (amp, freq, dur, opacity) in enumerate([
        (12, 300, 20, 0.5), (15, 250, 15, 0.6), (10, 350, 25, 0.4)
    ]):
        d = f"M -800 280 "
        y_base = 220 + i * 15
        for x in range(-800, 1601, 30):
            y = y_base + amp * math.sin((x + i * 200) / freq * math.pi)
            y += amp * 0.3 * math.sin(x / 80 * math.pi)
            d += f"L {x} {y:.1f} "
        d += f"L 1600 280 Z"
        svg += f'\n<path d="{d}" fill="url(#waveGrad)" stroke="url(#waveStroke)" stroke-width="0.8" style="animation: waveFlow {dur}s linear infinite;"/>'

    # Floating particles
    particles = [
        (100, 260, 12, 0.0), (250, 270, 15, 1.5), (400, 255, 10, 3.0),
        (550, 265, 13, 4.5), (700, 258, 11, 6.0), (180, 268, 14, 2.0),
        (620, 262, 16, 5.0), (350, 275, 9, 7.0),
    ]
    colors = ['#00D4FF', '#FF6B6B', '#FFD93D', '#9B59B6']
    for idx, (px, py, dur, delay) in enumerate(particles):
        c = colors[idx % 4]
        svg += f'\n<circle cx="{px}" cy="{py}" r="1.5" fill="{c}" style="animation: particleDrift {dur}s ease-in-out infinite {delay}s;"/>'

    svg += '''

<!-- Living content via foreignObject -->
<foreignObject x="0" y="0" width="800" height="280">
  <div xmlns="http://www.w3.org/1999/xhtml" style="
    width: 100%; height: 100%;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    color: #ffffff; text-align: center;
    box-sizing: border-box; padding: 20px;
  ">
    <!-- Name -->
    <div style="animation: gentleFloat 6s ease-in-out infinite; margin-bottom: 8px;">
      <div style="
        font-size: 38px; font-weight: 900;
        letter-spacing: 8px;
        background: linear-gradient(135deg, #00D4FF, #FF6B6B, #FFD93D, #9B59B6);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: pulseGlow 4s ease-in-out infinite;
      ">DΞVΛΠIK</div>
    </div>

    <!-- Designation -->
    <div style="animation: slowSway 8s ease-in-out infinite; margin-bottom: 12px;">
      <div style="
        font-size: 13px; letter-spacing: 5px;
        color: #00D4FF; opacity: 0.8;
        text-transform: uppercase;
        animation: breathe 3s ease-in-out infinite;
      ">Artificial Intelligence Researcher</div>
    </div>

    <!-- Tagline -->
    <div style="animation: gentleFloat 7s ease-in-out infinite 1s;">
      <div style="
        font-size: 11px; letter-spacing: 3px;
        color: #9B59B6; opacity: 0.6;
        font-style: italic;
      ">Neural Network Architect · Quantum Learning Researcher · Synthetic Intelligence Pioneer</div>
    </div>

    <!-- Fellowship badge -->
    <div style="animation: slowSway 9s ease-in-out infinite 0.5s; margin-top: 16px;">
      <div style="
        display: inline-block;
        background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(155,89,182,0.15));
        border: 1px solid rgba(0,212,255,0.2);
        border-radius: 20px; padding: 6px 18px;
        font-size: 10px; letter-spacing: 3px;
        color: #FFD93D; animation: breathe 5s ease-in-out infinite 1s;
      ">☆ SAMSUNG FELLOW @ IISc BANGALORE · ECE @ NIT AGARTALA ☆</div>
    </div>
  </div>
</foreignObject>
</svg>'''
    return svg


def generate_living_philosophy():
    """Philosophy section: quotes gently swaying like underwater."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 220" width="100%">
<style>
  @keyframes swayLeft {
    0%, 100% { transform: translateX(0) translateY(0); }
    33% { transform: translateX(-4px) translateY(-3px); }
    66% { transform: translateX(3px) translateY(-5px); }
  }
  @keyframes swayRight {
    0%, 100% { transform: translateX(0) translateY(0); }
    33% { transform: translateX(4px) translateY(-4px); }
    66% { transform: translateX(-3px) translateY(-2px); }
  }
  @keyframes breatheQuote {
    0%, 100% { opacity: 0.75; }
    50% { opacity: 1; }
  }
  @keyframes glowPulse {
    0%, 100% { opacity: 0.1; }
    50% { opacity: 0.25; }
  }
</style>
<defs>
  <linearGradient id="philoBg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0a0a1a"/>
    <stop offset="100%" stop-color="#0d1117"/>
  </linearGradient>
  <radialGradient id="aura1" cx="25%" cy="50%">
    <stop offset="0%" stop-color="#FF6B6B" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#0a0a1a" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="aura2" cx="75%" cy="50%">
    <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#0a0a1a" stop-opacity="0"/>
  </radialGradient>
</defs>

<rect width="800" height="220" fill="url(#philoBg)" rx="12"/>
<!-- Breathing auras behind each quote -->
<rect width="800" height="220" fill="url(#aura1)" rx="12" style="animation: glowPulse 6s ease-in-out infinite;"/>
<rect width="800" height="220" fill="url(#aura2)" rx="12" style="animation: glowPulse 6s ease-in-out infinite 3s;"/>

<foreignObject x="0" y="0" width="800" height="220">
  <div xmlns="http://www.w3.org/1999/xhtml" style="
    width: 100%; height: 100%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Segoe UI', Georgia, serif;
    color: #ffffff; text-align: center;
    box-sizing: border-box; padding: 20px;
    gap: 30px;
  ">
    <!-- Left quote -->
    <div style="
      flex: 1; animation: swayLeft 10s ease-in-out infinite;
      padding: 15px; max-width: 340px;
    ">
      <div style="
        font-size: 10px; letter-spacing: 4px; color: #FF6B6B;
        text-transform: uppercase; margin-bottom: 10px;
        animation: breatheQuote 4s ease-in-out infinite;
      ">◈ CORE BELIEF ◈</div>
      <div style="
        font-size: 13px; line-height: 1.6;
        color: rgba(255,255,255,0.85); font-style: italic;
        animation: breatheQuote 5s ease-in-out infinite 0.5s;
      ">"AI, when harnessed correctly, can increase human lifespan to infinity. The convergence of machine learning and biotechnology holds the key to transcending biological limitations."</div>
    </div>

    <!-- Divider -->
    <div style="width: 1px; height: 80px; background: linear-gradient(to bottom, transparent, #9B59B6, transparent); opacity: 0.4;"></div>

    <!-- Right quote -->
    <div style="
      flex: 1; animation: swayRight 10s ease-in-out infinite;
      padding: 15px; max-width: 340px;
    ">
      <div style="
        font-size: 10px; letter-spacing: 4px; color: #00D4FF;
        text-transform: uppercase; margin-bottom: 10px;
        animation: breatheQuote 4s ease-in-out infinite 1s;
      ">◈ MISSION ◈</div>
      <div style="
        font-size: 13px; line-height: 1.6;
        color: rgba(255,255,255,0.85); font-style: italic;
        animation: breatheQuote 5s ease-in-out infinite 1.5s;
      ">"To architect AI systems that don't just process data, but understand, empathize, and elevate human potential across all dimensions of existence."</div>
    </div>
  </div>
</foreignObject>
</svg>'''
    return svg


def generate_living_signoff():
    """Sign-off section: the closing manifesto pulsing with life."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 240" width="100%">
<style>
  @keyframes floatUp {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }
  @keyframes breatheSlow {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
  }
  @keyframes glowRotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  @keyframes borderPulse {
    0%, 100% { border-color: rgba(0,212,255,0.2); }
    50% { border-color: rgba(0,212,255,0.5); }
  }
</style>
<defs>
  <linearGradient id="signBg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0d1117"/>
    <stop offset="100%" stop-color="#0a0a1a"/>
  </linearGradient>
  <radialGradient id="centerGlow">
    <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.06"/>
    <stop offset="100%" stop-color="#0a0a1a" stop-opacity="0"/>
  </radialGradient>
</defs>

<rect width="800" height="240" fill="url(#signBg)" rx="12"/>
<ellipse cx="400" cy="120" rx="300" ry="100" fill="url(#centerGlow)" style="animation: breatheSlow 6s ease-in-out infinite;"/>

<!-- Orbiting ring -->
<g style="transform-origin: 400px 120px; animation: glowRotate 30s linear infinite;">
  <ellipse cx="400" cy="120" rx="250" ry="80" fill="none" stroke="#00D4FF" stroke-width="0.5" stroke-opacity="0.1" stroke-dasharray="8 12"/>
</g>
<g style="transform-origin: 400px 120px; animation: glowRotate 20s linear infinite reverse;">
  <ellipse cx="400" cy="120" rx="200" ry="60" fill="none" stroke="#9B59B6" stroke-width="0.5" stroke-opacity="0.08" stroke-dasharray="5 10"/>
</g>

<foreignObject x="0" y="0" width="800" height="240">
  <div xmlns="http://www.w3.org/1999/xhtml" style="
    width: 100%; height: 100%;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    font-family: 'Courier New', 'Consolas', monospace;
    color: #ffffff; text-align: center;
    box-sizing: border-box; padding: 20px;
  ">
    <!-- Manifesto lines -->
    <div style="animation: floatUp 5s ease-in-out infinite; margin-bottom: 6px;">
      <div style="
        font-size: 12px; letter-spacing: 2px;
        color: #00D4FF;
        animation: breatheSlow 4s ease-in-out infinite;
      ">"I am not just writing code. I am encoding consciousness."</div>
    </div>

    <div style="animation: floatUp 6s ease-in-out infinite 0.8s; margin-bottom: 6px;">
      <div style="
        font-size: 12px; letter-spacing: 2px;
        color: #FF6B6B;
        animation: breatheSlow 4s ease-in-out infinite 1s;
      ">"Every algorithm is a step toward understanding reality."</div>
    </div>

    <div style="animation: floatUp 7s ease-in-out infinite 1.6s; margin-bottom: 16px;">
      <div style="
        font-size: 12px; letter-spacing: 2px;
        color: #FFD93D;
        animation: breatheSlow 4s ease-in-out infinite 2s;
      ">"The singularity isn't coming. We're building it."</div>
    </div>

    <!-- Final tagline -->
    <div style="animation: floatUp 8s ease-in-out infinite 0.5s;">
      <div style="
        font-size: 11px; letter-spacing: 4px;
        color: #9B59B6; font-style: italic;
        animation: breatheSlow 6s ease-in-out infinite;
      ">Transforming data into intelligence, algorithms into consciousness</div>
    </div>

    <div style="animation: breatheSlow 8s ease-in-out infinite 2s; margin-top: 12px;">
      <div style="
        font-size: 9px; letter-spacing: 2px;
        color: rgba(255,255,255,0.35); font-style: italic;
      ">This README is a living document. Like biological organisms, it evolves, adapts, and grows.</div>
    </div>
  </div>
</foreignObject>
</svg>'''
    return svg


# ── Generate all living sections ──
sections = {
    'assets/living-hero.svg': generate_living_hero(),
    'assets/living-philosophy.svg': generate_living_philosophy(),
    'assets/living-signoff.svg': generate_living_signoff(),
}

for path, content in sections.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {path}")

print("All living sections generated.")
