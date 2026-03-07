import math

width, height = 1200, 500
cols, rows = 12, 12
tile_w = 40
tile_h = 20

svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
<defs>
  <style>
    @keyframes floatCube {{
      0%, 100% {{ transform: translateY(0px); opacity: 0.8; }}
      50% {{ transform: translateY(-30px); opacity: 1; }}
    }}
    @keyframes pulseHolo {{
      0%, 100% {{ opacity: 0.1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(1.1); }}
    }}
    @keyframes rayStream {{
      0% {{ stroke-dashoffset: 100; opacity: 0; }}
      50% {{ opacity: 1; }}
      100% {{ stroke-dashoffset: 0; opacity: 0; }}
    }}
    @keyframes orbitNode {{
      0% {{ transform: rotate(0deg) translateX(120px) rotate(0deg); }}
      100% {{ transform: rotate(360deg) translateX(120px) rotate(-360deg); }}
    }}
    .cube-top {{ fill: #00D4FF; stroke: #00F0FF; stroke-width: 0.5; filter: drop-shadow(0 0 4px #00D4FF); }}
    .cube-left {{ fill: #0066FF; stroke: #0088FF; stroke-width: 0.5; }}
    .cube-right {{ fill: #0a0a2e; stroke: #0033CC; stroke-width: 0.5; }}
    .cube-top-hot {{ fill: #FF6B6B; stroke: #FF9999; stroke-width: 0.5; filter: drop-shadow(0 0 6px #FF6B6B); }}
    .cube-left-hot {{ fill: #CC0000; stroke: #FF3333; stroke-width: 0.5; }}
    .cube-right-hot {{ fill: #4A0000; stroke: #880000; stroke-width: 0.5; }}
    .cube-top-gold {{ fill: #FFD93D; stroke: #FFFF99; stroke-width: 0.5; filter: drop-shadow(0 0 6px #FFD93D); }}
    .cube-left-gold {{ fill: #CC9900; stroke: #FFCC00; stroke-width: 0.5; }}
    .cube-right-gold {{ fill: #4A3300; stroke: #886600; stroke-width: 0.5; }}
    
    .holo-grid {{ stroke: #00D4FF; stroke-width: 0.5; opacity: 0.15; fill: none; }}
    .data-ray {{ stroke: #FFD93D; stroke-width: 1.5; stroke-dasharray: 20 80; opacity: 0; }}
    .core-sphere {{ fill: url(#coreGlow); filter: drop-shadow(0 0 20px #FF6B6B); }}
  </style>
  <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="30%" stop-color="#FF6B6B"/>
    <stop offset="100%" stop-color="#0a0a2e" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="{width}" height="{height}" fill="#050510" rx="12"/>

<!-- Holographic rings behind -->
<g transform="translate({width/2}, {height/2})">
  <ellipse cx="0" cy="0" rx="400" ry="150" stroke="#00D4FF" fill="none" class="holo-grid" style="animation: pulseHolo 8s infinite;" />
  <ellipse cx="0" cy="0" rx="300" ry="110" stroke="#FF6B6B" fill="none" class="holo-grid" stroke-dasharray="10 5" style="animation: pulseHolo 6s infinite 1s;" />
  <ellipse cx="0" cy="0" rx="200" ry="70" stroke="#FFD93D" fill="none" class="holo-grid" style="animation: pulseHolo 4s infinite 2s;" />
  
  <circle cx="0" cy="-50" r="80" class="core-sphere" style="animation: floatCube 4s infinite ease-in-out alternate;" />
  <text y="0" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" fill="#fff" letter-spacing="4px" opacity="0.6">SINGULARITY</text>
  
  <!-- Orbiting Nodes -->
  <g style="animation: orbitNode 12s linear infinite;">
     <circle cx="0" cy="0" r="4" fill="#00D4FF" filter="drop-shadow(0 0 5px #00D4FF)" />
     <path d="M0,0 L0,50" stroke="#00D4FF" stroke-dasharray="2 2" opacity="0.4" />
  </g>
  <g style="animation: orbitNode 8s linear infinite reverse;">
     <circle cx="0" cy="0" r="3" fill="#FFD93D" filter="drop-shadow(0 0 5px #FFD93D)" />
  </g>
</g>
'''

svg_cubes = ""
import random
random.seed(42)  # For reproducible masterpiece

# Calculate starting point so grid is centered
cx = width / 2
cy = height / 2 + 100

def draw_cube(x, y, level, typeStr, delay):
    # center is x, y. Cube height depends on level
    top_y = y - level * 20
    
    top_pts = f"{x},{top_y - tile_h} {x + tile_w},{top_y} {x},{top_y + tile_h} {x - tile_w},{top_y}"
    left_pts = f"{x - tile_w},{top_y} {x},{top_y + tile_h} {x},{y + tile_h} {x - tile_w},{y}"
    right_pts = f"{x},{top_y + tile_h} {x + tile_w},{top_y} {x + tile_w},{y} {x},{y + tile_h}"
    
    t_c = f"cube-top{typeStr}"
    l_c = f"cube-left{typeStr}"
    r_c = f"cube-right{typeStr}"
    
    anim = f"animation: floatCube {3 + random.uniform(0,3):.1f}s infinite ease-in-out {delay}s alternate;"
    
    return f'''
    <g style="{anim}">
      <polygon points="{left_pts}" class="{l_c}" />
      <polygon points="{right_pts}" class="{r_c}" />
      <polygon points="{top_pts}" class="{t_c}" />
      <!-- Data Ray streaming up -->
      <line x1="{x}" y1="{top_y}" x2="{x}" y2="{top_y - 120}" class="data-ray" style="animation: rayStream {2 + random.uniform(0,2):.1f}s infinite linear {random.uniform(0,3):.1f}s;" />
    </g>
    '''

# Generate isometric grid sorted by drawing order (back to front)
cubes = []
for r in range(rows):
    for c in range(cols):
        # Dist from center
        dist = math.sqrt((r - rows/2)**2 + (c - cols/2)**2)
        if dist > 6:
            continue
            
        hx = cx + (c - r) * tile_w
        hy = cy + (c + r) * (tile_h / 2)
        
        # Level based on something like a sine wave + randomness
        base = max(0, 5 - dist*0.8)
        level = base + random.uniform(0, 1.5)
        
        mod = random.random()
        typeS = ""
        if mod > 0.8: typeS = "-hot"
        elif mod > 0.6: typeS = "-gold"
        
        delay = random.uniform(0, 4)
        
        cubes.append((r+c, hx, hy, level, typeS, delay))

cubes.sort(key=lambda x: x[0]) # draw order from back to front

for c in cubes:
    svg_cubes += draw_cube(c[1], c[2]-120, c[3], c[4], c[5]) # shifted up slightly

svg_footer = "</svg>"

with open('c:\\AGI\\assets\\quantum-singularity.svg', 'w') as f:
    f.write(svg_header + svg_cubes + svg_footer)
print("Generated quantum-singularity.svg")
