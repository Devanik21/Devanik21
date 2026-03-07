import math

width = 1200
height = 80

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
<defs>
  <style>
'''

num_waves = 10
for i in range(num_waves):
    direction = "Left" if i % 2 == 0 else "Right"
    dur = 30 + i * 8
    svg_content += f'''
    @keyframes move{i} {{
      0% {{ transform: translateX({'0' if direction == "Left" else '-'+str(width)+'px'}); }}
      100% {{ transform: translateX({'-'+str(width)+'px' if direction == "Left" else '0px'}); }}
    }}
    .wave{i} {{
      animation: move{i} {dur}s linear infinite;
    }}
'''

svg_content += '''
  </style>
  <linearGradient id="waveGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.3"/>
    <stop offset="60%" stop-color="#9B59B6" stop-opacity="0.1"/>
    <stop offset="100%" stop-color="#050510" stop-opacity="0"/>
  </linearGradient>
</defs>
<g opacity="1.0">
'''

for i in range(num_waves):
    amp = 8 + i * 1.5
    y_center = height / 2.5 + (i - num_waves/2) * 1.5
    
    p1 = 1 + (i % 3)
    p2 = 1 + ((i+1) % 4)
    
    d = f"M 0 {height} "
    for x in range(0, 2400 + 20, 20):
        y = y_center + math.sin(x / width * p1 * 2 * math.pi) * amp
        y += math.sin(x / width * p2 * 2 * math.pi) * (amp * 0.4)
        d += f"L {x} {y:.1f} "
    
    d += f"L 2400 {height} Z"
    stroke_opacity = 0.2 + (i / num_waves) * 0.3
    svg_content += f'  <path class="wave{i}" d="{d}" fill="url(#waveGrad)" stroke="rgba(0, 212, 255, {stroke_opacity})" stroke-width="1.0" />\n'

svg_content += '''
</g>
</svg>
'''

with open('assets/digital-ocean-wave.svg', 'w') as f:
    f.write(svg_content)
print("done")
