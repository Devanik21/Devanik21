import math

width = 1200
height = 180  # Taller for better "bending" feel

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" preserveAspectRatio="none">
<defs>
  <!-- Liquid / Gooey Filter for more "rolling" feel -->
  <filter id="liquidFlow">
    <feGaussianBlur stdDeviation="8" in="SourceGraphic" result="blur" />
    <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="liquid" />
    <feComposite in="SourceGraphic" in2="liquid" operator="atop"/>
  </filter>
  
  <linearGradient id="midnightGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0d1117" stop-opacity="0"/>
    <stop offset="40%" stop-color="#161b22" stop-opacity="0.6"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0.1"/>
  </linearGradient>

  <linearGradient id="neuralAura" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.05"/>
    <stop offset="50%" stop-color="#9B59B6" stop-opacity="0.1"/>
    <stop offset="100%" stop-color="#00D4FF" stop-opacity="0.05"/>
  </linearGradient>
</defs>

<style>
  @keyframes surf {{
    0% {{ transform: translateY(0) scaleY(1); }}
    50% {{ transform: translateY(15px) scaleY(0.9); }}
    100% {{ transform: translateY(0) scaleY(1); }}
  }}
  @keyframes flow {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(-1200px); }}
  }}
  .liquid-group {{
    filter: url(#liquidFlow);
    animation: surf 8s infinite ease-in-out;
    transform-origin: center;
  }}
  .wave-path {{
    animation: flow 40s linear infinite;
  }}
</style>

<g class="liquid-group">
'''

# Generate multiple overlapping thick liquid layers
for i in range(3):
    dur = 30 + i * 15
    offset = i * 400
    opacity = 0.5 + (i * 0.1)
    
    # Create a long continuous path for the "flowing" animation
    d = f"M -1200 {height} "
    for x in range(-1200, 1200 + 100, 100):
        y = height/2 + math.sin((x + offset) / 300 * math.pi) * 35
        d += f"L {x} {y:.1f} "
    
    # Repeat for second half to loop
    for x in range(1200, 3600 + 100, 100):
        y = height/2 + math.sin((x + offset) / 300 * math.pi) * 35
        d += f"L {x} {y:.1f} "
        
    d += f"L 3600 {height} Z"
    
    svg_content += f'''
    <path class="wave-path" d="{d}" fill="url(#midnightGrad)" style="animation-duration: {dur}s; opacity: {opacity};" />
    <path class="wave-path" d="{d}" fill="none" stroke="url(#neuralAura)" stroke-width="2" style="animation-duration: {dur}s;" />
    '''

svg_content += '''
</g>
</svg>
'''

with open('assets/digital-ocean-wave.svg', 'w') as f:
    f.write(svg_content)
print("Liquid Atmosphere Generated")
