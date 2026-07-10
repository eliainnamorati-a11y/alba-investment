import os
import glob
import re

new_css_and_footer = """
    <style>
        /* Modern Elegant Footer CSS */
        .alba-footer {
            background-color: #112215;
            color: #ffffff;
            padding: 100px 10% 40px;
            font-family: 'Inter', sans-serif;
            position: relative;
            z-index: 20;
            border-top: 3px solid var(--gold);
        }
        
        .footer-container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .footer-top {
            display: flex;
            justify-content: space-between;
            gap: 60px;
            margin-bottom: 80px;
            align-items: flex-start;
        }

        .footer-brand {
            max-width: 350px;
        }

        .footer-logo {
            height: 70px;
            margin-bottom: 30px;
            object-fit: contain;
            opacity: 1;
        }

        .footer-mission {
            color: rgba(255, 255, 255, 0.6);
            font-size: 1.05rem;
            line-height: 1.7;
            margin: 0;
            font-weight: 300;
        }

        .footer-links-grid {
            display: flex;
            gap: 100px;
        }

        .footer-column h4 {
            color: var(--gold);
            font-size: 1.1rem;
            font-weight: 500;
            margin-bottom: 30px;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-family: 'Inter', sans-serif;
        }

        .footer-column a {
            display: block;
            color: rgba(255, 255, 255, 0.7);
            text-decoration: none;
            margin-bottom: 16px;
            font-size: 0.95rem;
            transition: all 0.3s ease;
            font-weight: 300;
        }

        .footer-column a:hover {
            color: #ffffff;
            transform: translateX(4px);
        }

        .footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .copyright {
            color: rgba(255, 255, 255, 0.4);
            font-size: 0.85rem;
            margin: 0;
        }

        .legal-links {
            display: flex;
            gap: 30px;
        }

        .legal-links a {
            color: rgba(255, 255, 255, 0.4);
            text-decoration: none;
            font-size: 0.85rem;
            transition: color 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .legal-links a:hover {
            color: var(--gold);
        }

        @media (max-width: 900px) {
            .footer-top { flex-direction: column; gap: 50px; margin-bottom: 50px; }
            .footer-links-grid { flex-direction: column; gap: 40px; }
            .alba-footer { padding: 80px 8% 40px; }
            .footer-bottom { flex-direction: column; gap: 20px; align-items: flex-start; }
            .legal-links { flex-direction: column; gap: 15px; }
        }
    </style>

    <footer class="alba-footer">
        <div class="footer-container">
            <div class="footer-top">
                <div class="footer-brand">
                    <img src="logos/light.png" alt="Alba Investment Partners" class="footer-logo">
                    <p class="footer-mission">Alba is an independent investment management boutique dedicated to providing superior risk-adjusted returns in fixed income and credit.</p>
                </div>
                
                <div class="footer-links-grid">
                    <div class="footer-column">
                        <h4>Firm</h4>
                        <a href="index.html">Home</a>
                        <a href="about.html">About Us</a>
                        <a href="insights.html">Insights</a>
                    </div>
                    <div class="footer-column">
                        <h4>Strategies</h4>
                        <a href="investment-approach.html">Investment Approach</a>
                        <a href="our-people.html">Our People</a>
                    </div>
                    <div class="footer-column">
                        <h4>Connect</h4>
                        <a href="contact.html">Contact</a>
                        <a href="#">LinkedIn</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p class="copyright">&copy; 2026 Alba Investment Partners. All rights reserved.</p>
                <div class="legal-links">
                    <a href="privacy-policy.html">Privacy Policy</a>
                    <a href="terms-of-use.html">Terms of Use</a>
                </div>
            </div>
        </div>
    </footer>
"""

html_files = glob.glob('**/*.html', recursive=True)
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We will replace the entire <footer class="alba-footer">...</footer> block.
    # To do this safely with regex, we match from <footer class="alba-footer"> to </footer>
    new_content = re.sub(r'<footer class="alba-footer">.*?</footer>', new_css_and_footer, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w') as f:
            f.write(new_content)
        print(f'Updated {file}')
