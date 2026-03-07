import os

dragon_pixels = [
    "............................................",
    "............................................",
    ".......................33...................",
    "......................3223..................",
    ".....................32223..................",
    "....................322223..................",
    "....................322223..................",
    "....................3132223.................",
    "..........4.........3332223.................",
    ".........444.........32223..................",
    ".......444544.......322223.......33.........",
    "......44555544......322223......3223........",
    ".......444544.......3222223....32223........",
    ".........444.......322222233..322223........",
    "..........4........32222222333222223........",
    "...................32222222232222223........",
    "..................322222222222222223........",
    ".................3222222222222222223........",
    ".................322222222233222233.........",
    "..................322222223..3223...........",
    "...................3322223....33............",
    ".....................3333...................",
    "............................................",
    "............................................",
]

# We want a more detailed pixel dragon
advanced_dragon = """
                  @@@@                  
                 @@  @@                 
          @@@@@@@@    @@                
         @@      @@  @@@@@@             
        @@  @@@@  @@@@    @@            
       @@  @@  @@  @@     @@            
      @@   @@  @@  @@    @@             
      @@    @@@@   @@   @@              
     @@            @@  @@               
     @@  @@@@@@@@@@    @@               
    @@  @@        @@@@@@                
    @@ @@               @@@@            
   @@ @@                    @@          
   @@ @@  @@@@@@              @@        
  @@  @@@@     @@               @@      
  @@   @@       @@ @@           @@      
 @@             @@@@  @@        @@      
 @@             @@   @@  @@    @@       
 @@            @@   @@    @@@@@@        
 @@           @@    @@                  
  @@         @@    @@                   
   @@@@@@@@@@@@@@@@@                    
"""

svg_header = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
<defs>
  <filter id="glow">
    <feGaussianBlur stdDeviation="2" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<style>
  .pixel { filter: url(#glow); }
  @keyframes breathe {
     0%, 100% { transform: translateY(0); }
     50% { transform: translateY(-5px); }
  }
  .dragon { animation: breathe 3s infinite ease-in-out; transform-origin: center; }
  @keyframes fireFlash {
     0%, 100% { fill: #ff0000; opacity: 0.7; }
     50% { fill: #ffff00; opacity: 1; }
  }
  .fire { animation: fireFlash 0.5s infinite; }
</style>
<rect width="400" height="300" fill="#0d1117" rx="10"/>
<g class="dragon" transform="translate(50, 20) scale(8)">
'''

svg_body = ""
lines = advanced_dragon.strip("\n").split("\n")
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '@':
            # Add some color variation
            color = "#00D4FF"
            svg_body += f'  <rect x="{x}" y="{y}" width="1.1" height="1.1" fill="{color}" class="pixel"/>\n'

svg_footer = '''
</g>
</svg>
'''

with open('c:\\AGI\\test_dragon.svg', 'w') as f:
    f.write(svg_header + svg_body + svg_footer)
print("done")
