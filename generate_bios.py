import re
import os

# Read the base template to get head, navbar, and footer
with open('/Users/eliainnamorati/Desktop/ALBA WEBSITE/index.html', 'r') as f:
    base_html = f.read()

# Extract Head & Navbar (Everything before <!-- Sticky Scrollytelling Hero Section -->)
head_nav_match = re.search(r'(.*?)(?=<!-- Sticky Scrollytelling Hero Section -->)', base_html, re.DOTALL)
if not head_nav_match:
    print("Could not find Hero Section in index.html")
    exit(1)
head_nav = head_nav_match.group(1)

# Extract Footer & Scripts (Everything after <!-- Modern Green Footer -->)
footer_scripts_match = re.search(r'(<!-- Modern Green Footer -->.*)', base_html, re.DOTALL)
if not footer_scripts_match:
    print("Could not find Footer in index.html")
    exit(1)
footer_scripts = footer_scripts_match.group(1)

# Add custom bio styles to head
custom_styles = '''
    <style>
        .bio-container { display: flex; min-height: 100vh; padding-top: 108px; background: #fff; }
        .bio-image-col { flex: 0 0 45%; position: relative; background: #f5f5f5; }
        .bio-image-col img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; }
        .bio-content-col { flex: 1; padding: 80px 8%; display: flex; flex-direction: column; justify-content: center; }
        .bio-back { font-family: 'Inter', sans-serif; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; color: var(--text-secondary); text-decoration: none; margin-bottom: 40px; display: inline-flex; align-items: center; gap: 10px; transition: color 0.3s ease; }
        .bio-back:hover { color: var(--accent); }
        .bio-name { font-family: 'Aperto', 'Georgia', serif; font-size: 3.5rem; color: #1e362d; margin: 0 0 15px 0; font-weight: 400; line-height: 1.1; }
        .bio-title { font-family: 'Inter', sans-serif; font-size: 0.85rem; font-weight: 500; text-transform: uppercase; letter-spacing: 2.5px; color: #9b2226; margin-bottom: 50px; }
        .bio-text p { font-family: 'Inter', sans-serif; font-size: 1.1rem; color: #333; line-height: 1.8; font-weight: 300; margin-bottom: 25px; }
        @media (max-width: 991px) {
            .bio-container { flex-direction: column; padding-top: 70px; }
            .bio-image-col { height: 60vh; flex: none; }
            .bio-content-col { padding: 60px 5%; }
            .bio-name { font-size: 2.5rem; }
        }
    </style>
</head>'''

head_nav = head_nav.replace('</head>', custom_styles)

# We need the navbar to be in light mode (green text, dark logo) because background is white
head_nav = head_nav.replace('id="navbar"', 'id="navbar" data-light-page="true" class="navbar-scrolled"')

team_data = [
    {
        'file': 'stefano-tittarelli.html',
        'name': 'Stefano Tittarelli, CFA',
        'title': 'Chief Executive Officer',
        'img': 'https://assets.zyrosite.com/YD0B9Plo46iLw9Z8/st-website3-YKbEeE1PGbhDPkga.JPG',
        'bio': '<p>With over 30 years of experience, Stefano has held key roles in the financial industry, including portfolio management, proprietary trading, and risk management. This unique blend of experience has equipped him with a deep understanding of market dynamics and a strong track record of success.</p><p>Stefano holds a Master in Economics and Social Sciences from Università Bocconi and is a CFA charterholder. He completed the Program for Management Development at Harvard Business School and obtained the Certificate in Corporate Governance from INSEAD.</p>'
    },
    {
        'file': 'luigi-mantrino.html',
        'name': 'Luigi Mantrino, CFA',
        'title': 'Chief Investment Officer',
        'img': 'https://assets.zyrosite.com/YD0B9Plo46iLw9Z8/lm-website2-mp81XvDqG8T9yLWa.JPG',
        'bio': '<p>Luigi has over 25 years of experience in the financial industry, primarily focused on fixed income and credit markets. His expertise spans across trading, portfolio management, and investment strategy, making him a seasoned professional in navigating complex market environments.</p><p>Luigi holds a Master in Economics and Business Administration from the University of Turin and is a CFA charterholder.</p>'
    },
    {
        'file': 'guillaume-di-liberatore.html',
        'name': 'Guillaume Di Liberatore, CFA',
        'title': 'Chief Research Officer',
        'img': 'https://assets.zyrosite.com/YD0B9Plo46iLw9Z8/gdl-website2-A1ab1lDJy8hx5Pqp.JPG',
        'bio': '<p>Guillaume has over 15 years of experience in credit research, specializing in European high-yield and investment-grade corporate bonds. His analytical rigor and deep understanding of credit fundamentals are invaluable assets to our investment team.</p><p>Guillaume holds a Master in Finance from Edhec Business School and is a CFA charterholder.</p>'
    },
    {
        'file': 'andrea-cavalleri.html',
        'name': 'Andrea Cavalleri',
        'title': 'Chairman',
        'img': 'https://assets.zyrosite.com/YD0B9Plo46iLw9Z8/ac-website3-dOqX1P08NocZngG2.JPG',
        'bio': '<p>Andrea brings extensive leadership experience to our board, having served in executive and board-level roles across various industries. His strategic vision and corporate governance expertise guide our firm\'s long-term growth and success.</p><p>Andrea holds a degree in Economics and Commerce from the University of Genoa.</p>'
    },
    {
        'file': 'henrik-hedman.html',
        'name': 'Henrik Hedman',
        'title': 'Director',
        'img': 'https://assets.zyrosite.com/YD0B9Plo46iLw9Z8/hh-website2-mePKv1o9kKSEwBjy.JPG',
        'bio': '<p>Henrik has a distinguished career in asset management and wealth advisory, with a strong focus on serving high-net-worth individuals and institutional clients. His deep market knowledge and client-centric approach are key to our business development efforts.</p><p>Henrik holds a degree in Business Administration from the Stockholm School of Economics.</p>'
    },
    {
        'file': 'balint-botos.html',
        'name': 'Balint Botos, CFA',
        'title': 'Director',
        'img': 'https://assets.zyrosite.com/YD0B9Plo46iLw9Z8/bb-website2-m7VvJkDMv9hP07Xv.JPG',
        'bio': '<p>Balint brings a wealth of experience in investment analysis and portfolio management. His rigorous quantitative skills and broad market expertise contribute significantly to our investment strategies and risk management framework.</p><p>Balint holds a Master in Finance from the Corvinus University of Budapest and is a CFA charterholder.</p>'
    }
]

for person in team_data:
    bio_content = f"""
    <div class="bio-container">
        <div class="bio-image-col">
            <img src="{person['img']}" alt="{person['name']}">
        </div>
        <div class="bio-content-col">
            <a href="our-people.html" class="bio-back">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                Back to Our People
            </a>
            <h1 class="bio-name">{person['name']}</h1>
            <div class="bio-title">{person['title']}</div>
            <div class="bio-text">
                {person['bio']}
            </div>
        </div>
    </div>
    """
    
    full_html = head_nav + bio_content + footer_scripts
    full_html = full_html.replace('<title>Alba Investment Partners</title>', f'<title>Alba Investment Partners - {person["name"]}</title>')
    
    with open(f"/Users/eliainnamorati/Desktop/ALBA WEBSITE/{person['file']}", 'w') as f:
        f.write(full_html)

print('Successfully generated all bio pages cleanly.')
