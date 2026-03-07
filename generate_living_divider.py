import math

width = 1200
height = 30

lines = []
lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" preserveAspectRatio="none">')
lines.append('<defs>')

# Multi-color neon gradient
lines.append('  <linearGradient id="neonFlow" x1="0" y1="0" x2="1" y2="0">')
lines.append('    <stop offset="0%" stop-color="#00D4FF"/>')
lines.append('    <stop offset="20%" stop-color="#FF6B6B"/>')
lines.append('    <stop offset="40%" stop-color="#FFD93D"/>')
lines.append('    <stop offset="60%" stop-color="#9B59B6"/>')
lines.append('    <stop offset="80%" stop-color="#00D4FF"/>')
lines.append('    <stop offset="100%" stop-color="#FF6B6B"/>')
lines.append('  </linearGradient>')

# Glow filter
lines.append('  <filter id="neonGlow">')
lines.append('    <feGaussianBlur stdDeviation="2" result="blur"/>')
lines.append('    <feMerge>')
lines.append('      <feMergeNode in="blur"/>')
lines.append('      <feMergeNode in="blur"/>')
lines.append('      <feMergeNode in="SourceGraphic"/>')
lines.append('    </feMerge>')
lines.append('  </filter>')

# Soft wide glow for the line
lines.append('  <filter id="wideGlow">')
lines.append('    <feGaussianBlur stdDeviation="4" result="blur"/>')
lines.append('    <feMerge>')
lines.append('      <feMergeNode in="blur"/>')
lines.append('      <feMergeNode in="SourceGraphic"/>')
lines.append('    </feMerge>')
lines.append('  </filter>')

lines.append('</defs>')

# CSS animations
lines.append('<style>')
lines.append('  @keyframes flowParticle {')
lines.append('    0% { transform: translateX(-60px); opacity: 0; }')
lines.append('    8% { opacity: 1; }')
lines.append('    92% { opacity: 1; }')
lines.append('    100% { transform: translateX(1260px); opacity: 0; }')
lines.append('  }')
lines.append('  @keyframes breathe {')
lines.append('    0%, 100% { opacity: 0.4; }')
lines.append('    50% { opacity: 1; }')
lines.append('  }')
lines.append('  @keyframes shimmer {')
lines.append('    0%, 100% { opacity: 0.15; }')
lines.append('    50% { opacity: 0.4; }')
lines.append('  }')
lines.append('</style>')

mid = height / 2

# Subtle background shimmer band
lines.append(f'<rect x="0" y="{mid - 8}" width="{width}" height="16" fill="url(#neonFlow)" rx="8" '
             f'style="animation: shimmer 5s ease-in-out infinite; opacity: 0.15;" filter="url(#wideGlow)"/>')

# Central breathing line
lines.append(f'<line x1="0" y1="{mid}" x2="{width}" y2="{mid}" '
             f'stroke="url(#neonFlow)" stroke-width="1.5" filter="url(#neonGlow)" '
             f'style="animation: breathe 3s ease-in-out infinite;"/>')

# Flowing particles — 20 particles with staggered delays
colors = ['#00D4FF', '#FF6B6B', '#FFD93D', '#9B59B6']
for i in range(20):
    delay = i * 0.4
    dur = 4.0 + (i % 4) * 0.8
    y = mid + math.sin(i * 0.85) * 4
    r = 1.0 + (i % 3) * 0.5
    c = colors[i % 4]
    lines.append(f'<circle cx="0" cy="{y:.1f}" r="{r:.1f}" fill="{c}" filter="url(#neonGlow)" '
                 f'style="animation: flowParticle {dur:.1f}s linear infinite {delay:.2f}s;"/>')

# Breathing pulse nodes at intervals along the line
for i in range(13):
    x = 50 + i * 92
    c = colors[i % 4]
    pdur = 2.0 + (i % 4) * 0.6
    pdelay = i * 0.3
    lines.append(f'<circle cx="{x}" cy="{mid}" fill="{c}" filter="url(#neonGlow)" opacity="0.4">')
    lines.append(f'  <animate attributeName="r" values="1;3.5;1" dur="{pdur:.1f}s" begin="{pdelay:.1f}s" repeatCount="indefinite"/>')
    lines.append(f'  <animate attributeName="opacity" values="0.3;1;0.3" dur="{pdur:.1f}s" begin="{pdelay:.1f}s" repeatCount="indefinite"/>')
    lines.append(f'</circle>')

lines.append('</svg>')

with open('assets/living-neural-pulse.svg', 'w') as f:
    f.write('\n'.join(lines))
print("Living Neural Pulse divider generated.")
