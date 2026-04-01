import re

base_file = "/Users/eliainnamorati/Desktop/ALBA WEBSITE/about.html"
credit_file = "/Users/eliainnamorati/Desktop/ALBA WEBSITE/credit-opportunities.html"
private_file = "/Users/eliainnamorati/Desktop/ALBA WEBSITE/private-wealth.html"

with open(base_file, "r") as f:
    template = f.read()

# Replace <title>
def generate_page(target_path, title_text, hero_payload, body_payload):
    html = template[:]
    html = re.sub(r'<title>.*?</title>', f'<title>{title_text}</title>', html)
    html = re.sub(r'<!-- Static Partial-Height Hero Section -->.*?<section class="newsletter-section">', f'<!-- Static Partial-Height Hero Section -->\n{hero_payload}\n{body_payload}\n<section class="newsletter-section">', html, flags=re.DOTALL)
    # Wipe the parallax/timeline JS since we deleted the DOM nodes for those pages
    html = re.sub(r'// Dynamic Timeline Logic.*?const navbar = document.getElementById', 'const navbar = document.getElementById', html, flags=re.DOTALL)
    html = re.sub(r'// Team Sketch Zoom Frame Loop.*?const navbar =', 'const navbar =', html, flags=re.DOTALL)
    with open(target_path, "w") as f:
        f.write(html)

credit_hero = """
    <div class="hero-container" id="hero-section" style="height: 70vh; min-height: 500px;">
        <div class="hero-sticky" style="height: 70vh; min-height: 500px; position: relative;">
            <div class="hero-bg" style="background-image: url('map.jpg'); background-position: center 25%; background-size: cover;">
                <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(11, 17, 14, 0.75);"></div>
            </div>
            <div class="hero-content" style="pointer-events: auto;">
                <div class="initial-content fade-up" style="bottom: 15vh;">
                    <h1 style="font-size: 4.5rem; opacity: 1; margin-bottom: 20px;">Alba Credit Opportunities</h1>
                    <p style="font-size: 1.5rem; font-weight: 300; max-width: 800px; margin-bottom: 20px;">A long/short credit strategy focused on liquid global credit opportunities.</p>
                    <p style="font-size: 1.15rem; color: rgba(255,255,255,0.7); max-width: 800px; line-height: 1.6; margin-bottom: 40px; font-family: -apple-system, sans-serif;">We invest across the credit spectrum to capture mispricing, market dislocations, and catalyst-driven opportunities while actively managing risk across market cycles.</p>
                    <a href="mailto:info@albapartners.com" class="newsletter-btn" style="text-decoration: none; display: inline-block; padding: 15px 30px; letter-spacing: 2px; text-transform: uppercase; font-size: 0.85rem;">Request Information</a>
                </div>
            </div>
        </div>
    </div>
"""

