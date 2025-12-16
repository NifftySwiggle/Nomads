import re

# Read the file
with open('nomads.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New traits section content
new_section = """      <!-- TRAITS -->
      <section id="traits">
        <div class="inner">
          <div class="section-header">
            <div>
              <div class="section-tag">Traits</div>
              <h2 class="section-title">100+ Unique Attributes</h2>
            </div>
            <div class="section-subtitle">
              Each Nomad Dog is generated from over 100 unique traits across 8 categories. Every combination is randomized, creating a diverse collection of 4444 unique explorers.
            </div>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div class="card">
              <div class="card-label">Background</div>
              <h3 class="card-title">21 Variations</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">Vibrant bursts and solid colors.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Red Burst</span>
                  <span class="badge-soft">Green Burst</span>
                  <span class="badge-soft">Yellow Burst</span>
                  <span class="badge-soft">Pink Burst</span>
                  <span class="badge-soft">Purple Burst</span>
                  <span class="badge-soft">Blue Burst</span>
                  <span class="badge-soft">Solid Colors</span>
                  <span class="badge-soft">+ More</span>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-label">Body</div>
              <h3 class="card-title">7 Colors</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">Including rare Golden and White variants.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Brown</span>
                  <span class="badge-soft">Light Brown</span>
                  <span class="badge-soft">Dark Brown</span>
                  <span class="badge-soft">Grey</span>
                  <span class="badge-soft">White</span>
                  <span class="badge-soft" style="color: #FFD700;">Golden</span>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-label">Back Items</div>
              <h3 class="card-title">38 Variants</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">Tools, weapons, and gear.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Jetpack</span>
                  <span class="badge-soft">Sword</span>
                  <span class="badge-soft">Katana</span>
                  <span class="badge-soft">Plasma Rifle</span>
                  <span class="badge-soft">Backpacks</span>
                  <span class="badge-soft">Cape</span>
                  <span class="badge-soft">Rocket</span>
                  <span class="badge-soft">+ 31 More</span>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-label">Pants</div>
              <h3 class="card-title">26 Styles</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">From ancient armor to futuristic fashion.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Scientist Apron</span>
                  <span class="badge-soft">Samurai</span>
                  <span class="badge-soft">Cyberpunk</span>
                  <span class="badge-soft">Gladiator</span>
                  <span class="badge-soft">Astro</span>
                  <span class="badge-soft">Ninja</span>
                  <span class="badge-soft">Rainbow</span>
                  <span class="badge-soft">+ 19 More</span>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-label">Head</div>
              <h3 class="card-title">30 Options</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">Hats, helmets, and headgear.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Scientist</span>
                  <span class="badge-soft">Crown</span>
                  <span class="badge-soft">Gladiator</span>
                  <span class="badge-soft">Mining</span>
                  <span class="badge-soft">Pilot</span>
                  <span class="badge-soft">Detective</span>
                  <span class="badge-soft">Mayan</span>
                  <span class="badge-soft">+ 23 More</span>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-label">Neck</div>
              <h3 class="card-title">25 Accessories</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">Chains, ties, bandanas, and mystical pendants.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Gold Chain</span>
                  <span class="badge-soft">Emerald</span>
                  <span class="badge-soft">Ruby Pendant</span>
                  <span class="badge-soft">Cyber Collar</span>
                  <span class="badge-soft">Bandanas</span>
                  <span class="badge-soft">Ties</span>
                  <span class="badge-soft">+ 19 More</span>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-label">Mouth</div>
              <h3 class="card-title">26 Items</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">Items held in or around the mouth.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Pizza Slice</span>
                  <span class="badge-soft">Pipe</span>
                  <span class="badge-soft">Cigar</span>
                  <span class="badge-soft">Gas Mask</span>
                  <span class="badge-soft">Ball</span>
                  <span class="badge-soft">Teddy</span>
                  <span class="badge-soft">Scientist</span>
                  <span class="badge-soft">+ 19 More</span>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-label">Eyes</div>
              <h3 class="card-title">24 Eyewear</h3>
              <div class="card-body">
                <p style="margin-bottom: 8px;">Glasses, goggles, masks, and vision tech.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                  <span class="badge-soft">Scientist Glasses</span>
                  <span class="badge-soft">Cyber</span>
                  <span class="badge-soft">Night Vision</span>
                  <span class="badge-soft">Laser Goggles</span>
                  <span class="badge-soft">3D Glasses</span>
                  <span class="badge-soft">Gold Glasses</span>
                  <span class="badge-soft">+ 18 More</span>
                </div>
              </div>
            </div>
          </div>

          <div class="highlight-card" style="margin-top: 20px;">
            <div class="highlight-inner" style="grid-template-columns: 1fr;">
              <div class="highlight-copy">
                <div class="chip-inline">
                  <span>100+</span> Randomized Traits
                </div>
                <p>
                  Every Nomad Dog is assembled from this trait pool using randomized generation. Some traits are common, others are rare — creating natural scarcity and collectibility across the 4444 supply.
                </p>
                <p>
                  Special combinations like Scientist variants (Scientist Apron, Scientist Glasses, Scientist Mouth) create thematic sets that holders can discover and collect.
                </p>
                <div class="highlight-badges">
                  <div class="badge-soft">
                    Total Traits: <span>100+</span>
                  </div>
                  <div class="badge-soft">
                    Categories: <span>8</span>
                  </div>
                  <div class="badge-soft">
                    Rarity: <span>Natural distribution</span>
                  </div>
                  <div class="badge-soft">
                    Generation: <span>Randomized on mint</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- MINT -->"""

# Find and replace
pattern = r'<!-- TRAITS / SCIENTISTS -->.*?<!-- MINT -->'
content = re.sub(pattern, new_section, content, flags=re.DOTALL)

# Write back
with open('nomads.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Traits section updated successfully!')