credit_body = """
    <!-- Strategy Overview Section -->
    <div class="normal-section fade-up delay-1" style="padding: 15vh 10%;">
        <div style="display: flex; gap: 80px; flex-wrap: wrap;">
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem;">Strategy<br>Overview</h2>
            </div>
            <div style="flex: 2 1 600px;">
                <p class="section-desc fade-up" style="opacity:1; transform:none;">Alba Credit Opportunities is a long/short credit strategy investing in liquid corporate and financial credit globally with a European bias. The strategy combines bottom-up fundamental credit analysis with top-down macro positioning to identify asymmetric risk-return opportunities across the capital structure.</p>
            </div>
        </div>
    </div>

    <!-- Investment Approach Section -->
    <div class="normal-section" style="background-color: #1a3622; color: #ffffff; padding: 15vh 10%;">
        <div style="display: flex; gap: 80px; flex-wrap: wrap-reverse;">
            <div style="flex: 2 1 600px;">
                <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px;">
                    <li style="font-size: 1.2rem; color: rgba(255,255,255,0.8);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Bottom-up fundamental credit research</li>
                    <li style="font-size: 1.2rem; color: rgba(255,255,255,0.8);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Top-down macro positioning</li>
                    <li style="font-size: 1.2rem; color: rgba(255,255,255,0.8);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Relative value and dislocation opportunities</li>
                    <li style="font-size: 1.2rem; color: rgba(255,255,255,0.8);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Catalyst-driven investments</li>
                    <li style="font-size: 1.2rem; color: rgba(255,255,255,0.8);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Active risk management</li>
                    <li style="font-size: 1.2rem; color: rgba(255,255,255,0.8);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>FX and interest rate hedging</li>
                </ul>
            </div>
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem; color: #ffffff;">Investment<br>Approach</h2>
            </div>
        </div>
    </div>

    <!-- Portfolio Construction & Key Characteristics Sections -->
    <div class="normal-section" style="padding: 15vh 10%;">
        <div style="display: flex; gap: 80px; flex-wrap: wrap; margin-bottom: 15vh;">
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem;">Portfolio<br>Construction</h2>
            </div>
            <div style="flex: 2 1 600px;">
                <p class="section-desc" style="opacity:1; transform:none;">The portfolio is built around a concentrated set of high-conviction positions, typically across 25–35 capital structures. The strategy focuses on diversification across issuers, sectors, and risk factors while maintaining flexibility to adjust exposure through derivatives.</p>
            </div>
        </div>
        
        <div style="height: 1px; width: 100%; background: rgba(0,0,0,0.1); margin-bottom: 15vh;"></div>

        <div style="display: flex; gap: 80px; flex-wrap: wrap;">
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem;">Key<br>Characteristics</h2>
            </div>
            <div style="flex: 2 1 600px;">
                <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px;">
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><strong style="color: var(--text-main); display: block; margin-bottom: 8px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px;">Strategy</strong>Long / Short Credit Strategy</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><strong style="color: var(--text-main); display: block; margin-bottom: 8px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px;">Focus</strong>Global Liquid Credit</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><strong style="color: var(--text-main); display: block; margin-bottom: 8px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px;">Bias</strong>European Bias</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><strong style="color: var(--text-main); display: block; margin-bottom: 8px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px;">Leverage</strong>Moderate Leverage</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><strong style="color: var(--text-main); display: block; margin-bottom: 8px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px;">Management</strong>Active Risk Management</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><strong style="color: var(--text-main); display: block; margin-bottom: 8px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px;">Returns</strong>Target Returns: Low Teens</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><strong style="color: var(--text-main); display: block; margin-bottom: 8px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px;">Volatility</strong>Controlled Volatility</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- CTA Section -->
    <div class="normal-section" style="padding: 15vh 10%; background: #050505; color: #fff; text-align: center;">
        <h2 style="font-size: 4rem; color: #fff; margin-bottom: 25px;">Learn More</h2>
        <p style="font-size: 1.25rem; font-weight: 300; color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto 50px;">Contact us for further information or access to fund documentation.</p>
        <a href="mailto:info@albapartners.com" class="newsletter-btn" style="text-decoration: none; display: inline-block; padding: 18px 40px; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; border: 1px solid var(--gold); border-radius: 4px; background: transparent; color: var(--gold);">Contact Us</a>
    </div>
"""

private_hero = """
    <div class="hero-container" id="hero-section" style="height: 70vh; min-height: 500px;">
        <div class="hero-sticky" style="height: 70vh; min-height: 500px; position: relative;">
            <div class="hero-bg" style="background-image: url('map.jpg'); background-position: center top; background-size: cover; filter: grayscale(100%);">
                <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(30, 54, 45, 0.85);"></div>
            </div>
            <div class="hero-content" style="pointer-events: auto;">
                <div class="initial-content fade-up" style="bottom: 15vh;">
                    <h1 style="font-size: 4.5rem; opacity: 1; margin-bottom: 20px;">Private Wealth &<br>Multi-Family Office</h1>
                    <p style="font-size: 1.5rem; font-weight: 300; max-width: 800px; margin-bottom: 20px;">Independent asset management and tailored investment solutions.</p>
                    <p style="font-size: 1.15rem; color: rgba(255,255,255,0.7); max-width: 800px; line-height: 1.6; margin-bottom: 40px; font-family: -apple-system, sans-serif;">We provide independent wealth management, asset allocation, and investment advisory services tailored to entrepreneurs, families, and private investors.</p>
                    <a href="mailto:info@albapartners.com" class="newsletter-btn" style="text-decoration: none; display: inline-block; padding: 15px 30px; letter-spacing: 2px; text-transform: uppercase; font-size: 0.85rem;">Get in Touch</a>
                </div>
            </div>
        </div>
    </div>
"""

private_body = """
    <!-- Our Approach Section -->
    <div class="normal-section fade-up delay-1" style="padding: 15vh 10%;">
        <div style="display: flex; gap: 80px; flex-wrap: wrap;">
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem;">Our<br>Approach</h2>
            </div>
            <div style="flex: 2 1 600px;">
                <p class="section-desc" style="opacity:1; transform:none;">We focus on long-term asset allocation, diversification, and risk management. As an independent asset manager, we select investments and managers without conflicts of interest, always focusing on after-fee performance and capital preservation.</p>
            </div>
        </div>
    </div>

    <!-- Asset Allocation Section -->
    <div class="normal-section" style="background-color: #f7f7f7; padding: 15vh 10%;">
        <div style="display: flex; gap: 80px; flex-wrap: wrap-reverse;">
            <div style="flex: 2 1 600px;">
                <p class="section-desc" style="opacity:1; transform:none;">We construct portfolios across fixed income, equities, and alternative investments based on each client’s risk profile, liquidity needs, and long-term objectives. Strategic and tactical asset allocation form the foundation of portfolio construction.</p>
            </div>
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem;">Asset<br>Allocation</h2>
            </div>
        </div>
    </div>

    <!-- Our Services Section -->
    <div class="normal-section" style="padding: 15vh 10%;">
        <div style="display: flex; gap: 80px; flex-wrap: wrap; margin-bottom: 15vh;">
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem;">Our<br>Services</h2>
            </div>
            <div style="flex: 2 1 600px;">
                <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px;">
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Investment Management</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Asset Allocation</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Portfolio Construction</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Risk Management</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Alternative Investments</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Liquidity Event Planning</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Bank Selection & Coordination</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary);"><span style="color: var(--gold); margin-right: 15px;">&#x2726;</span>Family Office Governance</li>
                </ul>
            </div>
        </div>
        
        <div style="height: 1px; width: 100%; background: rgba(0,0,0,0.1); margin-bottom: 15vh;"></div>

        <div style="display: flex; gap: 80px; flex-wrap: wrap;">
            <div style="flex: 1 1 350px;">
                <h2 style="font-size: 3.5rem;">Investment<br>Philosophy</h2>
            </div>
            <div style="flex: 2 1 600px;">
                <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: 1fr; gap: 20px;">
                    <li style="font-size: 1.15rem; color: var(--text-secondary); display:flex; align-items:flex-start;"><span style="color: var(--gold); margin-right: 15px; margin-top:2px;">&#x2713;</span>Active management in fixed income and credit</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary); display:flex; align-items:flex-start;"><span style="color: var(--gold); margin-right: 15px; margin-top:2px;">&#x2713;</span>Passive exposure in equities where appropriate</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary); display:flex; align-items:flex-start;"><span style="color: var(--gold); margin-right: 15px; margin-top:2px;">&#x2713;</span>Best-in-class alternative investments</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary); display:flex; align-items:flex-start;"><span style="color: var(--gold); margin-right: 15px; margin-top:2px;">&#x2713;</span>Independent and conflict-free advice</li>
                    <li style="font-size: 1.15rem; color: var(--text-secondary); display:flex; align-items:flex-start;"><span style="color: var(--gold); margin-right: 15px; margin-top:2px;">&#x2713;</span>Long-term wealth preservation and growth</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- CTA Section -->
    <div class="normal-section" style="padding: 15vh 10%; background: #050505; color: #fff; text-align: center;">
        <h2 style="font-size: 4rem; color: #fff; margin-bottom: 25px;">Work With Us</h2>
        <p style="font-size: 1.25rem; font-weight: 300; color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto 50px;">Contact us to discuss your investment and wealth management needs.</p>
        <a href="mailto:info@albapartners.com" class="newsletter-btn" style="text-decoration: none; display: inline-block; padding: 18px 40px; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; border: 1px solid var(--gold); border-radius: 4px; background: transparent; color: var(--gold);">Contact Us</a>
    </div>
"""

generate_page(credit_file, "Alba Investment Partners - Credit Opportunities", credit_hero, credit_body)
generate_page(private_file, "Alba Investment Partners - Private Wealth & MFO", private_hero, private_body)
print("done")
